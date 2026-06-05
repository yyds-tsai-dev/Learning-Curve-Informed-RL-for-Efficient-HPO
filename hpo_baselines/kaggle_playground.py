from __future__ import annotations

import json
import math
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch

from .search_space import Config, Parameter, SearchSpace
from .tasks import EvalResult


@dataclass(frozen=True)
class KaggleTaskSpec:
    slug: str
    episode: str
    name: str
    target_column: str


@dataclass(frozen=True)
class KaggleMetricSpec:
    name: str
    direction: str
    reference_worst_percentile: float


@dataclass(frozen=True)
class KaggleCacheSpec:
    configs_per_task: int
    epochs_per_config: int
    seeds_per_config: int
    max_train_rows: int | None
    max_categories_per_column: int | None
    split_train: float
    split_validation: float
    split_test: float
    split_seed: int


@dataclass(frozen=True)
class KaggleManifest:
    snapshot_date: str
    metric: KaggleMetricSpec
    cache: KaggleCacheSpec
    nested_order: tuple[str, ...]
    tasks: tuple[KaggleTaskSpec, ...]

    @property
    def by_slug(self) -> dict[str, KaggleTaskSpec]:
        return {task.slug: task for task in self.tasks}


def load_manifest(path: str | Path) -> KaggleManifest:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    split = raw["cache"]["split"]
    manifest = KaggleManifest(
        snapshot_date=str(raw["snapshot_date"]),
        metric=KaggleMetricSpec(
            name=str(raw["metric"]["name"]),
            direction=str(raw["metric"]["direction"]),
            reference_worst_percentile=float(raw["metric"]["reference_worst_percentile"]),
        ),
        cache=KaggleCacheSpec(
            configs_per_task=int(raw["cache"]["configs_per_task"]),
            epochs_per_config=int(raw["cache"]["epochs_per_config"]),
            seeds_per_config=int(raw["cache"]["seeds_per_config"]),
            max_train_rows=(
                None
                if raw["cache"].get("max_train_rows") is None
                else int(raw["cache"]["max_train_rows"])
            ),
            max_categories_per_column=(
                None
                if raw["cache"].get("max_categories_per_column") is None
                else int(raw["cache"]["max_categories_per_column"])
            ),
            split_train=float(split["train"]),
            split_validation=float(split["validation"]),
            split_test=float(split["test"]),
            split_seed=int(split["seed"]),
        ),
        nested_order=tuple(str(slug) for slug in raw["nested_order"]),
        tasks=tuple(
            KaggleTaskSpec(
                slug=str(item["slug"]),
                episode=str(item["episode"]),
                name=str(item["name"]),
                target_column=str(item["target_column"]),
            )
            for item in raw["tasks"]
        ),
    )
    _validate_manifest(manifest)
    return manifest


def nested_task_slugs(manifest: KaggleManifest, count: int) -> list[str]:
    if count not in {1, 5, 10, 15}:
        raise ValueError("count must be one of 1, 5, 10, 15")
    return list(manifest.nested_order[:count])


def kaggle_mlp_search_space() -> SearchSpace:
    return SearchSpace(
        [
            Parameter("learning_rate", "float", low=1e-4, high=1e-1, log=True),
            Parameter("weight_decay", "float", low=0.0, high=1e-2),
            Parameter("hidden_width", "int", low=32, high=512, log=True),
            Parameter("num_layers", "int", low=1, high=4),
            Parameter("dropout", "float", low=0.0, high=0.5),
            Parameter("batch_size", "categorical", choices=(16, 32, 64, 128, 256)),
        ]
    )


