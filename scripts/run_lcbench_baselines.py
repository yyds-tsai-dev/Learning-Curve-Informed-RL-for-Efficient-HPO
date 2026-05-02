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
    traces = evaluator.run()
    evaluator.save(traces, args.output_dir)

    print("LCBench Baseline Evaluation Summary")
    print(
        "task,method,runs,val_score_mean,val_score_std,test_score_mean,simple_regret_mean"
    )
    for row in evaluator.summarize(traces):
        print(
            f"{row['task']},{row['method']},{row['runs']},"
            f"{row['best_val_score_mean']:.4f},{row['best_val_score_std']:.4f},"
            f"{row['best_test_score_mean']:.4f},{row['simple_regret_mean']:.4f}"
        )
    print(
        f"\nSaved traces, summary, pairwise comparisons, and conclusion to {args.output_dir}"
    )


if __name__ == "__main__":
    main()
