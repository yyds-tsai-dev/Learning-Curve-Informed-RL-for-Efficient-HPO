from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

import numpy as np

from .search_space import Config, Parameter, SearchSpace

np.seterr(over="ignore", invalid="ignore", divide="ignore")

type LCBenchData = dict[str, Any]


@dataclass(slots=True)
class EvalResult:
    val_score: float
    test_score: float
    learning_curve: list[float]
    metadata: dict[str, Any]


class SyntheticRegressionTask:
    """Small deterministic regression HPO task with validation learning curves.

    The task trains a linear model by mini-batch SGD. Hyperparameters affect the
    optimizer dynamics, so each evaluation produces both a final validation RMSE
    and a full validation learning curve for RL-style methods.
    """

    def __init__(
        self,
        name: str = "toy_synthetic_regression",
        seed: int = 7,
        n_features: int = 12,
        n_train: int = 512,
        n_val: int = 192,
        n_test: int = 192,
        noise: float = 0.35,
        epochs: int = 18,
    ) -> None:
        self.name = name
        self.seed = seed
        self.n_features = n_features
        self.epochs = epochs
        rng = np.random.default_rng(seed)
        n_total = n_train + n_val + n_test

        x = rng.normal(size=(n_total, n_features))
        true_w = rng.normal(size=n_features)
        nonlinear = 0.45 * np.sin(x[:, 0] * x[:, 1]) + 0.25 * (x[:, 2] ** 2)
        y = x @ true_w + nonlinear + rng.normal(scale=noise, size=n_total)

        x_mean = x[:n_train].mean(axis=0)
        x_std = x[:n_train].std(axis=0) + 1e-8
        y_mean = y[:n_train].mean()
        y_std = y[:n_train].std() + 1e-8
        x = (x - x_mean) / x_std
        y = (y - y_mean) / y_std

        self.x_train = x[:n_train]
        self.y_train = y[:n_train]
        self.x_val = x[n_train : n_train + n_val]
        self.y_val = y[n_train : n_train + n_val]
        self.x_test = x[n_train + n_val :]
        self.y_test = y[n_train + n_val :]
        self.search_space = SearchSpace(
            [
                Parameter("learning_rate", "float", low=1e-4, high=5e-2, log=True),
                Parameter("l2", "float", low=1e-7, high=1e-1, log=True),
                Parameter("momentum", "float", low=0.0, high=0.9),
                Parameter("batch_size", "categorical", choices=(16, 32, 64, 128)),
            ]
        )

    @staticmethod
    def metric_name() -> str:
        return "RMSE"

    def evaluate(self, config: Config, seed: int) -> EvalResult:
        rng = np.random.default_rng(seed)
        learning_rate = float(config["learning_rate"])
        l2 = float(config["l2"])
        momentum = float(config["momentum"])
        batch_size = int(config["batch_size"])

        weights = rng.normal(scale=0.01, size=self.n_features)
        bias = 0.0
        velocity_w = np.zeros_like(weights)
        velocity_b = 0.0
        curve: list[float] = []

        for _ in range(self.epochs):
            order = rng.permutation(len(self.x_train))
            for start in range(0, len(order), batch_size):
                idx = order[start : start + batch_size]
                xb = self.x_train[idx]
                yb = self.y_train[idx]
                with np.errstate(over="ignore", invalid="ignore"):
                    pred = xb @ weights + bias
                    error = pred - yb
                    grad_w = (xb.T @ error) / len(idx) + l2 * weights
                    grad_b = float(error.mean())
                grad_norm = float(np.linalg.norm(grad_w))
                if grad_norm > 10.0:
                    grad_w *= 10.0 / (grad_norm + 1e-12)

                velocity_w = momentum * velocity_w + grad_w
                velocity_b = momentum * velocity_b + grad_b
                weights -= learning_rate * velocity_w
                bias -= learning_rate * velocity_b
                if not np.all(np.isfinite(weights)) or not np.isfinite(bias):
                    return self._failed_result(curve)
                if np.linalg.norm(weights) > 1e4 or abs(bias) > 1e4:
                    return self._failed_result(curve)

            val_rmse = self._rmse(self.x_val, self.y_val, weights, bias)
            if not np.isfinite(val_rmse):
                val_rmse = 1e6
            curve.append(float(min(val_rmse, 1e6)))

        test_rmse = self._rmse(self.x_test, self.y_test, weights, bias)
        if not np.isfinite(test_rmse):
            test_rmse = 1e6

        return EvalResult(
            val_score=float(curve[-1]),
            test_score=float(min(test_rmse, 1e6)),
            learning_curve=curve,
            metadata={"epochs": self.epochs},
        )

    @staticmethod
    def _rmse(x: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float) -> float:
        with np.errstate(over="ignore", invalid="ignore"):
            pred = x @ weights + bias
            value = np.sqrt(np.mean((pred - y) ** 2))
        if not np.isfinite(value):
            return 1e6
        return float(value)

    def _failed_result(self, partial_curve: list[float]) -> EvalResult:
        curve = partial_curve + [1e6] * (self.epochs - len(partial_curve))
        return EvalResult(
            val_score=1e6,
            test_score=1e6,
            learning_curve=curve,
            metadata={"epochs": self.epochs, "failed": True},
        )