def normalized_simple_regret_reference(
    validation_scores: list[float] | np.ndarray, percentile: float = 90
) -> tuple[float, float]:
    try:
        scores = np.asarray(validation_scores, dtype=float)
    except (TypeError, ValueError) as exc:
        raise ValueError("validation_scores must contain only finite values") from exc
    if scores.ndim != 1:
        raise ValueError("validation_scores must be a 1D sequence")
    if scores.size == 0:
        raise ValueError("validation_scores must be non-empty")
    if not np.all(np.isfinite(scores)):
        raise ValueError("validation_scores must contain only finite values")
    try:
        percentile = float(percentile)
    except (TypeError, ValueError) as exc:
        raise ValueError("percentile must be in [0, 100]") from exc
    if not math.isfinite(percentile) or not 0 <= percentile <= 100:
        raise ValueError("percentile must be in [0, 100]")

    oracle = float(np.min(scores))
    reference = float(np.percentile(scores, percentile))
    if reference <= oracle:
        reference = oracle + _normalizer_eps(oracle)
    return oracle, reference


def normalized_simple_regret(
    best_val_score: float, oracle: float, reference: float
) -> float:
    best = float(best_val_score)
    oracle = float(oracle)
    reference = float(reference)
    if not all(math.isfinite(value) for value in (best, oracle, reference)):
        raise ValueError("best_val_score, oracle, and reference must be finite")
    if reference <= oracle:
        reference = oracle + _normalizer_eps(oracle)
    return float((best - oracle) / (reference - oracle))


def _normalizer_eps(oracle: float) -> float:
    return max(abs(float(oracle)), 1.0) * 1e-12


