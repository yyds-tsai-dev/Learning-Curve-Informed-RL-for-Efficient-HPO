from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from hpo_baselines.kaggle_playground import load_manifest, nested_task_slugs

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
