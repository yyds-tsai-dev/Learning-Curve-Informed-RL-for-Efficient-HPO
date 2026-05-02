from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from math import erf, pi, sqrt
from typing import Any, Protocol

import numpy as np
import torch
from torch import nn, optim

from .search_space import Config, SearchSpace
from .tasks import EvalResult

np.seterr(over="ignore", invalid="ignore", divide="ignore")

type CandidateConfigs = list[Config]


class HPOTask(Protocol):
    name: str
    search_space: SearchSpace

    def evaluate(self, config: Config, seed: int) -> EvalResult: ...


@dataclass(slots=True)
class EvaluationRecord:
    iteration: int
    config: Config
    val_score: float
    test_score: float
    learning_curve: list[float]
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
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
        candidates = _candidate_configs(task)
        used: set[int] = set()
        for iteration in range(budget):
            if candidates is None:
                config = task.search_space.sample(rng)
            else:
                available = [idx for idx in range(len(candidates)) if idx not in used]
                if not available:
                    break
                idx = int(rng.choice(available))
                used.add(idx)
                config = candidates[idx]
            result = task.evaluate(config, seed=int(rng.integers(0, 2**31 - 1)))
            evaluations.append(_record(iteration, config, result))
        return OptimizationTrace(self.name, task.name, seed, evaluations)


@dataclass(slots=True)
class BayesianOptimization(BaseOptimizer):
    """Gaussian-process BO with Expected Improvement.

    On tabular benchmarks such as LCBench, EI is computed over the finite
    configuration table. On open search spaces, it is computed over a sampled
    candidate pool.
    """

    name = "Bayesian Optimization"
    initial_points: int = 5
    candidate_pool_size: int = 512
    max_observations: int = 128
    length_scale: float = 0.35
    noise: float = 1e-6

    def optimize(self, task: HPOTask, budget: int, seed: int) -> OptimizationTrace:
        rng = np.random.default_rng(seed)
        configs: list[Config] = []
        scores: list[float] = []
        evaluations: list[EvaluationRecord] = []
        finite_candidates = _candidate_configs(task)
        used: set[int] = set()

        for iteration in range(budget):
            if finite_candidates is not None:
                available = [
                    idx for idx in range(len(finite_candidates)) if idx not in used
                ]
                if not available:
                    break
                if iteration < min(self.initial_points, budget):
                    idx = int(rng.choice(available))
                else:
                    train_configs, train_scores = self._surrogate_subset(
                        configs, scores
                    )
                    x_train = task.search_space.to_matrix(train_configs)
                    y_train = np.asarray(train_scores, dtype=float)
                    candidate_idx = self._candidate_subset(available, rng)
                    x_candidates = task.search_space.to_matrix(
                        [finite_candidates[idx] for idx in candidate_idx]
                    )
                    ei = self._expected_improvement(x_train, y_train, x_candidates)
                    idx = candidate_idx[int(np.argmax(ei))]
                used.add(idx)
                config = finite_candidates[idx]
            elif iteration < min(self.initial_points, budget):
                config = task.search_space.sample(rng)
            else:
                candidates = task.search_space.sample_many(
                    rng, self.candidate_pool_size
                )
                train_configs, train_scores = self._surrogate_subset(configs, scores)
                x_train = task.search_space.to_matrix(train_configs)
                y_train = np.asarray(train_scores, dtype=float)
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

    def _surrogate_subset(
        self, configs: list[Config], scores: list[float]
    ) -> tuple[list[Config], list[float]]:
        if len(configs) <= self.max_observations:
            return configs, scores
        order = np.argsort(np.asarray(scores, dtype=float))
        n_best = self.max_observations // 2
        best_idx = list(order[:n_best])
        recent_idx = list(
            range(max(0, len(configs) - (self.max_observations - n_best)), len(configs))
        )
        selected = list(dict.fromkeys([*best_idx, *recent_idx]))
        return [configs[idx] for idx in selected], [scores[idx] for idx in selected]

    def _candidate_subset(
        self, available: list[int], rng: np.random.Generator
    ) -> list[int]:
        if len(available) <= self.candidate_pool_size:
            return available
        return [
            int(idx)
            for idx in rng.choice(
                available, size=self.candidate_pool_size, replace=False
            )
        ]


