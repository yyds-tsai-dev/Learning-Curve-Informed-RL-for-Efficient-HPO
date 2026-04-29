from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

import numpy as np


@dataclass(frozen=True)
class Parameter:
    name: str
    kind: str
    low: float | None = None
    high: float | None = None
    choices: tuple[Any, ...] | None = None
    log: bool = False

    def sample(self, rng: np.random.Generator) -> Any:
        if self.kind == "float":
            assert self.low is not None and self.high is not None
            if self.log:
                return float(np.exp(rng.uniform(np.log(self.low), np.log(self.high))))
            return float(rng.uniform(self.low, self.high))
        if self.kind == "int":
            assert self.low is not None and self.high is not None
            if self.log:
                value = np.exp(rng.uniform(np.log(self.low), np.log(self.high)))
                return int(np.clip(round(value), self.low, self.high))
            return int(rng.integers(int(self.low), int(self.high) + 1))
        if self.kind == "categorical":
            assert self.choices is not None
            return self.choices[int(rng.integers(0, len(self.choices)))]
        raise ValueError(f"Unsupported parameter kind: {self.kind}")

    def to_unit(self, value: Any) -> list[float]:
        if self.kind in {"float", "int"}:
            assert self.low is not None and self.high is not None
            raw_value = float(value)
            low = float(self.low)
            high = float(self.high)
            if self.log:
                raw_value = np.log(max(raw_value, 1e-300))
                low = float(np.log(low))
                high = float(np.log(high))
            if high == low:
                return [0.0]
            return [float(np.clip((raw_value - low) / (high - low), 0.0, 1.0))]
        if self.kind == "categorical":
            assert self.choices is not None
            return [1.0 if choice == value else 0.0 for choice in self.choices]
        raise ValueError(f"Unsupported parameter kind: {self.kind}")


class SearchSpace:
    def __init__(self, parameters: Iterable[Parameter]):
        self.parameters = tuple(parameters)

    def sample(self, rng: np.random.Generator) -> dict[str, Any]:
        return {parameter.name: parameter.sample(rng) for parameter in self.parameters}

    def sample_many(self, rng: np.random.Generator, n: int) -> list[dict[str, Any]]:
        return [self.sample(rng) for _ in range(n)]

    def to_vector(self, config: dict[str, Any]) -> np.ndarray:
        values: list[float] = []
        for parameter in self.parameters:
            values.extend(parameter.to_unit(config[parameter.name]))
        return np.asarray(values, dtype=float)

    def to_matrix(self, configs: list[dict[str, Any]]) -> np.ndarray:
        return np.vstack([self.to_vector(config) for config in configs])
