from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (project_root := str(PROJECT_ROOT)) not in sys.path:
    sys.path.insert(0, project_root)

from hpo_baselines import (  # noqa: E402
    BaselineEvaluator,
    BayesianOptimization,
    CrossDatasetEvaluator,
    CrossDatasetHyperRLOptimizer,
    CrossDatasetLCDQNOptimizer,
    HyperRLOptimizer,
    LCBenchTask,
    LearningCurveDQNOptimizer,
    RandomSearch,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run LCBench HPO baselines.")
    parser.add_argument(
        "--data-path",
        type=Path,
        default=PROJECT_ROOT / "data" / "tiny_lcbench.json",
        help="Path to the official LCBench JSON file or the tiny fixture.",
    )
    parser.add_argument(
        "--dataset", type=str, default=None, help="Single LCBench dataset name."
    )
    parser.add_argument(
        "--datasets",
        type=str,
        default=None,
        help=(
            "Comma-separated LCBench dataset names, or 'all' for all datasets. "
            "Overrides --dataset."
        ),
    )
    parser.add_argument(
        "--budget", type=int, default=4, help="HPO evaluations per method/seed."
    )
    parser.add_argument(
        "--seeds", type=int, default=3, help="Number of repeated random seeds."
    )
    parser.add_argument(
        "--limit-configs",
        type=int,
        default=None,
        help="Optional cap for fast debugging.",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=PROJECT_ROOT / "results" / "lcbench"
    )
    parser.add_argument(
        "--cross-dataset",
        action="store_true",
        help="Use cross-dataset training mode (weight inheritance across datasets).",
    )
    parser.add_argument(
        "--total-episodes",
        type=int,
        default=50,
        help="Total episodes for cross-dataset training (ignored in single-task mode).",
    )
    args = parser.parse_args()

    data = json.loads(args.data_path.read_text(encoding="utf-8"))
    if args.datasets:
        if args.datasets.strip().lower() == "all":
            dataset_names = sorted(data.keys())
        else:
            dataset_names = [
                name.strip() for name in args.datasets.split(",") if name.strip()
            ]
    elif args.dataset:
        dataset_names = [args.dataset]
    else:
        dataset_names = sorted(data.keys())
    tasks = [
        LCBenchTask(
            data_path=args.data_path,
            dataset_name=dataset_name,
            limit_configs=args.limit_configs,
            data=data,
        )
        for dataset_name in dataset_names
    ]
    dqn_kwargs = {
        "hidden_sizes": (64, 64),
        "batch_size": min(4, args.budget),
        "learning_starts": min(2, args.budget),
        "target_update_freq": 4,
    }

    # Choose evaluation mode based on --cross-dataset flag
    if args.cross_dataset:
        # Cross-dataset mode: single network shared across all datasets
        print(f"\n{'=' * 60}")
        print("CROSS-DATASET TRAINING MODE")
        print("Single DQN network with weight inheritance across datasets")
        print(f"Total episodes: {args.total_episodes}")
        print(f"{'=' * 60}\n")

        evaluator = CrossDatasetEvaluator(
            tasks=tasks,
            methods=[
                CrossDatasetHyperRLOptimizer(
                    **dqn_kwargs,
                    total_episodes=args.total_episodes,
                    episode_budget=args.budget,
                ),
                CrossDatasetLCDQNOptimizer(
                    **dqn_kwargs,
                    total_episodes=args.total_episodes,
                    episode_budget=args.budget,
                ),
            ],
            total_episodes=args.total_episodes,
            seeds=list(range(args.seeds)),
        )
        output_subdir = args.output_dir / "cross_dataset"
    else:
        # Single-task mode: each task trained independently
        print(f"\n{'=' * 60}")
        print("SINGLE-TASK BASELINE MODE")
        print("Each task trained independently (no weight sharing)")
        print(f"Budget per task: {args.budget}")
        print(f"{'=' * 60}\n")

        evaluator = BaselineEvaluator(
            tasks=tasks,
            methods=[
                RandomSearch(),
                BayesianOptimization(initial_points=min(3, args.budget)),
                HyperRLOptimizer(**dqn_kwargs),
                LearningCurveDQNOptimizer(**dqn_kwargs),
            ],
            budget=args.budget,
            seeds=list(range(args.seeds)),
        )
        output_subdir = args.output_dir / "single_task"

    traces = evaluator.run()
    evaluator.save(traces, output_subdir)

    print("LCBench Evaluation Summary")
    print(
        "task,method,runs,val_score_mean,val_score_std,test_score_mean,simple_regret_mean"
    )
    for row in evaluator.summarize(traces):
        print(
            f"{row['task']},{row['method']},{row['runs']},"
            f"{row['best_val_score_mean']:.4f},{row['best_val_score_std']:.4f},"
            f"{row['best_test_score_mean']:.4f},{row['simple_regret_mean']:.4f}"
        )

    print(f"\nSaved results to {output_subdir}")

    if args.cross_dataset:
        print("\nCross-dataset insights:")
        print("  ✓ Single DQN network shared across datasets")
        print("  ✓ Weights inherited between episodes (transfer learning)")
        print("  ✓ Meta-features initialize LSTM hidden state")
        print("  ✓ Random dataset sampling during training")
    else:
        print("\nSingle-task baseline insights:")
        print("  ✓ Each dataset trained independently")
        print("  ✓ Network reinitialized for each task")
        print("  ✓ No weight sharing between datasets")


if __name__ == "__main__":
    main()
