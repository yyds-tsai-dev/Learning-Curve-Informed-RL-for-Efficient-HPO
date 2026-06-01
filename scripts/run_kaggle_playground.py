from __future__ import annotations

import argparse
import csv
import json
from math import sqrt
from statistics import mean, stdev
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
from hpo_baselines.optimizers import OptimizationTrace


def _tasks_by_slug(
    cache_dir: Path, manifest_path: Path
) -> dict[str, KaggleRegressionTask]:
    manifest = load_manifest(manifest_path)
    return {
        spec.slug: KaggleRegressionTask(cache_dir / f"{spec.slug}.json")
        for spec in manifest.tasks
    }


def _normalized_best_regret(trace: OptimizationTrace) -> float:
    best = trace.best_record
    normalizer = best.extra.get("normalizer")
    if isinstance(normalizer, dict):
        try:
            oracle = float(normalizer["oracle_val_score"])
            reference = float(normalizer["reference_worst_val_score"])
            denom = reference - oracle
            if denom > 0:
                return float((best.val_score - oracle) / (denom + 1e-8))
        except (KeyError, TypeError, ValueError):
            pass
    return float(best.val_score)


def _write_task_count_outputs(
    traces_by_count: dict[int, list[OptimizationTrace]], output_dir: Path
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    combined = []
    for count, traces in sorted(traces_by_count.items()):
        completed = [trace for trace in traces if trace.evaluations]
        values = [_normalized_best_regret(trace) for trace in completed]
        if not values:
            continue
        std = float(stdev(values)) if len(values) > 1 else 0.0
        rows.append(
            {
                "train_task_count": count,
                "method": "CrossDataset-LC-DQN",
                "runs": len(values),
                "normalized_simple_regret_mean": float(mean(values)),
                "normalized_simple_regret_std": std,
                "normalized_simple_regret_se": std / sqrt(len(values)),
            }
        )
        for trace in traces:
            combined.append(_trace_payload(trace, train_task_count=count))

    (output_dir / "traces.json").write_text(
        json.dumps(combined, indent=2), encoding="utf-8"
    )
    _write_task_count_csv(output_dir / "summary_by_task_count.csv", rows)
    _write_task_count_csv(
        output_dir / "normalized_simple_regret_by_task_count.csv", rows
    )
    if rows:
        _write_task_count_plot(
            rows, output_dir / "normalized_simple_regret_by_task_count.png"
        )
    (output_dir / "conclusion.md").write_text(
        _task_count_conclusion(rows), encoding="utf-8"
    )


def _write_task_count_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fieldnames = [
        "train_task_count",
        "method",
        "runs",
        "normalized_simple_regret_mean",
        "normalized_simple_regret_std",
        "normalized_simple_regret_se",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_task_count_plot(rows: list[dict[str, object]], output_path: Path) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    sorted_rows = sorted(rows, key=lambda row: int(row["train_task_count"]))
    xs = [int(row["train_task_count"]) for row in sorted_rows]
    ys = [float(row["normalized_simple_regret_mean"]) for row in sorted_rows]
    yerr = [float(row["normalized_simple_regret_se"]) for row in sorted_rows]
    fig, ax = plt.subplots(figsize=(8, 5), dpi=180)
    ax.errorbar(xs, ys, yerr=yerr, marker="o", linewidth=2.0, capsize=3)
    ax.set_xlabel("Meta-training task count")
    ax.set_ylabel("Normalized simple regret (lower is better)")
    ax.set_title("LC-DQN Transfer vs. Number of Training Tasks")
    ax.set_xticks(xs)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def _task_count_conclusion(rows: list[dict[str, object]]) -> str:
    if not rows:
        return "# LC-DQN Task-Count Sweep\n\nNo completed evaluations were recorded.\n"
    sorted_rows = sorted(rows, key=lambda row: int(row["train_task_count"]))
    best = min(sorted_rows, key=lambda row: float(row["normalized_simple_regret_mean"]))
    means = [float(row["normalized_simple_regret_mean"]) for row in sorted_rows]
    non_increasing = all(
        later <= earlier + 1e-12 for earlier, later in zip(means, means[1:])
    )
    lines = [
        "# LC-DQN Task-Count Sweep",
        "",
        (
            "Lower normalized simple regret is better. The best mean score is "
            f"at {int(best['train_task_count'])} training task(s): "
            f"{float(best['normalized_simple_regret_mean']):.4f}."
        ),
        "",
        (
            "The curve is monotonic non-increasing across the tested task counts."
            if non_increasing
            else "The curve is not monotonic across the tested task counts."
        ),
        "",
        "| Train tasks | Runs | Mean | Std | SE |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in sorted_rows:
        lines.append(
            f"| {int(row['train_task_count'])} | {int(row['runs'])} | "
            f"{float(row['normalized_simple_regret_mean']):.4f} | "
            f"{float(row['normalized_simple_regret_std']):.4f} | "
            f"{float(row['normalized_simple_regret_se']):.4f} |"
        )
    return "\n".join(lines) + "\n"


def _trace_payload(
    trace: OptimizationTrace, train_task_count: int | None = None
) -> dict[str, object]:
    payload: dict[str, object] = {
        "task": trace.task,
        "method": trace.method,
        "seed": trace.seed,
        "evaluations": [
            {
                "iteration": record.iteration,
                "config": record.config,
                "val_score": record.val_score,
                "test_score": record.test_score,
                "learning_curve": record.learning_curve,
                "extra": record.extra,
            }
            for record in trace.evaluations
        ],
    }
    if train_task_count is not None:
        payload["train_task_count"] = train_task_count
    return payload


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

    traces_by_count: dict[int, list[OptimizationTrace]] = {}
    task_count_dir = args.output_dir / "lcdqn_task_count"
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
        for trace in traces:
            for record in trace.evaluations:
                record.extra["train_task_count"] = count
        traces_by_count[count] = traces
        evaluator.save(traces, task_count_dir / f"train_{count}")
    _write_task_count_outputs(traces_by_count, task_count_dir)


if __name__ == "__main__":
    main()