@dataclass(slots=True)
class HyperRLOptimizer(BaseOptimizer):
    """Hyp-RL-style DQN with the paper/repo state.

    The original implementation uses a DQN controller over a finite
    hyperparameter grid, replay buffer, epsilon-greedy exploration, and a target
    network. This implementation keeps the padded history state representation
    and supports either an MLP or an LSTM Q-network.
    """

    name = "HyperRL-DQN"
    hidden_sizes: tuple[int, ...] = (128, 128)
    learning_rate: float = 1e-3
    gamma: float = 0.99
    replay_size: int = 1024
    batch_size: int = 32
    learning_starts: int = 4
    target_update_freq: int = 10
    epsilon_start: float = 1.0
    epsilon_end: float = 0.05
    reward_mode: str = "improvement"
    network_type: str = "lstm"

    def optimize(self, task: HPOTask, budget: int, seed: int) -> OptimizationTrace:
        controller = _DQNController(
            method_name=self.name,
            include_curve_features=False,
            hidden_sizes=self.hidden_sizes,
            learning_rate=self.learning_rate,
            gamma=self.gamma,
            replay_size=self.replay_size,
            batch_size=self.batch_size,
            learning_starts=self.learning_starts,
            target_update_freq=self.target_update_freq,
            epsilon_start=self.epsilon_start,
            epsilon_end=self.epsilon_end,
            reward_mode=self.reward_mode,
            network_type=self.network_type,
        )
        return controller.optimize(task, budget, seed)


class LearningCurveDQNOptimizer(HyperRLOptimizer):
    """Our method: Hyp-RL plus learning-curve value and derivative features."""

    name = "OurMethod-LC-DQN"

    def optimize(self, task: HPOTask, budget: int, seed: int) -> OptimizationTrace:
        controller = _DQNController(
            method_name=self.name,
            include_curve_features=True,
            hidden_sizes=self.hidden_sizes,
            learning_rate=self.learning_rate,
            gamma=self.gamma,
            replay_size=self.replay_size,
            batch_size=self.batch_size,
            learning_starts=self.learning_starts,
            target_update_freq=self.target_update_freq,
            epsilon_start=self.epsilon_start,
            epsilon_end=self.epsilon_end,
            reward_mode=self.reward_mode,
            network_type=self.network_type,
        )
        return controller.optimize(task, budget, seed)


@dataclass(slots=True)
class _Transition:
    state: np.ndarray
    action: int
    reward: float
    next_state: np.ndarray
    done: bool


class _ReplayBuffer:
    def __init__(self, capacity: int) -> None:
        self.items: deque[_Transition] = deque(maxlen=capacity)

    def add(self, transition: _Transition) -> None:
        self.items.append(transition)

    def sample(self, rng: np.random.Generator, batch_size: int) -> list[_Transition]:
        idx = rng.choice(len(self.items), size=batch_size, replace=False)
        return [self.items[int(item)] for item in idx]

    def __len__(self) -> int:
        return len(self.items)


