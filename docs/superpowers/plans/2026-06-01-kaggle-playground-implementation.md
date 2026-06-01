# Kaggle Playground Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Kaggle Playground regression benchmark that exposes 15 fixed tasks as LCBench-compatible cached HPO tables, then run all-methods and LC-DQN task-count experiments.

**Architecture:** Add a focused Kaggle benchmark module that owns manifest loading, raw CSV preprocessing, cache generation, cache loading, task adaptation, and normalized simple regret metadata. Keep optimizers mostly unchanged, but extend the cross-dataset path so meta-training tasks and evaluation tasks can differ. Add scripts as thin entry points over the new module and existing evaluator APIs.

**Tech Stack:** Python 3.12, NumPy, PyTorch, matplotlib, tqdm, pytest for tests, Kaggle CLI for optional data download, standard-library CSV/JSON/pathlib for data plumbing.

---

## File Structure

- Create: `data/kaggle_playground/manifest.json`
  - Fixed 15-task whitelist, target columns, competition slugs, metric direction, and nested order.
- Create: `hpo_baselines/kaggle_playground.py`
  - Manifest dataclasses, preprocessing helpers, MLP cache builder, cache loader, `KaggleRegressionTask`, and normalized-regret helpers.
- Modify: `hpo_baselines/__init__.py`
  - Export `KaggleRegressionTask` and helper loaders.
- Modify: `hpo_baselines/evaluator.py`
  - Add normalized simple regret support and allow cross-dataset methods to train on one task list while evaluating on another.
- Modify: `hpo_baselines/optimizers.py`
  - Add optional evaluation task list to cross-dataset Hyp-RL/LC-DQN.
- Create: `scripts/download_kaggle_playground.py`
  - Thin Kaggle CLI wrapper for manifest tasks.
- Create: `scripts/build_kaggle_playground_cache.py`
  - Build cached HPO tables from downloaded raw CSVs.
- Create: `scripts/run_kaggle_playground.py`
  - Run all-methods benchmark and LC-DQN task-count sweep.
- Create: `tests/test_kaggle_playground.py`
  - Unit tests for manifest parsing, preprocessing, meta-features, cache adapter, normalized regret, and train/eval task separation.
- Modify: `requirements.txt`
  - Add `pytest>=8.0` for local verification.
- Modify: `README.md`
  - Document Kaggle benchmark commands and expected data/cache paths.

---

### Task 1: Manifest And Test Harness

**Files:**
- Create: `data/kaggle_playground/manifest.json`
- Create: `tests/test_kaggle_playground.py`
- Modify: `requirements.txt`

- [ ] **Step 1: Add pytest to requirements**

Add this exact line to `requirements.txt`:

```text
pytest>=8.0
```

- [ ] **Step 2: Create the fixed task manifest**

Create `data/kaggle_playground/manifest.json`:

```json
{
  "snapshot_date": "2026-06-01",
  "metric": {
    "name": "RMSE",
    "direction": "minimize",
    "reference_worst_percentile": 90
  },
  "cache": {
    "configs_per_task": 256,
    "epochs_per_config": 25,
    "seeds_per_config": 1,
    "split": {
      "train": 0.8,
      "validation": 0.1,
      "test": 0.1,
      "seed": 20260601
    }
  },
  "nested_order": [
    "playground-series-s3e1",
    "playground-series-s4e4",
    "playground-series-s4e12",
    "playground-series-s3e14",
    "playground-series-s4e9",
    "playground-series-s3e9",
    "playground-series-s3e16",
    "playground-series-s5e5",
    "playground-series-s3e11",
    "playground-series-s5e4",
    "playground-series-s3e6",
    "playground-series-s3e8",
    "playground-series-s3e25",
    "playground-series-s4e5",
    "playground-series-s5e2"
  ],
  "tasks": [
    {"slug": "playground-series-s3e1", "episode": "S3E1", "name": "California Housing", "target_column": "MedHouseVal"},
    {"slug": "playground-series-s3e6", "episode": "S3E6", "name": "Paris Housing Price", "target_column": "price"},
    {"slug": "playground-series-s3e8", "episode": "S3E8", "name": "Gemstone Price", "target_column": "price"},
    {"slug": "playground-series-s3e9", "episode": "S3E9", "name": "Concrete Strength", "target_column": "Strength"},
    {"slug": "playground-series-s3e11", "episode": "S3E11", "name": "Media Campaign Cost", "target_column": "cost"},
    {"slug": "playground-series-s3e14", "episode": "S3E14", "name": "Wild Blueberry Yield", "target_column": "yield"},
    {"slug": "playground-series-s3e16", "episode": "S3E16", "name": "Crab Age", "target_column": "Age"},
    {"slug": "playground-series-s3e25", "episode": "S3E25", "name": "Mohs Hardness", "target_column": "Hardness"},
    {"slug": "playground-series-s4e4", "episode": "S4E4", "name": "Abalone", "target_column": "Rings"},
    {"slug": "playground-series-s4e5", "episode": "S4E5", "name": "Flood Prediction", "target_column": "FloodProbability"},
    {"slug": "playground-series-s4e9", "episode": "S4E9", "name": "Used Car Prices", "target_column": "price"},
    {"slug": "playground-series-s4e12", "episode": "S4E12", "name": "Insurance", "target_column": "Premium Amount"},
    {"slug": "playground-series-s5e2", "episode": "S5E2", "name": "Backpack Prediction", "target_column": "Price"},
    {"slug": "playground-series-s5e4", "episode": "S5E4", "name": "Podcast Listening Time", "target_column": "Listening_Time_minutes"},
    {"slug": "playground-series-s5e5", "episode": "S5E5", "name": "Calorie Expenditure", "target_column": "Calories"}
  ]
}
```

