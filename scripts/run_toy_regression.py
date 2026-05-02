from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (project_root := str(PROJECT_ROOT)) not in sys.path:
    sys.path.insert(0, project_root)

from hpo_baselines import (  # noqa: E402
    BaselineEvaluator,
    BayesianOptimization,
    HyperRLOptimizer,
    RandomSearch,
    SyntheticRegressionTask,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run toy regression HPO baselines.")
    parser.add_argument(
        "--budget", type=int, default=20, help="HPO evaluations per method/seed."
    )
    parser.add_argument(
        "--seeds", type=int, default=5, help="Number of repeated random seeds."
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("results/toy_regression")
    )
    args = parser.parse_args()

    task = SyntheticRegressionTask()
    evaluator = BaselineEvaluator(
        tasks=[task],
        methods=[
            RandomSearch(),
            BayesianOptimization(),
            HyperRLOptimizer(),
        ],
        budget=args.budget,
        seeds=list(range(args.seeds)),
    )
    traces = evaluator.run()
    evaluator.save(traces, args.output_dir)

    summary = evaluator.summarize(traces)
    print("Baseline Evaluation Summary")
    print(
        "task,method,runs,val_score_mean,val_score_std,test_score_mean,simple_regret_mean"
    )
    for row in summary:
        print(
            f"{row['task']},{row['method']},{row['runs']},"
            f"{row['best_val_score_mean']:.4f},{row['best_val_score_std']:.4f},"
            f"{row['best_test_score_mean']:.4f},{row['simple_regret_mean']:.4f}"
        )
    print(f"\nSaved traces, summary, and conclusion to {args.output_dir}")


if __name__ == "__main__":
    main()