class KaggleRegressionTask:
    def __init__(self, cache_path: str | Path) -> None:
        self.cache_path = Path(cache_path)
        raw = json.loads(self.cache_path.read_text(encoding="utf-8"))
        task = raw["task"]
        self.slug = str(task["slug"])
        self.display_name = str(task.get("display_name", task.get("name", self.slug)))
        self.name = self.slug
        self.search_space = kaggle_mlp_search_space()

        meta_features = np.asarray(
            task.get("meta_features", raw.get("meta_features")), dtype=float
        )
        if meta_features.shape != (16,):
            raise ValueError("Kaggle cache meta_features must have shape (16,)")
        self._meta_features = meta_features

        self._metric_name = str(raw.get("metric", {}).get("name", "RMSE"))
        if self._metric_name != "RMSE":
            raise ValueError("Kaggle cache metric.name must be RMSE")
        config_records = self._validate_config_records(raw["configs"])
        val_scores = [float(item["val_score"]) for _, item in config_records]
        self.oracle_val_score, self.reference_worst_val_score = (
            normalized_simple_regret_reference(val_scores, percentile=90)
        )
        self.candidate_configs: list[Config] = []
        self._by_id: dict[str, dict[str, Any]] = {}
        for config_id, item in config_records:
            config = dict(item["config"])
            config["__config_id__"] = int(config_id)
            self.candidate_configs.append(config)
            self._by_id[config_id] = item
        self.candidate_vectors = self.search_space.to_matrix(self.candidate_configs)

    def _validate_config_records(
        self, raw_configs: Any
    ) -> list[tuple[str, dict[str, Any]]]:
        if not raw_configs:
            raise ValueError(f"Kaggle cache {self.cache_path} must contain configs")

        required_keys = {parameter.name for parameter in self.search_space.parameters}
        seen_ids: set[str] = set()
        records: list[tuple[str, dict[str, Any]]] = []
        for index, item in enumerate(raw_configs):
            if not isinstance(item, dict):
                raise ValueError(
                    f"Kaggle cache {self.cache_path} config index {index} "
                    "must be an object"
                )
            if "config_id" not in item:
                raise ValueError(
                    f"Kaggle cache {self.cache_path} config index {index} "
                    "must contain config_id"
                )
            config_id = self._normalize_config_id(item["config_id"])
            if config_id in seen_ids:
                raise ValueError(
                    f"Kaggle cache {self.cache_path} config_id={config_id} "
                    "is duplicate"
                )
            seen_ids.add(config_id)

            config = item.get("config")
            if not isinstance(config, dict):
                raise ValueError(
                    f"Kaggle cache {self.cache_path} config_id={config_id} "
                    "must contain config object"
                )
            missing = sorted(required_keys - set(config))
            if missing:
                raise ValueError(
                    f"Kaggle cache {self.cache_path} config_id={config_id} "
                    f"missing config fields: {missing}"
                )

            for score_key in ("val_score", "test_score"):
                self._require_finite(item.get(score_key), config_id, score_key)
            learning_curve = item.get("learning_curve")
            if not isinstance(learning_curve, list) or not learning_curve:
                raise ValueError(
                    f"Kaggle cache {self.cache_path} config_id={config_id} "
                    "learning_curve must be a non-empty list"
                )
            for curve_index, value in enumerate(learning_curve):
                self._require_finite(
                    value, config_id, f"learning_curve[{curve_index}]"
                )
            records.append((config_id, item))
        return records

    def _normalize_config_id(self, raw_config_id: Any) -> str:
        if isinstance(raw_config_id, bool):
            raise ValueError(
                f"Kaggle cache {self.cache_path} config_id={raw_config_id!r} "
                "must be an integer or integer string"
            )
        if isinstance(raw_config_id, int):
            return str(raw_config_id)
        if isinstance(raw_config_id, str) and re.fullmatch(r"\d+", raw_config_id):
            return str(int(raw_config_id))
        raise ValueError(
            f"Kaggle cache {self.cache_path} config_id={raw_config_id!r} "
            "must be an integer or integer string"
        )

    def _require_finite(self, value: Any, config_id: str, field: str) -> None:
        try:
            finite = math.isfinite(float(value))
        except (TypeError, ValueError) as exc:
            raise ValueError(
                f"Kaggle cache {self.cache_path} config_id={config_id} "
                f"{field} must be finite"
            ) from exc
        if not finite:
            raise ValueError(
                f"Kaggle cache {self.cache_path} config_id={config_id} "
                f"{field} must be finite"
            )

    def evaluate(self, config: Config, seed: int = 0) -> EvalResult:
        del seed
        if "__config_id__" in config:
            config_id = str(config["__config_id__"])
        else:
            config_id = str(self._nearest_config_id(config))
        item = self._by_id[config_id]
        learning_curve = [float(value) for value in item["learning_curve"]]
        return EvalResult(
            val_score=float(item["val_score"]),
            test_score=float(item["test_score"]),
            learning_curve=learning_curve,
            metadata={
                "task": self.slug,
                "config_id": int(config_id) if config_id.isdecimal() else config_id,
                "metric": self._metric_name,
                "normalizer": {
                    "oracle_val_score": self.oracle_val_score,
                    "reference_worst_val_score": self.reference_worst_val_score,
                },
            },
        )

    def meta_features(self) -> np.ndarray:
        return self._meta_features.copy()

    def metric_name(self) -> str:
        return self._metric_name

    def _nearest_config_id(self, config: Config) -> int | str:
        vector = self.search_space.to_vector(config)
        distances = np.linalg.norm(self.candidate_vectors - vector, axis=1)
        return self.candidate_configs[int(np.argmin(distances))]["__config_id__"]


