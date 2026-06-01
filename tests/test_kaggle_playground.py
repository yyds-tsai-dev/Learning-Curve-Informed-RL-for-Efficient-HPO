import argparse
import csv
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from hpo_baselines.evaluator import BaselineEvaluator, CrossDatasetEvaluator
import hpo_baselines.kaggle_playground as kaggle_playground
from hpo_baselines.kaggle_playground import (
    KaggleRegressionTask,
    KaggleTaskSpec,
    build_task_cache,
    load_manifest,
    nested_task_slugs,
    normalized_simple_regret,
    normalized_simple_regret_reference,
    prepare_tabular_regression_data,
)
from hpo_baselines.optimizers import RandomSearch
from scripts.build_kaggle_playground_cache import positive_int

MANIFEST = PROJECT_ROOT / "data" / "kaggle_playground" / "manifest.json"


def _valid_kaggle_cache() -> dict[str, object]:
    return {
        "task": {
            "slug": "kaggle_demo",
            "name": "Kaggle Demo",
            "target_column": "target",
        },
        "meta_features": [float(i) for i in range(16)],
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


def test_normalized_simple_regret_reference_uses_table_oracle_and_percentile():
    oracle, reference = normalized_simple_regret_reference([10.0, 1.0, 4.0, 2.0])

    assert oracle == 1.0
    assert reference == pytest.approx(8.2)
    assert normalized_simple_regret(4.6, oracle, reference) == pytest.approx(0.5)


@pytest.mark.parametrize(
    ("scores", "percentile", "match"),
    [
        ([], 90, "non-empty"),
        ([[1.0, 2.0]], 90, "1D"),
        ([1.0, float("inf")], 90, "finite"),
        ([1.0, 2.0], -1, "percentile"),
        ([1.0, 2.0], 101, "percentile"),
    ],
)
def test_normalized_simple_regret_reference_validates_inputs(
    scores, percentile, match
):
    with pytest.raises(ValueError, match=match):
        normalized_simple_regret_reference(scores, percentile=percentile)


def test_normalized_simple_regret_reference_falls_back_when_reference_equals_oracle():
    oracle, reference = normalized_simple_regret_reference([3.0, 3.0, 3.0])

    assert oracle == 3.0
    assert reference > oracle
    assert normalized_simple_regret(3.0, oracle, reference) == 0.0
    assert normalized_simple_regret(4.0, oracle, reference) > 0.0


def test_kaggle_regression_task_exposes_normalizer_metadata(tmp_path):
    cache_path = tmp_path / "kaggle_demo.json"
    cache_path.write_text(json.dumps(_valid_kaggle_cache()), encoding="utf-8")

    task = KaggleRegressionTask(cache_path)
    result = task.evaluate({"__config_id__": 0}, seed=123)

    assert task.oracle_val_score == 0.75
    assert task.reference_worst_val_score == pytest.approx(1.2)
    assert result.metadata["normalizer"] == {
        "oracle_val_score": 0.75,
        "reference_worst_val_score": pytest.approx(1.2),
    }


def _trace(
    *,
    task: str,
    method: str,
    seed: int,
    scores: list[float],
    normalizer: dict[str, float] | None = None,
):
    records = []
    for iteration, score in enumerate(scores):
        metadata = {"normalizer": normalizer} if normalizer is not None else {}
        records.append(
            SimpleNamespace(
                iteration=iteration,
                val_score=score,
                test_score=score + 0.1,
                metadata=metadata,
                extra=metadata,
            )
        )
    return SimpleNamespace(
        task=task,
        method=method,
        seed=seed,
        evaluations=records,
        best_record=min(records, key=lambda record: record.val_score),
    )


def test_baseline_evaluator_summarize_reports_kaggle_normalized_simple_regret():
    traces = [
        _trace(
            task="kaggle_demo",
            method="A",
            seed=0,
            scores=[1.4, 1.2],
            normalizer={"oracle_val_score": 1.0, "reference_worst_val_score": 3.0},
        ),
        _trace(
            task="kaggle_demo",
            method="A",
            seed=1,
            scores=[2.0],
            normalizer={"oracle_val_score": 1.0, "reference_worst_val_score": 3.0},
        ),
    ]

    summary = BaselineEvaluator(tasks=[], methods=[]).summarize(traces)

    assert summary[0]["simple_regret_mean"] == pytest.approx(0.0)
    assert summary[0]["normalized_simple_regret_mean"] == pytest.approx(0.3)
    assert summary[0]["normalized_simple_regret_std"] == pytest.approx(
        np.std([0.1, 0.5], ddof=1)
    )


def test_random_search_trace_preserves_kaggle_normalizer_for_summary(tmp_path):
    cache_path = tmp_path / "kaggle_demo.json"
    cache_path.write_text(json.dumps(_valid_kaggle_cache()), encoding="utf-8")

    task = KaggleRegressionTask(cache_path)
    trace = RandomSearch().optimize(task, budget=1, seed=1)
    best_extra = trace.best_record.extra

    assert best_extra["normalizer"] == {
        "oracle_val_score": 0.75,
        "reference_worst_val_score": pytest.approx(1.2),
    }

    summary = BaselineEvaluator(tasks=[task], methods=[]).summarize([trace])
    expected_normalized = normalized_simple_regret(1.25, 0.75, 1.2)

    assert summary[0]["simple_regret_mean"] == pytest.approx(0.0)
    assert summary[0]["normalized_simple_regret_mean"] == pytest.approx(
        expected_normalized
    )
    assert summary[0]["normalized_simple_regret_mean"] != pytest.approx(
        summary[0]["simple_regret_mean"]
    )


def test_cross_dataset_evaluator_summarize_falls_back_to_raw_simple_regret():
    traces = [
        _trace(task="lcbench_demo", method="A", seed=0, scores=[3.0, 2.0]),
        _trace(task="lcbench_demo", method="B", seed=0, scores=[1.5]),
    ]

    summary = CrossDatasetEvaluator(tasks=[], methods=[]).summarize(traces)
    by_method = {row["method"]: row for row in summary}

    assert by_method["A"]["simple_regret_mean"] == pytest.approx(0.5)
    assert by_method["A"]["normalized_simple_regret_mean"] == pytest.approx(0.5)
    assert by_method["B"]["normalized_simple_regret_mean"] == pytest.approx(0.0)


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


def test_kaggle_regression_task_rejects_non_integral_config_id(tmp_path):
    cache_path = tmp_path / "non_integral_config_id.json"
    raw = _valid_kaggle_cache()
    raw["configs"][1]["config_id"] = 1.5
    cache_path.write_text(json.dumps(raw), encoding="utf-8")

    with pytest.raises(ValueError) as exc_info:
        KaggleRegressionTask(cache_path)

    message = str(exc_info.value)
    assert cache_path.name in message
    assert "config_id=1.5" in message
    assert "integer" in message


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


def test_build_task_cache_writes_learning_curves(tmp_path):
    raw_dir = tmp_path / "raw" / "demo"
    raw_dir.mkdir(parents=True)
    train_csv = raw_dir / "train.csv"
    rows = [
        {
            "id": row_id,
            "x": float(row_id),
            "group": ["a", "b", "c"][row_id % 3],
            "target": float(2 * row_id + (row_id % 3)),
        }
        for row_id in range(30)
    ]
    _write_csv(train_csv, rows)

    output_path = tmp_path / "cache" / "demo.json"
    spec = KaggleTaskSpec(
        slug="demo",
        episode="demo",
        name="Demo",
        target_column="target",
    )

    build_task_cache(
        spec=spec,
        train_csv=train_csv,
        output_path=output_path,
        configs_per_task=3,
        epochs_per_config=2,
        split_seed=123,
        config_seed=456,
    )

    raw = json.loads(output_path.read_text(encoding="utf-8"))
    assert raw["task"] == {
        "slug": "demo",
        "name": "Demo",
        "target_column": "target",
    }
    assert len(raw["meta_features"]) == 16
    assert len(raw["configs"]) == 3
    for index, item in enumerate(raw["configs"]):
        assert item["config_id"] == index
        assert len(item["learning_curve"]) == 2

    task = KaggleRegressionTask(output_path)
    assert task.name == "demo"
    assert task.meta_features().shape == (16,)


def test_build_task_cache_rejects_non_positive_configs_per_task(tmp_path):
    spec = KaggleTaskSpec(
        slug="demo",
        episode="demo",
        name="Demo",
        target_column="target",
    )

    with pytest.raises(ValueError, match=r"configs_per_task.*positive"):
        build_task_cache(
            spec=spec,
            train_csv=tmp_path / "missing.csv",
            output_path=tmp_path / "cache" / "demo.json",
            configs_per_task=0,
            epochs_per_config=1,
            split_seed=123,
            config_seed=456,
        )


def test_build_task_cache_rejects_non_positive_epochs_per_config(tmp_path):
    spec = KaggleTaskSpec(
        slug="demo",
        episode="demo",
        name="Demo",
        target_column="target",
    )

    with pytest.raises(ValueError, match=r"epochs_per_config.*positive"):
        build_task_cache(
            spec=spec,
            train_csv=tmp_path / "missing.csv",
            output_path=tmp_path / "cache" / "demo.json",
            configs_per_task=1,
            epochs_per_config=0,
            split_seed=123,
            config_seed=456,
        )


@pytest.mark.parametrize("raw_value", ["0", "-1"])
def test_positive_int_rejects_non_positive_values(raw_value):
    with pytest.raises(argparse.ArgumentTypeError, match="positive"):
        positive_int(raw_value)


def test_build_task_cache_rejects_nonfinite_scores_before_write(tmp_path, monkeypatch):
    train_csv = tmp_path / "train.csv"
    rows = [
        {
            "id": row_id,
            "x": float(row_id),
            "target": float(row_id),
        }
        for row_id in range(30)
    ]
    _write_csv(train_csv, rows)

    output_path = tmp_path / "cache" / "demo.json"
    spec = KaggleTaskSpec(
        slug="demo",
        episode="demo",
        name="Demo",
        target_column="target",
    )

    def train_with_nan(*args, **kwargs):
        return {
            "val_score": float("nan"),
            "test_score": 1.0,
            "learning_curve": [2.0, 1.0],
        }

    monkeypatch.setattr(kaggle_playground, "_train_cached_mlp", train_with_nan)

    with pytest.raises(ValueError) as exc_info:
        build_task_cache(
            spec=spec,
            train_csv=train_csv,
            output_path=output_path,
            configs_per_task=1,
            epochs_per_config=2,
            split_seed=123,
            config_seed=456,
        )

    message = str(exc_info.value)
    assert "config_id=0" in message
    assert "val_score" in message
    assert not output_path.exists()
