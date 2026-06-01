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


def _tasks_by_slug(
    cache_dir: Path, manifest_path: Path
) -> dict[str, KaggleRegressionTask]:
    manifest = load_manifest(manifest_path)
    return {
        spec.slug: KaggleRegressionTask(cache_dir / f"{spec.slug}.json")
        for spec in manifest.tasks
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run Kaggle Playground HPO experiments."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=PROJECT_ROOT / "data" / "kaggle_playground" / "manifest.json",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=PROJECT_ROOT / "data" / "kaggle_playground" / "cache",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "results" / "kaggle_playground",
    )
    parser.add_argument(
        "--suite",
        choices=("all-methods", "lcdqn-task-count"),
        default="all-methods",
    )
    parser.add_argument("--budget", type=int, default=20)
    parser.add_argument("--seeds", type=int, default=5)
    parser.add_argument("--total-episodes", type=int, default=150)
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    by_slug = _tasks_by_slug(args.cache_dir, args.manifest)
    all_tasks = [by_slug[slug] for slug in manifest.nested_order]
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
        return

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
        evaluator.save(
            traces,
            args.output_dir / "lcdqn_task_count" / f"train_{count}",
        )


if __name__ == "__main__":
    main()