def _validate_manifest(manifest: KaggleManifest) -> None:
    if manifest.snapshot_date != "2026-06-01":
        raise ValueError("snapshot_date must be 2026-06-01")
    if manifest.metric.name != "RMSE":
        raise ValueError("metric.name must be RMSE")
    if manifest.metric.direction != "minimize":
        raise ValueError("metric.direction must be minimize")
    if manifest.metric.reference_worst_percentile != 90:
        raise ValueError("metric.reference_worst_percentile must be 90")

    cache = manifest.cache
    if cache.configs_per_task != 256:
        raise ValueError("cache.configs_per_task must be 256")
    if cache.epochs_per_config != 25:
        raise ValueError("cache.epochs_per_config must be 25")
    if cache.seeds_per_config != 1:
        raise ValueError("cache.seeds_per_config must be 1")
    if cache.max_train_rows != 2_000:
        raise ValueError("cache.max_train_rows must be 2000")
    if cache.max_categories_per_column != 32:
        raise ValueError("cache.max_categories_per_column must be 32")
    if (cache.split_train, cache.split_validation, cache.split_test) != (0.8, 0.1, 0.1):
        raise ValueError("cache split must be 80/10/10")
    if cache.split_seed != 20260601:
        raise ValueError("cache split seed must be 20260601")

    slugs = [task.slug for task in manifest.tasks]
    if len(slugs) != 15:
        raise ValueError(f"Expected 15 Kaggle tasks, found {len(slugs)}")
    if len(set(slugs)) != len(slugs):
        raise ValueError("Kaggle task slugs must be unique")

    nested_order = list(manifest.nested_order)
    if len(nested_order) != 15:
        raise ValueError("nested_order must contain 15 task slugs")
    if len(set(nested_order)) != len(nested_order):
        raise ValueError("nested_order slugs must be unique")
    missing = sorted(set(nested_order) - set(slugs))
    if missing:
        raise ValueError(f"nested_order contains unknown task slugs: {missing}")


@dataclass(frozen=True)
class PreparedRegressionData:
    x_train: np.ndarray
    y_train: np.ndarray
    x_val: np.ndarray
    y_val: np.ndarray
    x_test: np.ndarray
    y_test: np.ndarray
    y_mean: float
    y_std: float
    meta_features: np.ndarray
    feature_names: tuple[str, ...]


class _TabularMLP(torch.nn.Module):
    def __init__(
        self,
        input_dim: int,
        hidden_width: int,
        num_layers: int,
        dropout: float,
    ) -> None:
        super().__init__()
        layers: list[torch.nn.Module] = []
        width = int(hidden_width)
        previous_dim = input_dim
        for _ in range(int(num_layers)):
            layers.append(torch.nn.Linear(previous_dim, width))
            layers.append(torch.nn.ReLU())
            if dropout > 0.0:
                layers.append(torch.nn.Dropout(float(dropout)))
            previous_dim = width
        layers.append(torch.nn.Linear(previous_dim, 1))
        self.network = torch.nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x).squeeze(-1)


def _cache_training_device() -> torch.device:
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def build_task_cache(
    spec: KaggleTaskSpec,
    train_csv: str | Path,
    output_path: str | Path,
    configs_per_task: int,
    epochs_per_config: int,
    split_seed: int,
    config_seed: int,
    max_train_rows: int | None = None,
    max_categories_per_column: int | None = None,
) -> None:
    if configs_per_task <= 0:
        raise ValueError("configs_per_task must be positive")
    if epochs_per_config <= 0:
        raise ValueError("epochs_per_config must be positive")
    if max_train_rows is not None and max_train_rows <= 0:
        raise ValueError("max_train_rows must be positive when provided")
    if max_categories_per_column is not None and max_categories_per_column <= 0:
        raise ValueError("max_categories_per_column must be positive when provided")

    prepare_started_at = time.time()
    print(
        f"{spec.slug}: preparing data with max_train_rows={max_train_rows}",
        flush=True,
    )
    prepared = prepare_tabular_regression_data(
        csv_path=train_csv,
        target_column=spec.target_column,
        split_seed=split_seed,
        split=(0.8, 0.1, 0.1),
        max_train_rows=max_train_rows,
        max_categories_per_column=max_categories_per_column,
    )
    print(
        f"{spec.slug}: prepared train={prepared.x_train.shape} "
        f"val={prepared.x_val.shape} test={prepared.x_test.shape} "
        f"in {time.time() - prepare_started_at:.1f}s",
        flush=True,
    )
    rng = np.random.default_rng(config_seed)
    search_space = kaggle_mlp_search_space()
    configs = search_space.sample_many(rng, configs_per_task)
    records = []
    started_at = time.time()
    for config_id, config in enumerate(configs):
        serializable_config = _json_serializable_config(config)
        result = _train_cached_mlp(
            prepared=prepared,
            config=serializable_config,
            epochs=epochs_per_config,
            seed=config_seed + config_id,
        )
        _require_finite_cache_value(result["val_score"], config_id, "val_score")
        _require_finite_cache_value(result["test_score"], config_id, "test_score")
        learning_curve = result["learning_curve"]
        if not isinstance(learning_curve, list) or not learning_curve:
            raise ValueError(
                f"Kaggle cache config_id={config_id} "
                "learning_curve must be a non-empty list"
            )
        for curve_index, value in enumerate(learning_curve):
            _require_finite_cache_value(
                value, config_id, f"learning_curve[{curve_index}]"
            )
        records.append(
            {
                "config_id": config_id,
                "config": serializable_config,
                "val_score": result["val_score"],
                "test_score": result["test_score"],
                "learning_curve": learning_curve,
            }
        )
        if (config_id + 1) % 16 == 0 or config_id + 1 == configs_per_task:
            elapsed = time.time() - started_at
            print(
                f"{spec.slug}: cached {config_id + 1}/{configs_per_task} "
                f"configs in {elapsed:.1f}s",
                flush=True,
            )

    cache = {
        "task": {
            "slug": spec.slug,
            "name": spec.name,
            "target_column": spec.target_column,
        },
        "meta_features": [float(value) for value in prepared.meta_features],
        "metric": {
            "name": "RMSE",
            "direction": "minimize",
            "reference_worst_percentile": 90,
        },
        "cache": {
            "max_train_rows": max_train_rows,
            "max_categories_per_column": max_categories_per_column,
            "split": {"train": 0.8, "validation": 0.1, "test": 0.1},
            "split_seed": split_seed,
        },
        "configs": records,
    }
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(cache, indent=2, allow_nan=False), encoding="utf-8"
    )


