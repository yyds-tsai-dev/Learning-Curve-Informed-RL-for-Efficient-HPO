from __future__ import annotations

import argparse
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from hpo_baselines.kaggle_playground import build_task_cache, load_manifest


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build Kaggle Playground MLP learning-curve caches."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("data/kaggle_playground/manifest.json"),
    )
    parser.add_argument("--raw-dir", type=Path, default=Path("data/kaggle_playground/raw"))
    parser.add_argument(
        "--cache-dir", type=Path, default=Path("data/kaggle_playground/cache")
    )
    parser.add_argument(
        "--tasks",
        nargs="*",
        help=(
            "Task slugs to build, or 'all'. Defaults to all manifest tasks in "
            "nested order."
        ),
    )
    parser.add_argument("--configs-per-task", type=int)
    parser.add_argument("--epochs-per-config", type=int)
    parser.add_argument("--config-seed", type=int, default=20260601)
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    task_by_slug = manifest.by_slug
    task_slugs = (
        list(manifest.nested_order)
        if not args.tasks or args.tasks == ["all"]
        else args.tasks
    )
    configs_per_task = args.configs_per_task or manifest.cache.configs_per_task
    epochs_per_config = args.epochs_per_config or manifest.cache.epochs_per_config

    for slug in task_slugs:
        if slug not in task_by_slug:
            raise ValueError(f"Unknown Kaggle task slug: {slug}")
        spec = task_by_slug[slug]
        build_task_cache(
            spec=spec,
            train_csv=args.raw_dir / slug / "train.csv",
            output_path=args.cache_dir / f"{slug}.json",
            configs_per_task=configs_per_task,
            epochs_per_config=epochs_per_config,
            split_seed=manifest.cache.split_seed,
            config_seed=args.config_seed,
        )


if __name__ == "__main__":
    main()