class LCBenchTask:
    """LCBench tabular HPO task.

    LCBench stores a finite table of neural-network hyperparameter configurations
    and per-epoch learning curves. This adapter exposes one OpenML dataset as an
    HPO task where each action selects a precomputed configuration.
    """

    def __init__(
        self,
        data_path: str | Path,
        dataset_name: str | None = None,
        val_metric_tag: str = "Train/val_accuracy",
        test_metric_tag: str = "final_test_accuracy",
        limit_configs: int | None = None,
        data: LCBenchData | None = None,
    ) -> None:
        self.data_path = Path(data_path)
        if data is None:
            self.data = json.loads(self.data_path.read_text(encoding="utf-8"))
        else:
            self.data = data
        self.dataset_name = dataset_name or sorted(self.data.keys())[0]
        if self.dataset_name not in self.data:
            raise ValueError(
                f"Dataset {self.dataset_name!r} not found in {self.data_path}"
            )
        self.name = f"lcbench_{self.dataset_name}"
        self.val_metric_tag = self._resolve_tag(val_metric_tag, preferred=True)
        self.test_metric_tag = self._resolve_tag(test_metric_tag, preferred=False)
        self._score_from_accuracy = "accuracy" in self.val_metric_tag.lower()

        config_ids = sorted(self.data[self.dataset_name], key=int)
        if limit_configs is not None:
            config_ids = config_ids[:limit_configs]
        self.config_ids = config_ids
        self.candidate_configs = [
            self._config_with_id(config_id) for config_id in config_ids
        ]
        self.search_space = self._build_search_space(self.candidate_configs)
        self.candidate_vectors = self.search_space.to_matrix(self.candidate_configs)
        self._meta_features = self._read_meta_features()

    @staticmethod
    def metric_name() -> str:
        return "validation loss"

    def evaluate(self, config: Config, seed: int = 0) -> EvalResult:
        del seed
        config_id = str(config.get("__config_id__", self._nearest_config_id(config)))
        val_curve_raw = self._query_curve(config_id, self.val_metric_tag)
        test_curve_raw = self._query_curve(config_id, self.test_metric_tag)
        val_curve = self._to_minimized_curve(val_curve_raw)
        test_curve = self._to_minimized_curve(test_curve_raw)
        return EvalResult(
            val_score=float(val_curve[-1]),
            test_score=float(test_curve[-1]),
            learning_curve=[float(item) for item in val_curve],
            metadata={
                "dataset": self.dataset_name,
                "config_id": int(config_id),
                "val_metric_tag": self.val_metric_tag,
                "test_metric_tag": self.test_metric_tag,
            },
        )

    def meta_features(self) -> np.ndarray:
        return self._meta_features.copy()

    def _resolve_tag(self, tag: str, preferred: bool) -> str:
        first = self.data[self.dataset_name][
            sorted(self.data[self.dataset_name], key=int)[0]
        ]
        available = first.get("log", {}).keys() | first.get("results", {}).keys()
        if tag in available:
            return tag
        fallbacks = (
            [
                "Train/val_accuracy",
                "final_val_accuracy",
                "Train/val_cross_entropy",
                "Train/val_loss",
            ]
            if preferred
            else [
                "final_test_accuracy",
                "Train/test_result",
                "Train/test_accuracy",
                "final_test_cross_entropy",
                "Train/test_loss",
                "Train/val_accuracy",
                "final_val_accuracy",
            ]
        )
        for fallback in fallbacks:
            if fallback in available:
                return fallback
        raise ValueError(
            f"None of the requested LCBench tags are available. Found: {sorted(available)}"
        )

    def _query_curve(self, config_id: str, tag: str) -> np.ndarray:
        item = self.data[self.dataset_name][config_id]
        values = item.get("results", {}) | item.get("log", {})
        if tag not in values:
            raise ValueError(f"Tag {tag!r} not found for config {config_id}")
        value = values[tag]
        arr = np.asarray(value if isinstance(value, list) else [value], dtype=float)
        if arr.ndim != 1 or len(arr) == 0:
            raise ValueError(
                f"Tag {tag!r} for config {config_id} is not a non-empty curve"
            )
        return arr

    def _to_minimized_curve(self, curve: np.ndarray) -> np.ndarray:
        if self._score_from_accuracy:
            scale = 100.0 if float(np.nanmax(curve)) > 1.0 else 1.0
            return scale - curve
        return curve

    def _config_with_id(self, config_id: str) -> Config:
        raw_config = dict(self.data[self.dataset_name][config_id]["config"])
        raw_config["__config_id__"] = int(config_id)
        return raw_config

    def _build_search_space(self, configs: list[Config]) -> SearchSpace:
        parameters: list[Parameter] = []
        keys = [key for key in configs[0] if key != "__config_id__"]
        for key in keys:
            values = [config[key] for config in configs]
            if all(_is_number(value) for value in values):
                numeric = np.asarray(values, dtype=float)
                low = float(numeric.min())
                high = float(numeric.max())
                if np.allclose(numeric, np.round(numeric)):
                    parameters.append(Parameter(key, "int", low=low, high=high))
                else:
                    parameters.append(Parameter(key, "float", low=low, high=high))
            else:
                parameters.append(
                    Parameter(key, "categorical", choices=tuple(sorted(set(values))))
                )
        return SearchSpace(parameters)

    def _read_meta_features(self) -> np.ndarray:
        first = self.data[self.dataset_name][self.config_ids[0]]
        sources = [first.get("results", {}), first.get("config", {})]
        values = []
        for key in ("classes", "features", "instances"):
            raw = next((source[key] for source in sources if key in source), 0.0)
            values.append(float(np.log1p(float(raw))))
        return np.asarray(values, dtype=float)

    def _nearest_config_id(self, config: Config) -> int:
        vector = self.search_space.to_vector(config)
        distances = np.linalg.norm(self.candidate_vectors - vector, axis=1)
        return int(self.candidate_configs[int(np.argmin(distances))]["__config_id__"])


def _is_number(value: Any) -> bool:
    try:
        float(value)
    except (TypeError, ValueError):
        return False
    return True