def _require_finite_cache_value(value: Any, config_id: int, field: str) -> None:
    try:
        finite = math.isfinite(float(value))
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"Kaggle cache config_id={config_id} {field} must be finite"
        ) from exc
    if not finite:
        raise ValueError(f"Kaggle cache config_id={config_id} {field} must be finite")


def _json_serializable_config(config: Config) -> dict[str, int | float]:
    serializable: dict[str, int | float] = {}
    for key, value in config.items():
        if isinstance(value, bool):
            serializable[key] = int(value)
        elif isinstance(value, (np.integer, int)):
            serializable[key] = int(value)
        elif isinstance(value, (np.floating, float)):
            serializable[key] = float(value)
        else:
            serializable[key] = value
    return serializable


def _train_cached_mlp(
    prepared: PreparedRegressionData,
    config: Config,
    epochs: int,
    seed: int,
) -> dict[str, float | list[float]]:
    device = _cache_training_device()
    torch.manual_seed(seed)
    if device.type == "mps":
        torch.mps.manual_seed(seed)
    model = _TabularMLP(
        input_dim=prepared.x_train.shape[1],
        hidden_width=int(config["hidden_width"]),
        num_layers=int(config["num_layers"]),
        dropout=float(config["dropout"]),
    ).to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=float(config["learning_rate"]),
        weight_decay=float(config["weight_decay"]),
    )
    x_train = torch.as_tensor(prepared.x_train, dtype=torch.float32, device=device)
    y_train = torch.as_tensor(prepared.y_train, dtype=torch.float32, device=device)
    x_val = torch.as_tensor(prepared.x_val, dtype=torch.float32, device=device)
    y_val = torch.as_tensor(prepared.y_val, dtype=torch.float32, device=device)
    x_test = torch.as_tensor(prepared.x_test, dtype=torch.float32, device=device)
    y_test = torch.as_tensor(prepared.y_test, dtype=torch.float32, device=device)

    batch_size = max(1, int(config["batch_size"]))
    learning_curve: list[float] = []
    for epoch in range(epochs):
        model.train()
        generator = torch.Generator(device=device).manual_seed(seed + epoch)
        permutation = torch.randperm(
            x_train.shape[0], generator=generator, device=device
        )
        for start in range(0, x_train.shape[0], batch_size):
            batch_indices = permutation[start : start + batch_size]
            prediction = model(x_train[batch_indices])
            loss = torch.nn.functional.mse_loss(prediction, y_train[batch_indices])
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_prediction = model(x_val)
            val_rmse = _rmse(val_prediction, y_val) * prepared.y_std
        learning_curve.append(float(val_rmse))

    model.eval()
    with torch.no_grad():
        test_prediction = model(x_test)
        test_rmse = _rmse(test_prediction, y_test) * prepared.y_std
    return {
        "val_score": float(learning_curve[-1]),
        "test_score": float(test_rmse),
        "learning_curve": learning_curve,
    }


