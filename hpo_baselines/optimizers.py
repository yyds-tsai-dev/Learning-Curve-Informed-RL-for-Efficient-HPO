from __future__ import annotations

from dataclasses import dataclass, field
from math import erf, pi, sqrt
from typing import Any, Protocol

import numpy as np

from .search_space import SearchSpace
from .tasks import EvalResult

np.seterr(over="ignore", invalid="ignore", divide="ignore")


class HPOTask(Protocol):
    name: str
    search_space: SearchSpace

    def evaluate(self, config: dict[str, Any], seed: int) -> EvalResult: ...


@dataclass
class EvaluationRecord:
    iteration: int
    config: dict[str, Any]
    val_score: float
    test_score: float
    learning_curve: list[float]
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass
class OptimizationTrace:
    method: str
    task: str
    seed: int
    evaluations: list[EvaluationRecord]

    @property
    def best_record(self) -> EvaluationRecord:
        return min(self.evaluations, key=lambda item: item.val_score)


class BaseOptimizer:
    name = "base"

    def optimize(self, task: HPOTask, budget: int, seed: int) -> OptimizationTrace:
        raise NotImplementedError


class RandomSearch(BaseOptimizer):
    name = "Random Search"

    def optimize(self, task: HPOTask, budget: int, seed: int) -> OptimizationTrace:
        rng = np.random.default_rng(seed)
        evaluations: list[EvaluationRecord] = []
        for iteration in range(budget):
            config = task.search_space.sample(rng)
            result = task.evaluate(config, seed=int(rng.integers(0, 2**31 - 1)))
            evaluations.append(_record(iteration, config, result))
        return OptimizationTrace(self.name, task.name, seed, evaluations)


