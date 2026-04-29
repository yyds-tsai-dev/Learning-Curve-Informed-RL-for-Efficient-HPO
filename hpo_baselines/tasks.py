from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from .search_space import Parameter, SearchSpace

np.seterr(over="ignore", invalid="ignore", divide="ignore")


@dataclass
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

    def evaluate(self, config: dict[str, Any], seed: int) -> EvalResult:
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