def _rmse(prediction: torch.Tensor, target: torch.Tensor) -> float:
    mse = torch.mean((prediction - target) ** 2)
    return float(torch.sqrt(mse).item())


def prepare_tabular_regression_data(
    csv_path: str | Path,
    target_column: str,
    split_seed: int,
    split: tuple[float, float, float],
    max_train_rows: int | None = None,
    max_categories_per_column: int | None = None,
) -> PreparedRegressionData:
    frame = pd.read_csv(Path(csv_path), dtype=str, keep_default_na=False)
    if frame.empty:
        raise ValueError(f"{csv_path} has no rows")
    if target_column not in frame.columns:
        raise ValueError(f"Target column {target_column!r} not found in {csv_path}")
    if max_train_rows is not None and max_train_rows <= 0:
        raise ValueError("max_train_rows must be positive when provided")
    if max_categories_per_column is not None and max_categories_per_column <= 0:
        raise ValueError("max_categories_per_column must be positive when provided")

    feature_columns = [
        key for key in frame.columns if key != target_column and key.lower() != "id"
    ]
    train_idx, val_idx, test_idx = _split_indices(len(frame), split_seed, split)
    numeric_columns = [
        column
        for column in feature_columns
        if _is_pandas_numeric_column(frame[column].iloc[train_idx])
    ]
    categorical_columns = [
        column for column in feature_columns if column not in numeric_columns
    ]

    numeric_stats = _fit_pandas_numeric_stats(frame, train_idx, numeric_columns)
    categorical_stats = _fit_pandas_categorical_stats(
        frame, train_idx, categorical_columns, max_categories_per_column
    )
    feature_names = _pandas_feature_names(
        numeric_columns,
        categorical_columns,
        categorical_stats,
    )
    capped_train_idx = _cap_train_indices(train_idx, max_train_rows, split_seed)

    y = _pandas_target_array(frame[target_column], target_column)
    y_mean = float(y[train_idx].mean())
    target_std = float(y[train_idx].std())
    y_std = target_std if target_std > 0.0 else 1.0
    y_scaled = (y - y_mean) / y_std

    x_train = _transform_pandas_features(
        frame,
        capped_train_idx,
        numeric_columns,
        categorical_columns,
        numeric_stats,
        categorical_stats,
        feature_names,
    )
    meta_features = _hyp_rl_table1_meta_features(x_train)

    return PreparedRegressionData(
        x_train=x_train,
        y_train=y_scaled[capped_train_idx],
        x_val=_transform_pandas_features(
            frame,
            val_idx,
            numeric_columns,
            categorical_columns,
            numeric_stats,
            categorical_stats,
            feature_names,
        ),
        y_val=y_scaled[val_idx],
        x_test=_transform_pandas_features(
            frame,
            test_idx,
            numeric_columns,
            categorical_columns,
            numeric_stats,
            categorical_stats,
            feature_names,
        ),
        y_test=y_scaled[test_idx],
        y_mean=y_mean,
        y_std=y_std,
        meta_features=meta_features,
        feature_names=tuple(feature_names),
    )


def _cap_train_indices(
    train_idx: np.ndarray, max_train_rows: int | None, seed: int
) -> np.ndarray:
    if max_train_rows is None or train_idx.size <= max_train_rows:
        return train_idx
    rng = np.random.default_rng(seed + 17)
    selected = rng.choice(train_idx, size=max_train_rows, replace=False)
    return np.sort(selected)


