from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


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
