import csv
from pathlib import Path
import sys

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from hpo_baselines.kaggle_playground import (
    load_manifest,
    nested_task_slugs,
    prepare_tabular_regression_data,
)

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
    assert prepared.x_train.shape[1] == prepared.x_test.shape[1]
    assert np.all(np.isfinite(prepared.x_train))
    assert np.all(np.isfinite(prepared.y_train))
    assert prepared.meta_features.shape == (16,)
    assert prepared.meta_features[0] == 8
    assert prepared.meta_features[1] == np.log1p(8)
    assert prepared.meta_features[2] == prepared.x_train.shape[1]
    assert prepared.meta_features[3] == np.log1p(prepared.x_train.shape[1])
    assert np.all(np.isfinite(prepared.meta_features))