- [ ] **Step 3: Write failing manifest tests**

Create `tests/test_kaggle_playground.py` with:

```python
from pathlib import Path

from hpo_baselines.kaggle_playground import load_manifest, nested_task_slugs


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT_ROOT / "data" / "kaggle_playground" / "manifest.json"


def test_manifest_has_fixed_15_tasks():
    manifest = load_manifest(MANIFEST)

    assert len(manifest.tasks) == 15
    assert manifest.tasks[0].slug == "playground-series-s3e1"
    assert manifest.tasks[-1].slug == "playground-series-s5e5"
    assert manifest.by_slug["playground-series-s4e12"].target_column == "Premium Amount"


def test_nested_task_slugs_are_prefixes():
    manifest = load_manifest(MANIFEST)

    one = nested_task_slugs(manifest, 1)
    five = nested_task_slugs(manifest, 5)
    ten = nested_task_slugs(manifest, 10)
    fifteen = nested_task_slugs(manifest, 15)

    assert one == ["playground-series-s3e1"]
    assert one == five[:1]
    assert five == ten[:5]
    assert ten == fifteen[:10]
    assert len(fifteen) == 15
```

- [ ] **Step 4: Run manifest tests and verify they fail**

Run:

```bash
uv pip install -r requirements.txt
uv run pytest tests/test_kaggle_playground.py::test_manifest_has_fixed_15_tasks -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'hpo_baselines.kaggle_playground'`.

- [ ] **Step 5: Implement manifest loading**

Create the first section of `hpo_baselines/kaggle_playground.py`:

```python
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


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
    slugs = [task.slug for task in manifest.tasks]
    if len(slugs) != 15:
        raise ValueError(f"Expected 15 Kaggle tasks, found {len(slugs)}")
    if len(set(slugs)) != len(slugs):
        raise ValueError("Kaggle task slugs must be unique")
    if sorted(manifest.nested_order) != sorted(slugs):
        raise ValueError("nested_order must contain exactly the task slugs")
    split_total = (
        manifest.cache.split_train
        + manifest.cache.split_validation
        + manifest.cache.split_test
    )
    if abs(split_total - 1.0) > 1e-8:
        raise ValueError(f"Split fractions must sum to 1.0, got {split_total}")
```

- [ ] **Step 6: Run manifest tests and verify they pass**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_manifest_has_fixed_15_tasks tests/test_kaggle_playground.py::test_nested_task_slugs_are_prefixes -v
```

Expected: both tests PASS.

- [ ] **Step 7: Commit manifest slice**

Run:

```bash
git add requirements.txt data/kaggle_playground/manifest.json hpo_baselines/kaggle_playground.py tests/test_kaggle_playground.py
git commit -m "feat: add kaggle playground manifest"
```

---

### Task 2: Preprocessing And Meta-Features

**Files:**
- Modify: `hpo_baselines/kaggle_playground.py`
- Modify: `tests/test_kaggle_playground.py`

- [ ] **Step 1: Add failing preprocessing and meta-feature tests**

Append to `tests/test_kaggle_playground.py`:

```python
import csv

import numpy as np

from hpo_baselines.kaggle_playground import prepare_tabular_regression_data


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def test_prepare_tabular_regression_data_splits_preprocesses_and_meta_features(tmp_path):
    csv_path = tmp_path / "train.csv"
    _write_csv(
        csv_path,
        [
            {"id": 1, "num": 1.0, "cat": "a", "target": 10.0},
            {"id": 2, "num": "", "cat": "b", "target": 12.0},
            {"id": 3, "num": 3.0, "cat": "a", "target": 14.0},
            {"id": 4, "num": 4.0, "cat": "", "target": 16.0},
            {"id": 5, "num": 5.0, "cat": "c", "target": 18.0},
            {"id": 6, "num": 6.0, "cat": "b", "target": 20.0},
            {"id": 7, "num": 7.0, "cat": "a", "target": 22.0},
            {"id": 8, "num": 8.0, "cat": "c", "target": 24.0},
            {"id": 9, "num": 9.0, "cat": "b", "target": 26.0},
            {"id": 10, "num": 10.0, "cat": "a", "target": 28.0},
        ],
    )

    prepared = prepare_tabular_regression_data(
        csv_path=csv_path,
        target_column="target",
        split_seed=123,
        split=(0.8, 0.1, 0.1),
    )

    assert prepared.x_train.shape[0] == 8
    assert prepared.x_val.shape[0] == 1
    assert prepared.x_test.shape[0] == 1
    assert prepared.x_train.shape[1] == prepared.x_val.shape[1]
    assert np.all(np.isfinite(prepared.x_train))
    assert np.all(np.isfinite(prepared.y_train))
    assert prepared.meta_features.shape == (8,)
    assert prepared.meta_features[0] == np.log1p(8)
    assert prepared.meta_features[1] == np.log1p(2)
```

- [ ] **Step 2: Run preprocessing test and verify it fails**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_prepare_tabular_regression_data_splits_preprocesses_and_meta_features -v
```

Expected: FAIL with `ImportError` or `AttributeError` for `prepare_tabular_regression_data`.

- [ ] **Step 3: Implement CSV parsing, preprocessing, and meta-features**

Append this code to `hpo_baselines/kaggle_playground.py`:

```python
import csv
import math
from collections import Counter

import numpy as np


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
        key
        for key in rows[0]
        if key != target_column and key.lower() != "id"
    ]
    n_raw_features = len(feature_columns)
    numeric_columns = [
        key for key in feature_columns if _is_numeric_column(rows, key)
    ]
    categorical_columns = [
        key for key in feature_columns if key not in numeric_columns
    ]
    missing_count = sum(
        1
        for row in rows
        for key in feature_columns
        if _is_missing(row.get(key, ""))
    )
    total_cells = max(len(rows) * max(len(feature_columns), 1), 1)

    train_idx, val_idx, test_idx = _split_indices(len(rows), split_seed, split)
    numeric_stats = _numeric_stats(rows, train_idx, numeric_columns)
    categorical_stats = _categorical_stats(rows, train_idx, categorical_columns)
    encoded, encoded_names = _encode_features(
        rows, feature_columns, numeric_columns, categorical_columns, numeric_stats, categorical_stats
    )
    y = np.asarray([float(row[target_column]) for row in rows], dtype=np.float32)
    y_mean = float(y[train_idx].mean())
    y_std = float(y[train_idx].std() + 1e-8)
    y_scaled = ((y - y_mean) / y_std).astype(np.float32)

    n_train_rows = len(train_idx)
    meta = np.asarray(
        [
            math.log1p(n_train_rows),
            math.log1p(n_raw_features),
            math.log1p(len(numeric_columns)),
            math.log1p(len(categorical_columns)),
            math.log1p(encoded.shape[1]),
            missing_count / total_cells,
            len(categorical_columns) / max(n_raw_features, 1),
            math.log1p(float(y[train_idx].std())),
        ],
        dtype=np.float32,
    )
    return PreparedRegressionData(
        x_train=encoded[train_idx],
        y_train=y_scaled[train_idx],
        x_val=encoded[val_idx],
        y_val=y_scaled[val_idx],
        x_test=encoded[test_idx],
        y_test=y_scaled[test_idx],
        y_mean=y_mean,
        y_std=y_std,
        meta_features=meta,
        feature_names=tuple(encoded_names),
    )


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"{path} has no rows")
    return rows


def _is_missing(value: object) -> bool:
    return value is None or str(value).strip() == ""


def _is_number(value: object) -> bool:
    if _is_missing(value):
        return False
    try:
        float(value)
    except ValueError:
        return False
    return True


def _is_numeric_column(rows: list[dict[str, str]], column: str) -> bool:
    values = [row[column] for row in rows if not _is_missing(row[column])]
    return bool(values) and all(_is_number(value) for value in values)


def _split_indices(
    n_rows: int, seed: int, split: tuple[float, float, float]
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if n_rows < 10:
        raise ValueError("Need at least 10 rows to create 80/10/10 splits")
    rng = np.random.default_rng(seed)
    indices = rng.permutation(n_rows)
    n_train = int(round(n_rows * split[0]))
    n_val = int(round(n_rows * split[1]))
    n_test = n_rows - n_train - n_val
    if min(n_train, n_val, n_test) <= 0:
        raise ValueError("Split produced an empty partition")
    return indices[:n_train], indices[n_train : n_train + n_val], indices[n_train + n_val :]


def _numeric_stats(
    rows: list[dict[str, str]], train_idx: np.ndarray, columns: list[str]
) -> dict[str, tuple[float, float]]:
    stats = {}
    for column in columns:
        values = np.asarray(
            [
                float(rows[int(idx)][column])
                for idx in train_idx
                if not _is_missing(rows[int(idx)][column])
            ],
            dtype=np.float32,
        )
        median = float(np.median(values)) if len(values) else 0.0
        filled = np.asarray(
            [
                float(rows[int(idx)][column]) if not _is_missing(rows[int(idx)][column]) else median
                for idx in train_idx
            ],
            dtype=np.float32,
        )
        stats[column] = (median, float(filled.mean()), float(filled.std() + 1e-8))
    return stats


def _categorical_stats(
    rows: list[dict[str, str]], train_idx: np.ndarray, columns: list[str]
) -> dict[str, tuple[str, tuple[str, ...]]]:
    stats = {}
    for column in columns:
        values = [
            str(rows[int(idx)][column])
            for idx in train_idx
            if not _is_missing(rows[int(idx)][column])
        ]
        mode = Counter(values).most_common(1)[0][0] if values else "__missing__"
        categories = tuple(sorted(set(values + [mode])))
        stats[column] = (mode, categories)
    return stats


def _encode_features(
    rows: list[dict[str, str]],
    feature_columns: list[str],
    numeric_columns: list[str],
    categorical_columns: list[str],
    numeric_stats: dict[str, tuple[float, float, float]],
    categorical_stats: dict[str, tuple[str, tuple[str, ...]]],
) -> tuple[np.ndarray, list[str]]:
    encoded_rows = []
    encoded_names = []
    for column in numeric_columns:
        encoded_names.append(column)
    for column in categorical_columns:
        for category in categorical_stats[column][1]:
            encoded_names.append(f"{column}={category}")

    for row in rows:
        values = []
        for column in numeric_columns:
            median, mean, std = numeric_stats[column]
            raw = median if _is_missing(row[column]) else float(row[column])
            values.append((raw - mean) / std)
        for column in categorical_columns:
            mode, categories = categorical_stats[column]
            raw = mode if _is_missing(row[column]) else str(row[column])
            values.extend(1.0 if raw == category else 0.0 for category in categories)
        encoded_rows.append(values)
    return np.asarray(encoded_rows, dtype=np.float32), encoded_names
```