class BayesianOptimization(BaseOptimizer):
    """Gaussian-process BO with Expected Improvement over sampled candidates."""

    name = "Bayesian Optimization"

    def __init__(
        self,
        initial_points: int = 5,
        candidate_pool_size: int = 512,
        length_scale: float = 0.35,
        noise: float = 1e-6,
    ) -> None:
        self.initial_points = initial_points
        self.candidate_pool_size = candidate_pool_size
        self.length_scale = length_scale
        self.noise = noise

    def optimize(self, task: HPOTask, budget: int, seed: int) -> OptimizationTrace:
        rng = np.random.default_rng(seed)
        configs: list[dict[str, Any]] = []
        scores: list[float] = []
        evaluations: list[EvaluationRecord] = []

        for iteration in range(budget):
            if iteration < min(self.initial_points, budget):
                config = task.search_space.sample(rng)
            else:
                candidates = task.search_space.sample_many(rng, self.candidate_pool_size)
                x_train = task.search_space.to_matrix(configs)
                y_train = np.asarray(scores, dtype=float)
                x_candidates = task.search_space.to_matrix(candidates)
                ei = self._expected_improvement(x_train, y_train, x_candidates)
                config = candidates[int(np.argmax(ei))]

            result = task.evaluate(config, seed=int(rng.integers(0, 2**31 - 1)))
            configs.append(config)
            scores.append(result.val_score)
            evaluations.append(_record(iteration, config, result))

        return OptimizationTrace(self.name, task.name, seed, evaluations)

    def _expected_improvement(
        self, x_train: np.ndarray, y_train: np.ndarray, x_candidates: np.ndarray
    ) -> np.ndarray:
        y_mean = float(y_train.mean())
        y_std = float(y_train.std() + 1e-8)
        y_scaled = (y_train - y_mean) / y_std

        k_xx = self._kernel(x_train, x_train)
        k_xx[np.diag_indices_from(k_xx)] += self.noise
        k_xs = self._kernel(x_train, x_candidates)
        k_ss_diag = np.ones(len(x_candidates))

        try:
            chol = np.linalg.cholesky(k_xx)
            alpha = np.linalg.solve(chol.T, np.linalg.solve(chol, y_scaled))
            pred_mean = k_xs.T @ alpha
            v = np.linalg.solve(chol, k_xs)
            pred_var = np.maximum(k_ss_diag - np.sum(v * v, axis=0), 1e-10)
        except np.linalg.LinAlgError:
            pred_mean = np.repeat(y_scaled.mean(), len(x_candidates))
            pred_var = np.repeat(y_scaled.var() + 1e-6, len(x_candidates))

        pred_std = np.sqrt(pred_var)
        best = float(y_scaled.min())
        z = (best - pred_mean) / pred_std
        phi = np.exp(-0.5 * z * z) / sqrt(2.0 * pi)
        cdf = 0.5 * (1.0 + np.vectorize(erf)(z / sqrt(2.0)))
        return (best - pred_mean) * cdf + pred_std * phi

    def _kernel(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
        diff = left[:, None, :] - right[None, :, :]
        dist2 = np.sum(diff * diff, axis=2)
        return np.exp(-0.5 * dist2 / (self.length_scale**2))


class HyperRLOptimizer(BaseOptimizer):
    """Small HyperRL-style baseline using approximate Q-learning.

    This is intentionally a toy proxy for Hyp-RL: it treats HPO as sequential
    decisions over a fixed candidate pool and updates a linear Q function from
    validation reward plus learning-curve trend features.
    """

    name = "HyperRL"

    def __init__(
        self,
        candidate_pool_size: int = 128,
        epsilon_start: float = 0.45,
        epsilon_end: float = 0.05,
        learning_rate: float = 0.08,
        gamma: float = 0.6,
    ) -> None:
        self.candidate_pool_size = candidate_pool_size
        self.epsilon_start = epsilon_start
        self.epsilon_end = epsilon_end
        self.learning_rate = learning_rate
        self.gamma = gamma

    def optimize(self, task: HPOTask, budget: int, seed: int) -> OptimizationTrace:
        rng = np.random.default_rng(seed)
        candidates = task.search_space.sample_many(rng, self.candidate_pool_size)
        action_features = task.search_space.to_matrix(candidates)
        state = np.zeros(4, dtype=float)
        theta = np.zeros(self._feature(action_features[0], state).shape[0], dtype=float)
        used: set[int] = set()
        evaluations: list[EvaluationRecord] = []

        for iteration in range(budget):
            epsilon = self._epsilon(iteration, max(budget - 1, 1))
            available = np.asarray([idx for idx in range(len(candidates)) if idx not in used])
            if len(available) == 0:
                break

            if rng.random() < epsilon:
                action_idx = int(rng.choice(available))
            else:
                q_values = np.asarray(
                    [theta @ self._feature(action_features[idx], state) for idx in available]
                )
                action_idx = int(available[int(np.argmax(q_values))])

            used.add(action_idx)
            feature = self._feature(action_features[action_idx], state)
            config = candidates[action_idx]
            result = task.evaluate(config, seed=int(rng.integers(0, 2**31 - 1)))
            reward = -result.val_score
            next_state = self._state_from_curve(result.learning_curve, iteration, budget)
            next_available = np.asarray([idx for idx in range(len(candidates)) if idx not in used])
            if len(next_available):
                next_q = max(
                    theta @ self._feature(action_features[idx], next_state)
                    for idx in next_available
                )
            else:
                next_q = 0.0
            td_error = reward + self.gamma * next_q - theta @ feature
            theta += self.learning_rate * td_error * feature
            state = next_state

            evaluations.append(
                _record(
                    iteration,
                    config,
                    result,
                    extra={"epsilon": float(epsilon), "reward": float(reward)},
                )
            )

        return OptimizationTrace(self.name, task.name, seed, evaluations)

    def _epsilon(self, iteration: int, denominator: int) -> float:
        frac = iteration / denominator
        return self.epsilon_start + frac * (self.epsilon_end - self.epsilon_start)

    @staticmethod
    def _state_from_curve(curve: list[float], iteration: int, budget: int) -> np.ndarray:
        values = np.asarray(curve, dtype=float)
        if len(values) < 3:
            return np.asarray([iteration / budget, 0.0, 0.0, 0.0], dtype=float)
        tail = values[-min(8, len(values)) :]
        first_derivative = np.diff(tail)
        second_derivative = np.diff(first_derivative) if len(first_derivative) > 1 else np.zeros(1)
        total_drop = values[0] - values[-1]
        return np.asarray(
            [
                iteration / max(budget, 1),
                float(np.clip(-first_derivative.mean(), -1.0, 1.0)),
                float(np.clip(-second_derivative.mean(), -1.0, 1.0)),
                float(np.clip(total_drop, -1.0, 1.0)),
            ],
            dtype=float,
        )

    @staticmethod
    def _feature(action: np.ndarray, state: np.ndarray) -> np.ndarray:
        return np.concatenate(([1.0], action, state, np.outer(action, state).ravel()))


def _record(
    iteration: int,
    config: dict[str, Any],
    result: EvalResult,
    extra: dict[str, Any] | None = None,
) -> EvaluationRecord:
    return EvaluationRecord(
        iteration=iteration,
        config=config,
        val_score=result.val_score,
        test_score=result.test_score,
        learning_curve=result.learning_curve,
        extra=extra or {},
    )