def _stripped_series(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip()


def _missing_mask(values: pd.Series) -> pd.Series:
    return values == ""


def _nonfinite_literal_mask(values: pd.Series) -> pd.Series:
    lowered = values.str.lower()
    return lowered.isin(
        {
            "nan",
            "+nan",
            "-nan",
            "inf",
            "+inf",
            "-inf",
            "infinity",
            "+infinity",
            "-infinity",
        }
    )


def _numeric_series(values: pd.Series) -> np.ndarray:
    stripped = _stripped_series(values)
    parsed = pd.to_numeric(stripped.mask(_missing_mask(stripped)), errors="coerce")
    return parsed.to_numpy(dtype=float)


def _is_pandas_numeric_column(values: pd.Series) -> bool:
    stripped = _stripped_series(values)
    missing = _missing_mask(stripped)
    parsed = pd.to_numeric(stripped.mask(missing), errors="coerce")
    parsed_values = parsed.to_numpy(dtype=float)
    finite = np.isfinite(parsed_values)
    invalid_non_numeric = (
        ~missing
        & pd.isna(parsed)
        & ~_nonfinite_literal_mask(stripped)
    )
    return bool(finite.any() and not invalid_non_numeric.any())


def _split_indices(
    n_rows: int,
    seed: int,
    split: tuple[float, float, float],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if len(split) != 3:
        raise ValueError("split must contain train, validation, and test fractions")
    if any(part <= 0.0 for part in split):
        raise ValueError("split fractions must be positive")
    if abs(sum(split) - 1.0) > 1e-8:
        raise ValueError("split fractions must sum to 1.0")

    rng = np.random.default_rng(seed)
    indices = rng.permutation(n_rows)
    n_train = int(round(n_rows * split[0]))
    n_val = int(round(n_rows * split[1]))
    n_test = n_rows - n_train - n_val
    if min(n_train, n_val, n_test) <= 0:
        raise ValueError("Split produced an empty partition")
    return (
        indices[:n_train],
        indices[n_train : n_train + n_val],
        indices[n_train + n_val :],
    )


def _fit_pandas_numeric_stats(
    frame: pd.DataFrame,
    train_idx: np.ndarray,
    columns: list[str],
) -> dict[str, tuple[float, float, float]]:
    stats: dict[str, tuple[float, float, float]] = {}
    for column in columns:
        parsed = _numeric_series(frame[column].iloc[train_idx])
        finite = parsed[np.isfinite(parsed)]
        median = float(np.median(finite)) if finite.size else 0.0
        filled = np.where(np.isfinite(parsed), parsed, median).astype(np.float32)
        mean = float(filled.mean())
        std = float(filled.std())
        stats[column] = (median, mean, std if std > 0.0 else 1.0)
    return stats


def _fit_pandas_categorical_stats(
    frame: pd.DataFrame,
    train_idx: np.ndarray,
    columns: list[str],
    max_categories_per_column: int | None,
) -> dict[str, tuple[str, tuple[str, ...]]]:
    stats: dict[str, tuple[str, tuple[str, ...]]] = {}
    for column in columns:
        train_values = _stripped_series(frame[column].iloc[train_idx])
        train_values = train_values[~_missing_mask(train_values)]
        if not train_values.empty:
            most_frequent = str(train_values.mode(dropna=False).iloc[0])
            value_counts = train_values.value_counts()
            ranked = sorted(
                value_counts.items(), key=lambda item: (-int(item[1]), str(item[0]))
            )
            if max_categories_per_column is not None:
                ranked = ranked[:max_categories_per_column]
            categories = tuple(sorted(str(value) for value, _ in ranked))
        else:
            most_frequent = ""
            categories = ()
        stats[column] = (most_frequent, categories)
    return stats


def _pandas_feature_names(
    numeric_columns: list[str],
    categorical_columns: list[str],
    categorical_stats: dict[str, tuple[str, tuple[str, ...]]],
) -> list[str]:
    feature_names = list(numeric_columns)
    for column in categorical_columns:
        _, categories = categorical_stats[column]
        feature_names.extend(f"{column}={category}" for category in categories)
    return feature_names


def _transform_pandas_features(
    frame: pd.DataFrame,
    row_idx: np.ndarray,
    numeric_columns: list[str],
    categorical_columns: list[str],
    numeric_stats: dict[str, tuple[float, float, float]],
    categorical_stats: dict[str, tuple[str, tuple[str, ...]]],
    feature_names: list[str],
) -> np.ndarray:
    x = np.zeros((len(row_idx), len(feature_names)), dtype=np.float32)
    offset = 0
    for column in numeric_columns:
        median, mean, std = numeric_stats[column]
        parsed = _numeric_series(frame[column].iloc[row_idx])
        filled = np.where(np.isfinite(parsed), parsed, median).astype(np.float32)
        x[:, offset] = (filled - mean) / std
        offset += 1

    rows = np.arange(len(row_idx))
    for column in categorical_columns:
        most_frequent, categories = categorical_stats[column]
        width = len(categories)
        if width:
            values = _stripped_series(frame[column].iloc[row_idx])
            values = values.mask(_missing_mask(values), most_frequent)
            category_to_code = {category: index for index, category in enumerate(categories)}
            codes = values.map(category_to_code).to_numpy()
            known = codes >= 0
            x[rows[known], offset + codes[known].astype(int)] = 1.0
        offset += width
    return x


def _pandas_target_array(series: pd.Series, target_column: str) -> np.ndarray:
    values = _stripped_series(series)
    if _missing_mask(values).any():
        raise ValueError(f"Target column {target_column!r} contains missing values")
    parsed = pd.to_numeric(values, errors="coerce").to_numpy(dtype=float)
    if not np.all(np.isfinite(parsed)):
        raise ValueError(f"Target column {target_column!r} must contain finite values")
    return parsed


def _hyp_rl_table1_meta_features(x_train: np.ndarray) -> np.ndarray:
    n_instances = int(x_train.shape[0])
    n_features = int(x_train.shape[1]) if x_train.ndim == 2 else 0
    dataset_dimensionality = n_features / max(n_instances, 1)
    inverse_dataset_dimensionality = n_instances / max(n_features, 1)
    skewness, kurtosis = _column_skewness_and_kurtosis(x_train)

    return np.asarray(
        [
            n_instances,
            math.log1p(n_instances),
            n_features,
            math.log1p(n_features),
            dataset_dimensionality,
            math.log1p(dataset_dimensionality),
            inverse_dataset_dimensionality,
            math.log1p(inverse_dataset_dimensionality),
            *_summary_stats(kurtosis),
            *_summary_stats(skewness),
        ],
        dtype=float,
    )


def _column_skewness_and_kurtosis(x_train: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    if x_train.ndim != 2 or x_train.shape[1] == 0:
        empty = np.asarray([], dtype=float)
        return empty, empty

    x = x_train.astype(float, copy=False)
    mean = x.mean(axis=0)
    std = x.std(axis=0)
    non_constant = std > 0.0
    skewness = np.zeros(x.shape[1], dtype=float)
    kurtosis = np.zeros(x.shape[1], dtype=float)

    if np.any(non_constant):
        z = (x[:, non_constant] - mean[non_constant]) / std[non_constant]
        skewness[non_constant] = np.mean(z**3, axis=0)
        kurtosis[non_constant] = np.mean(z**4, axis=0) - 3.0

    return skewness, kurtosis


def _summary_stats(values: np.ndarray) -> tuple[float, float, float, float]:
    if values.size == 0:
        return 0.0, 0.0, 0.0, 0.0
    return (
        float(np.min(values)),
        float(np.max(values)),
        float(np.mean(values)),
        float(np.std(values)),
    )
