import csv
import json
from pathlib import Path
import sys

import numpy as np
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from hpo_baselines.kaggle_playground import (
    KaggleRegressionTask,
    load_manifest,
    nested_task_slugs,
    prepare_tabular_regression_data,
)

MANIFEST = PROJECT_ROOT / "data" / "kaggle_playground" / "manifest.json"


def _valid_kaggle_cache() -> dict[str, object]:
    return {
        "task": {
            "slug": "kaggle_demo",
            "display_name": "Kaggle Demo",
            "meta_features": [float(i) for i in range(16)],
        },
        "metric": {"name": "RMSE", "direction": "minimize"},
        "configs": [
            {
                "config_id": 0,
                "config": {
                    "learning_rate": 0.001,
                    "weight_decay": 0.0,
                    "hidden_width": 64,
                    "num_layers": 1,
                    "dropout": 0.0,
                    "batch_size": 32,
                },
                "val_score": 1.25,
                "test_score": 1.5,
                "learning_curve": [2.0, 1.5, 1.25],
            },
            {
                "config_id": 1,
                "config": {
                    "learning_rate": 0.01,
                    "weight_decay": 0.0001,
                    "hidden_width": 128,
                    "num_layers": 2,
                    "dropout": 0.1,
                    "batch_size": 64,
                },
                "val_score": 0.75,
                "test_score": 0.9,
                "learning_curve": [1.4, 1.0, 0.75],
            },
        ],
    }


def test_kaggle_regression_task_reads_cache_and_meta_features(tmp_path):
    cache_path = tmp_path / "kaggle_demo.json"
    cache_path.write_text(
        json.dumps(_valid_kaggle_cache()),
        encoding="utf-8",
    )

    task = KaggleRegressionTask(cache_path)
    result = task.evaluate({"__config_id__": 1}, seed=123)

    assert task.name == "kaggle_demo"
    assert task.metric_name() == "RMSE"
    assert task.meta_features().shape == (16,)
    assert result.val_score == 0.75
    assert result.test_score == 0.9
    assert result.learning_curve == [1.4, 1.0, 0.75]


def test_kaggle_regression_task_rejects_duplicate_config_ids(tmp_path):
    cache_path = tmp_path / "duplicate_ids.json"
    raw = _valid_kaggle_cache()
    raw["configs"][1]["config_id"] = 0
    cache_path.write_text(json.dumps(raw), encoding="utf-8")

    with pytest.raises(ValueError) as exc_info:
        KaggleRegressionTask(cache_path)

    message = str(exc_info.value)
    assert cache_path.name in message
    assert "duplicate" in message
    assert "config_id=0" in message


def test_kaggle_regression_task_rejects_missing_hyperparameter_field(tmp_path):
    cache_path = tmp_path / "missing_hyperparameter.json"
    raw = _valid_kaggle_cache()
    del raw["configs"][1]["config"]["dropout"]
    cache_path.write_text(json.dumps(raw), encoding="utf-8")

    with pytest.raises(ValueError) as exc_info:
        KaggleRegressionTask(cache_path)

    message = str(exc_info.value)
    assert cache_path.name in message
    assert "missing" in message
    assert "dropout" in message
    assert "config_id=1" in message


def test_kaggle_regression_task_rejects_missing_config_id(tmp_path):
    cache_path = tmp_path / "missing_config_id.json"
    raw = _valid_kaggle_cache()
    del raw["configs"][1]["config_id"]
    cache_path.write_text(json.dumps(raw), encoding="utf-8")

    with pytest.raises(ValueError) as exc_info:
        KaggleRegressionTask(cache_path)

    message = str(exc_info.value)
    assert cache_path.name in message
    assert "config index 1" in message
    assert "config_id" in message


def test_kaggle_regression_task_rejects_non_list_learning_curve(tmp_path):
    cache_path = tmp_path / "bad_learning_curve.json"
    raw = _valid_kaggle_cache()
    raw["configs"][1]["learning_curve"] = "123"
    cache_path.write_text(json.dumps(raw), encoding="utf-8")

    with pytest.raises(ValueError) as exc_info:
        KaggleRegressionTask(cache_path)

    message = str(exc_info.value)
    assert cache_path.name in message
    assert "config_id=1" in message
    assert "learning_curve" in message
    assert "non-empty list" in message


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


def test_prepare_tabular_regression_data_fits_numeric_columns_from_train_only(tmp_path):
    csv_path = tmp_path / "train.csv"
    _write_csv(
        csv_path,
        [
            {"id": 1, "num": 1.0, "target": 10.0},
            {"id": 2, "num": "not-a-number", "target": 12.0},
            {"id": 3, "num": "NaN", "target": 14.0},
            {"id": 4, "num": "inf", "target": 16.0},
            {"id": 5, "num": 5.0, "target": 18.0},
        ],
    )

    prepared = prepare_tabular_regression_data(
        csv_path=csv_path,
        target_column="target",
        split_seed=123,
        split=(0.6, 0.2, 0.2),
    )

    assert prepared.feature_names == ("num",)
    assert prepared.x_train.shape == (3, 1)
    assert prepared.x_val.shape == (1, 1)
    assert prepared.x_test.shape == (1, 1)
    assert np.all(np.isfinite(prepared.x_train))
    assert np.all(np.isfinite(prepared.x_val))
    assert np.all(np.isfinite(prepared.x_test))
    assert np.all(np.isfinite(prepared.meta_features))


def test_prepare_tabular_regression_data_unknown_categories_keep_train_schema(tmp_path):
    csv_path = tmp_path / "train.csv"
    _write_csv(
        csv_path,
        [
            {"id": 1, "cat": "a", "target": 10.0},
            {"id": 2, "cat": "unseen-test", "target": 12.0},
            {"id": 3, "cat": "b", "target": 14.0},
            {"id": 4, "cat": "unseen-val", "target": 16.0},
            {"id": 5, "cat": "a", "target": 18.0},
        ],
    )

    prepared = prepare_tabular_regression_data(
        csv_path=csv_path,
        target_column="target",
        split_seed=123,
        split=(0.6, 0.2, 0.2),
    )

    assert prepared.feature_names == ("cat=a", "cat=b")
    assert prepared.x_train.shape == (3, 2)
    assert prepared.x_val.shape == (1, 2)
    assert prepared.x_test.shape == (1, 2)
    assert np.array_equal(prepared.x_val[0], np.zeros(2, dtype=np.float32))
    assert np.array_equal(prepared.x_test[0], np.zeros(2, dtype=np.float32))