@dataclass(slots=True)
class _DQNController:
    method_name: str
    include_curve_features: bool
    hidden_sizes: tuple[int, ...]
    learning_rate: float
    gamma: float
    replay_size: int
    batch_size: int
    learning_starts: int
    target_update_freq: int
    epsilon_start: float
    epsilon_end: float
    reward_mode: str
    network_type: str

    def __post_init__(self) -> None:
        if self.reward_mode not in {"raw", "improvement"}:
            raise ValueError("reward_mode must be 'raw' or 'improvement'")
        if self.network_type not in {"mlp", "lstm"}:
            raise ValueError("network_type must be 'mlp' or 'lstm'")

    def optimize(self, task: HPOTask, budget: int, seed: int) -> OptimizationTrace:
        rng = np.random.default_rng(seed)
        torch.manual_seed(seed)

        candidates = _candidate_configs(task)
        if candidates is None:
            candidates = task.search_space.sample_many(rng, max(budget * 8, 64))
        action_vectors = task.search_space.to_matrix(candidates)
        meta = _meta_features(task)
        row_dim = (
            action_vectors.shape[1]
            + 1
            + len(meta)
            + (5 if self.include_curve_features else 0)
        )
        state_dim = budget * row_dim
        n_actions = len(candidates)

        online = self._build_q_network(state_dim, row_dim, budget, n_actions)
        target = self._build_q_network(state_dim, row_dim, budget, n_actions)
        target.load_state_dict(online.state_dict())
        optimizer = optim.Adam(online.parameters(), lr=self.learning_rate)
        replay = _ReplayBuffer(self.replay_size)

        history = np.zeros((budget, row_dim), dtype=np.float32)
        used: set[int] = set()
        evaluations: list[EvaluationRecord] = []
        previous_raw_reward = 0.0

        for iteration in range(budget):
            state = history.reshape(-1).copy()
            available = [idx for idx in range(n_actions) if idx not in used]
            if not available:
                break
            epsilon = _linear_epsilon(
                iteration,
                max(budget - 1, 1),
                start=self.epsilon_start,
                end=self.epsilon_end,
            )
            action_idx = self._select_action(online, state, available, rng, epsilon)
            used.add(action_idx)

            config = candidates[action_idx]
            result = task.evaluate(config, seed=int(rng.integers(0, 2**31 - 1)))
            raw_reward = -float(result.val_score)
            reward = (
                max(0.0, raw_reward - previous_raw_reward)
                if self.reward_mode == "improvement"
                else raw_reward
            )
            previous_raw_reward = raw_reward

            history[iteration] = self._history_row(
                action_vectors[action_idx],
                raw_reward,
                meta,
                result.learning_curve,
            )
            next_state = history.reshape(-1).copy()
            done = iteration == budget - 1 or len(used) == n_actions
            replay.add(_Transition(state, action_idx, reward, next_state, done))

            loss = None
            if len(replay) >= max(self.learning_starts, self.batch_size):
                loss = self._train_step(online, target, optimizer, replay, rng)
            if (iteration + 1) % self.target_update_freq == 0:
                target.load_state_dict(online.state_dict())

            evaluations.append(
                _record(
                    iteration,
                    config,
                    result,
                    extra={
                        "action_idx": int(action_idx),
                        "epsilon": float(epsilon),
                        "raw_reward": raw_reward,
                        "dqn_reward": float(reward),
                        "loss": None if loss is None else float(loss),
                    },
                )
            )

        return OptimizationTrace(self.method_name, task.name, seed, evaluations)

    def _build_q_network(
        self, state_dim: int, row_dim: int, seq_len: int, n_actions: int
    ) -> nn.Module:
        if self.network_type == "lstm":
            return _LSTMQNetwork(
                row_dim=row_dim,
                seq_len=seq_len,
                output_dim=n_actions,
                hidden_sizes=self.hidden_sizes,
            )
        return _MLPQNetwork(state_dim, n_actions, self.hidden_sizes)

    def _select_action(
        self,
        network: Any,
        state: np.ndarray,
        available: list[int],
        rng: np.random.Generator,
        epsilon: float,
    ) -> int:
        if rng.random() < epsilon:
            return int(rng.choice(available))
        with torch.no_grad():
            tensor = torch.as_tensor(state, dtype=torch.float32).unsqueeze(0)
            q_values = network(tensor).squeeze(0).detach().cpu().numpy()
        masked = q_values[available]
        return int(available[int(np.argmax(masked))])

    def _history_row(
        self,
        action_vector: np.ndarray,
        reward: float,
        meta: np.ndarray,
        curve: list[float],
    ) -> np.ndarray:
        pieces = [
            action_vector.astype(np.float32),
            np.asarray([reward], dtype=np.float32),
            meta,
        ]
        if self.include_curve_features:
            pieces.append(_curve_features(curve))
        return np.concatenate(pieces).astype(np.float32)

    def _train_step(
        self,
        online: Any,
        target: Any,
        optimizer: Any,
        replay: _ReplayBuffer,
        rng: np.random.Generator,
    ) -> float:
        batch = replay.sample(rng, self.batch_size)
        states = torch.as_tensor(
            np.vstack([item.state for item in batch]), dtype=torch.float32
        )
        actions = torch.as_tensor([item.action for item in batch], dtype=torch.int64)
        rewards = torch.as_tensor([item.reward for item in batch], dtype=torch.float32)
        next_states = torch.as_tensor(
            np.vstack([item.next_state for item in batch]), dtype=torch.float32
        )
        dones = torch.as_tensor([item.done for item in batch], dtype=torch.float32)

        q_selected = online(states).gather(1, actions.view(-1, 1)).squeeze(1)
        with torch.no_grad():
            next_q = target(next_states).max(dim=1).values
            targets = rewards + self.gamma * next_q * (1.0 - dones)
        loss = nn.functional.mse_loss(q_selected, targets)
        optimizer.zero_grad()
        loss.backward()
        nn.utils.clip_grad_norm_(online.parameters(), 10.0)
        optimizer.step()
        return float(loss.detach().cpu().item())


