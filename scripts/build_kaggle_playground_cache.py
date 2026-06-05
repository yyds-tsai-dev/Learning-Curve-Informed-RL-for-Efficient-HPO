from __future__ import annotations

import argparse
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from hpo_baselines.kaggle_playground import build_task_cache, load_manifest


def positive_int(raw_value: str) -> int:
    value = int(raw_value)
    if value <= 0:
        raise argparse.ArgumentTypeError("value must be positive")
    return value


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
    parser.add_argument("--configs-per-task", type=positive_int)
    parser.add_argument("--epochs-per-config", type=positive_int)
    parser.add_argument("--max-train-rows", type=positive_int)
    parser.add_argument("--max-categories-per-column", type=positive_int)
    parser.add_argument("--config-seed", type=int, default=20260601)
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    task_by_slug = manifest.by_slug
    task_slugs = (
        list(manifest.nested_order)
        if not args.tasks or args.tasks == ["all"]
        else args.tasks
    )
    configs_per_task = (
        manifest.cache.configs_per_task
        if args.configs_per_task is None
        else args.configs_per_task
    )
    epochs_per_config = (
        manifest.cache.epochs_per_config
        if args.epochs_per_config is None
        else args.epochs_per_config
    )
    max_train_rows = (
        manifest.cache.max_train_rows
        if args.max_train_rows is None
        else args.max_train_rows
    )
    max_categories_per_column = (
        manifest.cache.max_categories_per_column
        if args.max_categories_per_column is None
        else args.max_categories_per_column
    )

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
            max_train_rows=max_train_rows,
            max_categories_per_column=max_categories_per_column,
        )


if __name__ == "__main__":
    main()
