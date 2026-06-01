from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
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


def build_task_cache(
    spec: KaggleTaskSpec,
    train_csv: str | Path,
    output_path: str | Path,
    configs_per_task: int,
    epochs_per_config: int,
    split_seed: int,
    config_seed: int,
) -> None:
    prepared = prepare_tabular_regression_data(
        csv_path=train_csv,
        target_column=spec.target_column,
        split_seed=split_seed,
        split=(0.8, 0.1, 0.1),
    )
    rng = np.random.default_rng(config_seed)
    search_space = kaggle_mlp_search_space()
    configs = search_space.sample_many(rng, configs_per_task)
    records = []
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
    torch.manual_seed(seed)
    model = _TabularMLP(
        input_dim=prepared.x_train.shape[1],
        hidden_width=int(config["hidden_width"]),
        num_layers=int(config["num_layers"]),
        dropout=float(config["dropout"]),
    )
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=float(config["learning_rate"]),
        weight_decay=float(config["weight_decay"]),
    )
    x_train = torch.as_tensor(prepared.x_train, dtype=torch.float32)
    y_train = torch.as_tensor(prepared.y_train, dtype=torch.float32)
    x_val = torch.as_tensor(prepared.x_val, dtype=torch.float32)
    y_val = torch.as_tensor(prepared.y_val, dtype=torch.float32)
    x_test = torch.as_tensor(prepared.x_test, dtype=torch.float32)
    y_test = torch.as_tensor(prepared.y_test, dtype=torch.float32)

    batch_size = max(1, int(config["batch_size"]))
    learning_curve: list[float] = []
    for epoch in range(epochs):
        model.train()
        generator = torch.Generator().manual_seed(seed + epoch)
        permutation = torch.randperm(x_train.shape[0], generator=generator)
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
) -> PreparedRegressionData:
    rows = _read_csv_rows(Path(csv_path))
    if target_column not in rows[0]:
        raise ValueError(f"Target column {target_column!r} not found in {csv_path}")

    feature_columns = [
        key for key in rows[0] if key != target_column and key.lower() != "id"
    ]
    train_idx, val_idx, test_idx = _split_indices(len(rows), split_seed, split)
    numeric_columns = [
        column
        for column in feature_columns
        if _is_numeric_column(rows, train_idx, column)
    ]
    categorical_columns = [
        column for column in feature_columns if column not in numeric_columns
    ]

    numeric_stats = _fit_numeric_stats(rows, train_idx, numeric_columns)
    categorical_stats = _fit_categorical_stats(rows, train_idx, categorical_columns)
    x, feature_names = _transform_features(
        rows,
        numeric_columns,
        categorical_columns,
        numeric_stats,
        categorical_stats,
    )

    y = _target_array(rows, target_column)
    y_mean = float(y[train_idx].mean())
    target_std = float(y[train_idx].std())
    y_std = target_std if target_std > 0.0 else 1.0
    y_scaled = (y - y_mean) / y_std

    x_train = x[train_idx]
    meta_features = _hyp_rl_table1_meta_features(x_train)

    return PreparedRegressionData(
        x_train=x_train,
        y_train=y_scaled[train_idx],
        x_val=x[val_idx],
        y_val=y_scaled[val_idx],
        x_test=x[test_idx],
        y_test=y_scaled[test_idx],
        y_mean=y_mean,
        y_std=y_std,
        meta_features=meta_features,
        feature_names=tuple(feature_names),
    )


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"{path} has no rows")
    return rows


def _is_missing(value: object) -> bool:
    return value is None or str(value).strip() == ""


def _parse_finite_float(value: object) -> float | None:
    if _is_missing(value):
        return None
    try:
        parsed = float(str(value).strip())
    except ValueError:
        return None
    return parsed if math.isfinite(parsed) else None


def _is_nonfinite_number(value: object) -> bool:
    if _is_missing(value):
        return False
    try:
        parsed = float(str(value).strip())
    except ValueError:
        return False
    return not math.isfinite(parsed)


def _is_number(value: object) -> bool:
    return _parse_finite_float(value) is not None


def _is_numeric_column(
    rows: list[dict[str, str]], train_idx: np.ndarray, column: str
) -> bool:
    observed_finite = False
    for idx in train_idx:
        value = rows[int(idx)][column]
        if _is_missing(value):
            continue
        if _is_number(value):
            observed_finite = True
            continue
        if not _is_nonfinite_number(value):
            return False
    return observed_finite


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


def _fit_numeric_stats(
    rows: list[dict[str, str]],
    train_idx: np.ndarray,
    columns: list[str],
) -> dict[str, tuple[float, float, float]]:
    stats: dict[str, tuple[float, float, float]] = {}
    for column in columns:
        observed = np.asarray(
            [
                parsed
                for idx in train_idx
                if (parsed := _parse_finite_float(rows[int(idx)][column])) is not None
            ],
            dtype=np.float32,
        )
        median = float(np.median(observed)) if observed.size else 0.0
        filled = np.asarray(
            [
                parsed
                if (parsed := _parse_finite_float(rows[int(idx)][column])) is not None
                else median
                for idx in train_idx
            ],
            dtype=np.float32,
        )
        mean = float(filled.mean())
        std = float(filled.std())
        stats[column] = (median, mean, std if std > 0.0 else 1.0)
    return stats


def _fit_categorical_stats(
    rows: list[dict[str, str]],
    train_idx: np.ndarray,
    columns: list[str],
) -> dict[str, tuple[str, tuple[str, ...]]]:
    stats: dict[str, tuple[str, tuple[str, ...]]] = {}
    for column in columns:
        train_values = [
            str(rows[int(idx)][column]).strip()
            for idx in train_idx
            if not _is_missing(rows[int(idx)][column])
        ]
        if train_values:
            most_frequent = Counter(train_values).most_common(1)[0][0]
            categories = tuple(sorted(set(train_values)))
        else:
            most_frequent = ""
            categories = ()
        stats[column] = (most_frequent, categories)
    return stats


def _transform_features(
    rows: list[dict[str, str]],
    numeric_columns: list[str],
    categorical_columns: list[str],
    numeric_stats: dict[str, tuple[float, float, float]],
    categorical_stats: dict[str, tuple[str, tuple[str, ...]]],
) -> tuple[np.ndarray, list[str]]:
    feature_names = list(numeric_columns)
    for column in categorical_columns:
        _, categories = categorical_stats[column]
        feature_names.extend(f"{column}={category}" for category in categories)

    x = np.zeros((len(rows), len(feature_names)), dtype=np.float32)
    for row_idx, row in enumerate(rows):
        offset = 0
        for column in numeric_columns:
            median, mean, std = numeric_stats[column]
            value = _parse_finite_float(row[column])
            if value is None:
                value = median
            x[row_idx, offset] = (value - mean) / std
            offset += 1

        for column in categorical_columns:
            most_frequent, categories = categorical_stats[column]
            value = (
                most_frequent
                if _is_missing(row[column])
                else str(row[column]).strip()
            )
            if value in categories:
                x[row_idx, offset + categories.index(value)] = 1.0
            offset += len(categories)
    return x, feature_names


def _target_array(rows: list[dict[str, str]], target_column: str) -> np.ndarray:
    values = []
    for row in rows:
        value = row[target_column]
        if _is_missing(value):
            raise ValueError(f"Target column {target_column!r} contains missing values")
        values.append(float(value))
    return np.asarray(values, dtype=float)


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