- [ ] **Step 4: Run preprocessing tests and verify they pass**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_prepare_tabular_regression_data_splits_preprocesses_and_meta_features -v
```

Expected: PASS.

- [ ] **Step 5: Commit preprocessing slice**

Run:

```bash
git add hpo_baselines/kaggle_playground.py tests/test_kaggle_playground.py
git commit -m "feat: preprocess kaggle regression data"
```

---

### Task 3: Cache Builder And KaggleRegressionTask

**Files:**
- Modify: `hpo_baselines/kaggle_playground.py`
- Modify: `hpo_baselines/__init__.py`
- Modify: `tests/test_kaggle_playground.py`

- [ ] **Step 1: Add failing cache adapter test**

Append to `tests/test_kaggle_playground.py`:

```python
import json

from hpo_baselines.kaggle_playground import KaggleRegressionTask


def test_kaggle_regression_task_reads_cache_and_meta_features(tmp_path):
    cache_path = tmp_path / "cache.json"
    cache_path.write_text(
        json.dumps(
            {
                "task": {"slug": "demo", "name": "Demo", "target_column": "target"},
                "meta_features": [1.0, 2.0, 3.0, 4.0, 5.0, 0.1, 0.5, 2.5],
                "metric": {"name": "RMSE", "direction": "minimize", "reference_worst_percentile": 90},
                "configs": [
                    {
                        "config_id": 0,
                        "config": {
                            "learning_rate": 0.001,
                            "weight_decay": 0.0001,
                            "hidden_width": 32,
                            "num_layers": 1,
                            "dropout": 0.0,
                            "batch_size": 16
                        },
                        "learning_curve": [1.2, 1.0, 0.8],
                        "val_score": 0.8,
                        "test_score": 0.9
                    },
                    {
                        "config_id": 1,
                        "config": {
                            "learning_rate": 0.01,
                            "weight_decay": 0.001,
                            "hidden_width": 64,
                            "num_layers": 2,
                            "dropout": 0.1,
                            "batch_size": 32
                        },
                        "learning_curve": [1.3, 1.1, 0.7],
                        "val_score": 0.7,
                        "test_score": 0.85
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    task = KaggleRegressionTask(cache_path)
    result = task.evaluate(task.candidate_configs[1], seed=123)

    assert task.name == "kaggle_demo"
    assert task.metric_name() == "RMSE"
    assert task.meta_features().shape == (8,)
    assert result.val_score == 0.7
    assert result.test_score == 0.85
    assert result.learning_curve == [1.3, 1.1, 0.7]
```

- [ ] **Step 2: Run cache adapter test and verify it fails**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_kaggle_regression_task_reads_cache_and_meta_features -v
```

Expected: FAIL with import error or missing `KaggleRegressionTask`.

- [ ] **Step 3: Implement task search space, cache records, and adapter**

Append to `hpo_baselines/kaggle_playground.py`:

```python
from hpo_baselines.search_space import Parameter, SearchSpace
from hpo_baselines.tasks import Config, EvalResult


def kaggle_mlp_search_space() -> SearchSpace:
    return SearchSpace(
        [
            Parameter("learning_rate", "float", low=1e-4, high=5e-2, log=True),
            Parameter("weight_decay", "float", low=1e-7, high=1e-2, log=True),
            Parameter("hidden_width", "categorical", choices=(32, 64, 128, 256)),
            Parameter("num_layers", "categorical", choices=(1, 2, 3)),
            Parameter("dropout", "float", low=0.0, high=0.4),
            Parameter("batch_size", "categorical", choices=(32, 64, 128, 256)),
        ]
    )


class KaggleRegressionTask:
    def __init__(self, cache_path: str | Path) -> None:
        self.cache_path = Path(cache_path)
        self.cache = json.loads(self.cache_path.read_text(encoding="utf-8"))
        task = self.cache["task"]
        self.slug = str(task["slug"])
        self.display_name = str(task["name"])
        self.name = f"kaggle_{self.slug}"
        self.search_space = kaggle_mlp_search_space()
        self.candidate_configs = [
            dict(item["config"], __config_id__=int(item["config_id"]))
            for item in self.cache["configs"]
        ]
        self._by_id = {
            int(item["config_id"]): item for item in self.cache["configs"]
        }
        self.candidate_vectors = self.search_space.to_matrix(self.candidate_configs)
        self._meta_features = np.asarray(self.cache["meta_features"], dtype=float)

    @staticmethod
    def metric_name() -> str:
        return "RMSE"

    def meta_features(self) -> np.ndarray:
        return self._meta_features.copy()

    def evaluate(self, config: Config, seed: int = 0) -> EvalResult:
        del seed
        config_id = int(config.get("__config_id__", self._nearest_config_id(config)))
        item = self._by_id[config_id]
        return EvalResult(
            val_score=float(item["val_score"]),
            test_score=float(item["test_score"]),
            learning_curve=[float(value) for value in item["learning_curve"]],
            metadata={
                "slug": self.slug,
                "config_id": config_id,
                "cache_path": str(self.cache_path),
            },
        )

    def _nearest_config_id(self, config: Config) -> int:
        vector = self.search_space.to_vector(config)
        distances = np.linalg.norm(self.candidate_vectors - vector, axis=1)
        return int(self.candidate_configs[int(np.argmin(distances))]["__config_id__"])
```

- [ ] **Step 4: Export the adapter**

Modify `hpo_baselines/__init__.py` so it imports and exports:

```python
from .kaggle_playground import (
    KaggleRegressionTask,
    kaggle_mlp_search_space,
    load_manifest,
    nested_task_slugs,
)
```

Add these names to `__all__` if the file defines `__all__`.

- [ ] **Step 5: Run cache adapter tests and verify they pass**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_kaggle_regression_task_reads_cache_and_meta_features -v
```

Expected: PASS.

- [ ] **Step 6: Commit adapter slice**

Run:

```bash
git add hpo_baselines/kaggle_playground.py hpo_baselines/__init__.py tests/test_kaggle_playground.py
git commit -m "feat: add kaggle regression task adapter"
```

---

### Task 4: MLP Cache Generation

**Files:**
- Modify: `hpo_baselines/kaggle_playground.py`
- Create: `scripts/build_kaggle_playground_cache.py`
- Modify: `tests/test_kaggle_playground.py`

- [ ] **Step 1: Add failing tiny cache-builder test**

Append to `tests/test_kaggle_playground.py`:

```python
from hpo_baselines.kaggle_playground import build_task_cache


def test_build_task_cache_writes_learning_curves(tmp_path):
    raw_dir = tmp_path / "raw" / "demo"
    raw_dir.mkdir(parents=True)
    _write_csv(
        raw_dir / "train.csv",
        [
            {"id": i, "x": float(i), "group": "a" if i % 2 == 0 else "b", "target": float(i * 2)}
            for i in range(1, 31)
        ],
    )
    output = tmp_path / "cache" / "demo.json"
    spec = type("Spec", (), {"slug": "demo", "name": "Demo", "target_column": "target"})()

    build_task_cache(
        spec=spec,
        train_csv=raw_dir / "train.csv",
        output_path=output,
        configs_per_task=3,
        epochs_per_config=2,
        split_seed=123,
        config_seed=456,
    )

    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["task"]["slug"] == "demo"
    assert len(payload["configs"]) == 3
    assert len(payload["configs"][0]["learning_curve"]) == 2
    assert len(payload["meta_features"]) == 8
```

- [ ] **Step 2: Run cache-builder test and verify it fails**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_build_task_cache_writes_learning_curves -v
```

Expected: FAIL because `build_task_cache` is not implemented.

- [ ] **Step 3: Implement the MLP cache builder**

Append to `hpo_baselines/kaggle_playground.py`:

```python
import torch
from torch import nn


class _TabularMLP(nn.Module):
    def __init__(self, input_dim: int, hidden_width: int, num_layers: int, dropout: float) -> None:
        super().__init__()
        layers: list[nn.Module] = []
        current = input_dim
        for _ in range(num_layers):
            layers.append(nn.Linear(current, hidden_width))
            layers.append(nn.ReLU())
            if dropout > 0:
                layers.append(nn.Dropout(dropout))
            current = hidden_width
        layers.append(nn.Linear(current, 1))
        self.net = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x).squeeze(-1)


def build_task_cache(
    spec: Any,
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
        curve, val_score, test_score = _train_cached_mlp(
            prepared=prepared,
            config=config,
            epochs=epochs_per_config,
            seed=config_seed + config_id,
        )
        records.append(
            {
                "config_id": config_id,
                "config": config,
                "learning_curve": curve,
                "val_score": val_score,
                "test_score": test_score,
            }
        )
    output = {
        "task": {
            "slug": spec.slug,
            "name": spec.name,
            "target_column": spec.target_column,
        },
        "metric": {
            "name": "RMSE",
            "direction": "minimize",
            "reference_worst_percentile": 90,
        },
        "meta_features": [float(value) for value in prepared.meta_features],
        "configs": records,
    }
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2), encoding="utf-8")


def _train_cached_mlp(
    prepared: PreparedRegressionData,
    config: dict[str, Any],
    epochs: int,
    seed: int,
) -> tuple[list[float], float, float]:
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
    batch_size = int(config["batch_size"])
    curve: list[float] = []
    for _ in range(epochs):
        order = torch.randperm(len(x_train))
        model.train()
        for start in range(0, len(order), batch_size):
            idx = order[start : start + batch_size]
            loss = torch.mean((model(x_train[idx]) - y_train[idx]) ** 2)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        curve.append(_rmse_original_scale(model, x_val, y_val, prepared.y_std))
    test_score = _rmse_original_scale(model, x_test, y_test, prepared.y_std)
    return curve, float(curve[-1]), test_score


def _rmse_original_scale(
    model: nn.Module, x: torch.Tensor, y: torch.Tensor, y_std: float
) -> float:
    model.eval()
    with torch.no_grad():
        pred = model(x)
        rmse_scaled = torch.sqrt(torch.mean((pred - y) ** 2))
    return float(rmse_scaled.item() * y_std)
```

- [ ] **Step 4: Add cache-builder script**

Create `scripts/build_kaggle_playground_cache.py`:

```python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (project_root := str(PROJECT_ROOT)) not in sys.path:
    sys.path.insert(0, project_root)

from hpo_baselines.kaggle_playground import build_task_cache, load_manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Kaggle Playground HPO caches.")
    parser.add_argument("--manifest", type=Path, default=PROJECT_ROOT / "data" / "kaggle_playground" / "manifest.json")
    parser.add_argument("--raw-dir", type=Path, default=PROJECT_ROOT / "data" / "kaggle_playground" / "raw")
    parser.add_argument("--cache-dir", type=Path, default=PROJECT_ROOT / "data" / "kaggle_playground" / "cache")
    parser.add_argument("--tasks", type=str, default="all")
    parser.add_argument("--configs-per-task", type=int, default=None)
    parser.add_argument("--epochs-per-config", type=int, default=None)
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    selected = {item.strip() for item in args.tasks.split(",")} if args.tasks != "all" else None
    for spec in manifest.tasks:
        if selected is not None and spec.slug not in selected:
            continue
        build_task_cache(
            spec=spec,
            train_csv=args.raw_dir / spec.slug / "train.csv",
            output_path=args.cache_dir / f"{spec.slug}.json",
            configs_per_task=args.configs_per_task or manifest.cache.configs_per_task,
            epochs_per_config=args.epochs_per_config or manifest.cache.epochs_per_config,
            split_seed=manifest.cache.split_seed,
            config_seed=manifest.cache.split_seed,
        )
        print(f"wrote {args.cache_dir / f'{spec.slug}.json'}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run cache-builder tests and smoke script**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_build_task_cache_writes_learning_curves -v
uv run python scripts/build_kaggle_playground_cache.py --help
```

Expected: test PASS, script prints argparse help.

- [ ] **Step 6: Commit cache-builder slice**

Run:

```bash
git add hpo_baselines/kaggle_playground.py scripts/build_kaggle_playground_cache.py tests/test_kaggle_playground.py
git commit -m "feat: build kaggle hpo caches"
```

---

### Task 5: Normalized Simple Regret

**Files:**
- Modify: `hpo_baselines/kaggle_playground.py`
- Modify: `hpo_baselines/evaluator.py`
- Modify: `tests/test_kaggle_playground.py`

- [ ] **Step 1: Add failing normalized regret test**

Append to `tests/test_kaggle_playground.py`:

```python
from hpo_baselines.kaggle_playground import normalized_simple_regret_reference


def test_normalized_simple_regret_uses_table_oracle_and_percentile():
    oracle, reference = normalized_simple_regret_reference([0.4, 0.5, 0.8, 10.0], percentile=90)

    assert oracle == 0.4
    assert reference < 10.0
    assert reference > 0.8
```

- [ ] **Step 2: Run normalized regret test and verify it fails**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_normalized_simple_regret_uses_table_oracle_and_percentile -v
```

Expected: FAIL because `normalized_simple_regret_reference` is missing.

- [ ] **Step 3: Implement regret reference helpers**

Append to `hpo_baselines/kaggle_playground.py`:

```python
def normalized_simple_regret_reference(
    validation_scores: list[float] | np.ndarray, percentile: float = 90
) -> tuple[float, float]:
    scores = np.asarray(validation_scores, dtype=float)
    if scores.ndim != 1 or len(scores) == 0:
        raise ValueError("validation_scores must be a non-empty 1D sequence")
    oracle = float(np.min(scores))
    reference = float(np.percentile(scores, percentile))
    if reference <= oracle:
        reference = oracle + 1e-8
    return oracle, reference


def normalized_simple_regret(best_val_score: float, oracle: float, reference: float) -> float:
    return float((best_val_score - oracle) / (reference - oracle + 1e-8))
```

- [ ] **Step 4: Add normalized fields to evaluator summaries**

Modify `BaselineEvaluator.summarize` and `CrossDatasetEvaluator.summarize` in `hpo_baselines/evaluator.py` so each run row includes:

```python
oracle = getattr(trace, "metadata", {}).get("oracle_val_score") if hasattr(trace, "metadata") else None
reference = getattr(trace, "metadata", {}).get("reference_worst_val_score") if hasattr(trace, "metadata") else None
```

If `OptimizationTrace` has no metadata field, compute normalized regret in a helper using task-level cached metadata from each `EvalResult.metadata`:

```python
normalizer = best.metadata.get("normalizer", {})
oracle = normalizer.get("oracle_val_score")
reference = normalizer.get("reference_worst_val_score")
if oracle is not None and reference is not None:
    normalized = (best.val_score - oracle) / (reference - oracle + 1e-8)
else:
    normalized = best.val_score - oracle_by_task_seed[(trace.task, trace.seed)]
```

Add summary columns:

```python
"normalized_simple_regret_mean": _mean(rows, "normalized_simple_regret"),
"normalized_simple_regret_std": _std(rows, "normalized_simple_regret"),
```

- [ ] **Step 5: Put normalizer metadata into `KaggleRegressionTask.evaluate`**

In `KaggleRegressionTask.__init__`, compute:

```python
scores = [float(item["val_score"]) for item in self.cache["configs"]]
self.oracle_val_score, self.reference_worst_val_score = normalized_simple_regret_reference(scores, 90)
```

In `evaluate`, add:

```python
"normalizer": {
    "oracle_val_score": self.oracle_val_score,
    "reference_worst_val_score": self.reference_worst_val_score,
},
```

- [ ] **Step 6: Run tests**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py -v
```

Expected: all tests PASS.

- [ ] **Step 7: Commit metric slice**

Run:

```bash
git add hpo_baselines/kaggle_playground.py hpo_baselines/evaluator.py tests/test_kaggle_playground.py
git commit -m "feat: report normalized simple regret"
```

---

### Task 6: Separate Meta-Train And Evaluation Tasks

**Files:**
- Modify: `hpo_baselines/optimizers.py`
- Modify: `hpo_baselines/evaluator.py`
- Modify: `tests/test_kaggle_playground.py`

- [ ] **Step 1: Add failing API test for separate task sets**

Append to `tests/test_kaggle_playground.py`:

```python
import inspect

from hpo_baselines.optimizers import CrossDatasetLCDQNOptimizer


def test_cross_dataset_lcdqn_accepts_evaluation_tasks():
    signature = inspect.signature(CrossDatasetLCDQNOptimizer.optimize)

    assert "evaluation_tasks" in signature.parameters
```

- [ ] **Step 2: Run API test and verify it fails**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_cross_dataset_lcdqn_accepts_evaluation_tasks -v
```

Expected: FAIL because `evaluation_tasks` is not in the signature.

- [ ] **Step 3: Extend cross-dataset optimizer signatures**

Modify `CrossDatasetHyperRLOptimizer.optimize` and `CrossDatasetLCDQNOptimizer.optimize` in `hpo_baselines/optimizers.py`:

```python
def optimize(
    self,
    tasks: list[HPOTask],
    total_episodes: int | None = None,
    seed: int = 0,
    evaluation_budget: int | None = None,
    evaluation_tasks: list[HPOTask] | None = None,
) -> list[OptimizationTrace]:
```

Pass `evaluation_tasks=evaluation_tasks` into `controller.optimize_cross_dataset(...)`.

- [ ] **Step 4: Extend controller evaluation path**

Modify `_CrossDatasetDQNController.optimize_cross_dataset`:

```python
def optimize_cross_dataset(
    self,
    total_episodes: int,
    seed: int,
    evaluation_budget: int = 50,
    evaluation_tasks: list[HPOTask] | None = None,
) -> list[OptimizationTrace]:
```

After meta-training, evaluate:

```python
tasks_to_evaluate = evaluation_tasks or self.tasks
for task in tasks_to_evaluate:
    if task.name not in runtime.task_data:
        runtime.task_data[task.name] = self._prepare_single_task_data(task, rng)
    trace = self._evaluate_task(task, runtime, rng, total_episodes, seed, evaluation_budget)
```

Add helper:

```python
def _prepare_single_task_data(
    self, task: HPOTask, rng: np.random.Generator
) -> _CrossDatasetTaskData:
    configs = _candidate_configs(task)
    if configs is None:
        budget_estimate = max(self.episode_budget * 8, 128)
        configs = task.search_space.sample_many(rng, budget_estimate)
    return _CrossDatasetTaskData(
        task=task,
        configs=configs,
        action_vectors=task.search_space.to_matrix(configs),
        meta=_meta_features(task),
    )
```

Refactor `_prepare_task_data` to call `_prepare_single_task_data` for each training task.

- [ ] **Step 5: Extend `CrossDatasetEvaluator`**

Modify the dataclass in `hpo_baselines/evaluator.py` to add:

```python
evaluation_tasks: list[HPOTask] | None = None
```

In `run`, when a method supports cross-dataset, call:

```python
method.optimize(
    self.tasks,
    self.total_episodes,
    seed,
    self.evaluation_budget,
    evaluation_tasks=self.evaluation_tasks,
)
```

For non-meta baselines, iterate over:

```python
tasks_to_evaluate = self.evaluation_tasks or self.tasks
```

- [ ] **Step 6: Run API and existing smoke tests**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py::test_cross_dataset_lcdqn_accepts_evaluation_tasks -v
uv run python scripts/run_lcbench_baselines.py --data-path data/tiny_lcbench.json --budget 2 --seeds 1 --limit-configs 4 --cross-dataset --total-episodes 2 --output-dir results/smoke_lcbench
```

Expected: test PASS and smoke command exits 0.

- [ ] **Step 7: Commit train/eval split slice**

Run:

```bash
git add hpo_baselines/optimizers.py hpo_baselines/evaluator.py tests/test_kaggle_playground.py
git commit -m "feat: separate cross-dataset train and eval tasks"
```

---

### Task 7: Download And Experiment Runner Scripts

**Files:**
- Create: `scripts/download_kaggle_playground.py`
- Create: `scripts/run_kaggle_playground.py`
- Modify: `README.md`

- [ ] **Step 1: Add download helper**

Create `scripts/download_kaggle_playground.py`:

```python
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (project_root := str(PROJECT_ROOT)) not in sys.path:
    sys.path.insert(0, project_root)

from hpo_baselines.kaggle_playground import load_manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Download Kaggle Playground raw data.")
    parser.add_argument("--manifest", type=Path, default=PROJECT_ROOT / "data" / "kaggle_playground" / "manifest.json")
    parser.add_argument("--raw-dir", type=Path, default=PROJECT_ROOT / "data" / "kaggle_playground" / "raw")
    parser.add_argument("--tasks", type=str, default="all")
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    selected = {item.strip() for item in args.tasks.split(",")} if args.tasks != "all" else None
    args.raw_dir.mkdir(parents=True, exist_ok=True)
    for spec in manifest.tasks:
        if selected is not None and spec.slug not in selected:
            continue
        out_dir = args.raw_dir / spec.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [
                "kaggle",
                "competitions",
                "download",
                "-c",
                spec.slug,
                "-p",
                str(out_dir),
                "--unzip",
            ],
            check=True,
        )


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Add experiment runner**

Create `scripts/run_kaggle_playground.py`:

```python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (project_root := str(PROJECT_ROOT)) not in sys.path:
    sys.path.insert(0, project_root)

from hpo_baselines import (
    BayesianOptimization,
    CrossDatasetEvaluator,
    CrossDatasetHyperRLOptimizer,
    CrossDatasetLCDQNOptimizer,
    KaggleRegressionTask,
    RandomSearch,
)
from hpo_baselines.kaggle_playground import load_manifest, nested_task_slugs


def _tasks_by_slug(cache_dir: Path, manifest_path: Path) -> dict[str, KaggleRegressionTask]:
    manifest = load_manifest(manifest_path)
    return {
        spec.slug: KaggleRegressionTask(cache_dir / f"{spec.slug}.json")
        for spec in manifest.tasks
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Kaggle Playground HPO experiments.")
    parser.add_argument("--manifest", type=Path, default=PROJECT_ROOT / "data" / "kaggle_playground" / "manifest.json")
    parser.add_argument("--cache-dir", type=Path, default=PROJECT_ROOT / "data" / "kaggle_playground" / "cache")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results" / "kaggle_playground")
    parser.add_argument("--suite", choices=("all-methods", "lcdqn-task-count"), default="all-methods")
    parser.add_argument("--budget", type=int, default=20)
    parser.add_argument("--seeds", type=int, default=5)
    parser.add_argument("--total-episodes", type=int, default=150)
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    by_slug = _tasks_by_slug(args.cache_dir, args.manifest)
    all_tasks = [by_slug[spec.slug] for spec in manifest.tasks]
    dqn_kwargs = {
        "hidden_sizes": (64, 64),
        "batch_size": min(4, args.budget),
        "learning_starts": min(2, args.budget),
        "target_update_freq": 4,
        "episode_budget": args.budget,
        "evaluation_budget": args.budget,
    }
    if args.suite == "all-methods":
        evaluator = CrossDatasetEvaluator(
            tasks=all_tasks,
            methods=[
                RandomSearch(),
                BayesianOptimization(initial_points=min(3, args.budget)),
                CrossDatasetHyperRLOptimizer(**dqn_kwargs),
                CrossDatasetLCDQNOptimizer(**dqn_kwargs),
            ],
            total_episodes=args.total_episodes,
            evaluation_budget=args.budget,
            seeds=list(range(args.seeds)),
        )
        traces = evaluator.run()
        evaluator.save(traces, args.output_dir / "all_methods")
    else:
        for count in (1, 5, 10, 15):
            train_tasks = [by_slug[slug] for slug in nested_task_slugs(manifest, count)]
            evaluator = CrossDatasetEvaluator(
                tasks=train_tasks,
                evaluation_tasks=all_tasks,
                methods=[CrossDatasetLCDQNOptimizer(**dqn_kwargs)],
                total_episodes=args.total_episodes,
                evaluation_budget=args.budget,
                seeds=list(range(args.seeds)),
            )
            traces = evaluator.run()
            evaluator.save(traces, args.output_dir / "lcdqn_task_count" / f"train_{count}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Document Kaggle commands in README**

Add this section to `README.md`:

```markdown
## Kaggle Playground Regression Benchmark

The Kaggle Playground benchmark uses a fixed 15-task regression pool defined in
`data/kaggle_playground/manifest.json`. Raw Kaggle data is not committed.

Download raw competition files:

```bash
uv run python scripts/download_kaggle_playground.py --tasks all
```

Build cached MLP learning-curve tables:

```bash
uv run python scripts/build_kaggle_playground_cache.py --tasks all
```

Run all methods on all 15 tasks:

```bash
uv run python scripts/run_kaggle_playground.py --suite all-methods
```

Run the LC-DQN task-count sweep:

```bash
uv run python scripts/run_kaggle_playground.py --suite lcdqn-task-count
```
```

- [ ] **Step 4: Smoke scripts**

Run:

```bash
uv run python scripts/download_kaggle_playground.py --help
uv run python scripts/build_kaggle_playground_cache.py --help
uv run python scripts/run_kaggle_playground.py --help
```

Expected: all three commands print argparse help and exit 0.

- [ ] **Step 5: Commit scripts slice**

Run:

```bash
git add scripts/download_kaggle_playground.py scripts/run_kaggle_playground.py README.md
git commit -m "feat: add kaggle playground runners"
```

---

### Task 8: Final Verification And Graph Refresh

**Files:**
- No planned source edits unless verification finds issues.

- [ ] **Step 1: Run unit tests**

Run:

```bash
uv run pytest tests/test_kaggle_playground.py -v
```

Expected: all tests PASS.

- [ ] **Step 2: Run existing tiny LCBench smoke**

Run:

```bash
uv run python scripts/run_lcbench_baselines.py --data-path data/tiny_lcbench.json --budget 2 --seeds 1 --limit-configs 4 --output-dir results/smoke_lcbench
```

Expected: command exits 0 and writes `results/smoke_lcbench/single_task/summary.csv`.

- [ ] **Step 3: Run existing tiny cross-dataset smoke**

Run:

```bash
uv run python scripts/run_lcbench_baselines.py --data-path data/tiny_lcbench.json --budget 2 --seeds 1 --limit-configs 4 --cross-dataset --total-episodes 2 --output-dir results/smoke_lcbench_cross
```

Expected: command exits 0 and writes `results/smoke_lcbench_cross/cross_dataset/summary.csv`.

- [ ] **Step 4: Run graphify update after code changes**

Run:

```bash
graphify update .
```

Expected: graph update completes without errors.

- [ ] **Step 5: Inspect final git diff**

Run:

```bash
git status --short
git diff --stat HEAD
```

Expected: only intentional benchmark implementation files are modified or untracked.

- [ ] **Step 6: Commit final verification fixes if any**

If Step 1, 2, 3, or 4 required code changes, commit them:

```bash
git add <changed-files>
git commit -m "fix: stabilize kaggle playground benchmark"
```

If no changes were required, do not create an empty commit.

---

## Self-Review

Spec coverage:

- Fixed 15-task pool: Task 1.
- 256 configs, 25 epochs, 1 seed, 80/10/10: Task 1 and Task 4.
- Shared preprocessing and 8 meta-features: Task 2.
- Cached HPO task adapter: Task 3.
- Normalized simple regret with 90th percentile reference-worst: Task 5.
- All-methods benchmark and LC-DQN task-count sweep: Task 6 and Task 7.
- Train on nested subsets and evaluate on all 15 tasks: Task 6 and Task 7.
- Outputs under `results/kaggle_playground/`: Task 7.
- Verification and graph refresh: Task 8.

Placeholder scan:

- This plan contains no TBD, TODO, FIXME, or implementation placeholders.

Type consistency:

- `KaggleTaskSpec.slug`, `KaggleRegressionTask.name`, and cache task `slug` are used consistently.
- `meta_features()` returns an 8-dimensional NumPy array.
- `evaluation_tasks` is consistently passed from `CrossDatasetEvaluator` to cross-dataset optimizers and then to `_CrossDatasetDQNController.optimize_cross_dataset`.