class _MLPQNetwork:
    def __new__(
        cls, input_dim: int, output_dim: int, hidden_sizes: tuple[int, ...]
    ) -> nn.Sequential:
        layers = []
        current = input_dim
        for hidden in hidden_sizes:
            layers.append(nn.Linear(current, hidden))
            layers.append(nn.ReLU())
            current = hidden
        layers.append(nn.Linear(current, output_dim))
        return nn.Sequential(*layers)


class _LSTMQNetwork(nn.Module):
    def __init__(
        self,
        row_dim: int,
        seq_len: int,
        output_dim: int,
        hidden_sizes: tuple[int, ...],
    ) -> None:
        super().__init__()
        lstm_hidden = hidden_sizes[0] if hidden_sizes else 128
        self.row_dim = row_dim
        self.seq_len = seq_len
        self.lstm = nn.LSTM(
            input_size=row_dim,
            hidden_size=lstm_hidden,
            batch_first=True,
        )

        layers: list[nn.Module] = []
        current = lstm_hidden
        for hidden in hidden_sizes[1:]:
            layers.append(nn.Linear(current, hidden))
            layers.append(nn.ReLU())
            current = hidden
        layers.append(nn.Linear(current, output_dim))
        self.head = nn.Sequential(*layers)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        if inputs.ndim == 2:
            x = inputs.reshape(inputs.shape[0], self.seq_len, self.row_dim)
        elif inputs.ndim == 3:
            x = inputs
        else:
            raise ValueError(
                "inputs must have shape [batch, state_dim] or [batch, seq, row]"
            )

        # Infer effective sequence lengths from non-zero rows to avoid learning
        # from trailing padding when history is shorter than the budget.
        row_energy = x.abs().sum(dim=2)
        lengths = torch.clamp((row_energy > 0).sum(dim=1), min=1).to(torch.int64)
        packed = nn.utils.rnn.pack_padded_sequence(
            x,
            lengths.cpu(),
            batch_first=True,
            enforce_sorted=False,
        )
        _, (hidden, _) = self.lstm(packed)
        features = hidden[-1]
        return self.head(features)


def _candidate_configs(task: HPOTask) -> CandidateConfigs | None:
    candidates = getattr(task, "candidate_configs", None)
    if candidates is None:
        return None
    return [dict(config) for config in candidates]


def _meta_features(task: HPOTask) -> np.ndarray:
    if hasattr(task, "meta_features"):
        values = np.asarray(task.meta_features(), dtype=np.float32)
    else:
        values = np.zeros(0, dtype=np.float32)
    if len(values) == 0:
        return values
    scale = np.linalg.norm(values)
    return values / (scale + 1e-8)


def _curve_features(curve: list[float]) -> np.ndarray:
    values = np.asarray(curve, dtype=float)
    if len(values) == 0:
        return np.zeros(5, dtype=np.float32)
    tail = values[-min(8, len(values)) :]
    first = np.diff(tail)
    second = np.diff(first) if len(first) > 1 else np.zeros(1)
    features = np.asarray(
        [
            values[-1],
            float(np.min(values)),
            float(first.mean()) if len(first) else 0.0,
            float(second.mean()) if len(second) else 0.0,
            values[0] - values[-1],
        ],
        dtype=np.float32,
    )
    return np.clip(features, -1e3, 1e3)


def _linear_epsilon(
    iteration: int, denominator: int, start: float, end: float
) -> float:
    frac = iteration / denominator
    return float(start + frac * (end - start))


def _record(
    iteration: int,
    config: Config,
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
