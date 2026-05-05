from __future__ import annotations

import csv
import json
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from statistics import mean, stdev
from typing import Any

from tqdm import tqdm

from .optimizers import BaseOptimizer, OptimizationTrace

type Row = dict[str, Any]


@dataclass(slots=True)
class BaselineEvaluator:
    """Run HPO methods on one or more tasks and aggregate baseline statistics."""

    tasks: list[Any]
    methods: list[BaseOptimizer]
    budget: int = 20
    seeds: list[int] | None = None

    def __post_init__(self) -> None:
        self.seeds = self.seeds or [0, 1, 2, 3, 4]

    def run(self) -> list[OptimizationTrace]:
        traces: list[OptimizationTrace] = []
        total_runs = len(self.tasks) * len(self.seeds) * len(self.methods)

        with tqdm(total=total_runs, desc="Baseline evaluation", unit="run") as pbar:
            for task in self.tasks:
                for seed in self.seeds:
                    for method in self.methods:
                        traces.append(
                            method.optimize(task, budget=self.budget, seed=seed)
                        )
                        pbar.update(1)
        return traces

    def summarize(self, traces: list[OptimizationTrace]) -> list[Row]:
        oracle_by_task_seed: dict[tuple[str, int], float] = {}
        for trace in traces:
            key = (trace.task, trace.seed)
            best_seen = min(record.val_score for record in trace.evaluations)
            oracle_by_task_seed[key] = min(
                oracle_by_task_seed.get(key, best_seen), best_seen
            )

        runs: list[Row] = []
        for trace in traces:
            best = trace.best_record
            oracle = oracle_by_task_seed[(trace.task, trace.seed)]
            runs.append(
                {
                    "task": trace.task,
                    "method": trace.method,
                    "seed": trace.seed,
                    "best_val_score": best.val_score,
                    "best_test_score": best.test_score,
                    "simple_regret": best.val_score - oracle,
                    "best_iteration": best.iteration,
                }
            )

        grouped: dict[tuple[str, str], list[Row]] = defaultdict(list)
        for row in runs:
            grouped[(row["task"], row["method"])].append(row)

        summary: list[Row] = []
        for (task, method), rows in sorted(grouped.items()):
            summary.append(
                {
                    "task": task,
                    "method": method,
                    "runs": len(rows),
                    "best_val_score_mean": _mean(rows, "best_val_score"),
                    "best_val_score_std": _std(rows, "best_val_score"),
                    "best_test_score_mean": _mean(rows, "best_test_score"),
                    "best_test_score_std": _std(rows, "best_test_score"),
                    "simple_regret_mean": _mean(rows, "simple_regret"),
                    "simple_regret_std": _std(rows, "simple_regret"),
                    "best_iteration_mean": _mean(rows, "best_iteration"),
                }
            )
        return summary

    def save(self, traces: list[OptimizationTrace], output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        serializable = [
            {
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
            for trace in traces
        ]
        (output_dir / "traces.json").write_text(
            json.dumps(serializable, indent=2), encoding="utf-8"
        )

        summary = self.summarize(traces)
        with (output_dir / "summary.csv").open(
            "w", newline="", encoding="utf-8"
        ) as handle:
            if summary:
                writer = csv.DictWriter(handle, fieldnames=list(summary[0].keys()))
                writer.writeheader()
                writer.writerows(summary)
        _save_budget_performance_outputs(traces, output_dir)
        pairwise = self.pairwise_comparisons(traces)
        with (output_dir / "pairwise_comparisons.csv").open(
            "w", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
                    "task",
                    "method_a",
                    "method_b",
                    "mean_delta_a_minus_b",
                    "std_delta",
                    "wins_a",
                    "wins_b",
                    "ties",
                    "runs",
                ],
            )
            writer.writeheader()
            writer.writerows(pairwise)
        (output_dir / "conclusion.md").write_text(
            self.conclusion(summary), encoding="utf-8"
        )

    @staticmethod
    def pairwise_comparisons(traces: list[OptimizationTrace]) -> list[Row]:
        by_task_seed_method: dict[tuple[str, int, str], float] = {}
        methods_by_task: dict[str, set[str]] = defaultdict(set)
        seeds_by_task: dict[str, set[int]] = defaultdict(set)
        for trace in traces:
            by_task_seed_method[(trace.task, trace.seed, trace.method)] = (
                trace.best_record.val_score
            )
            methods_by_task[trace.task].add(trace.method)
            seeds_by_task[trace.task].add(trace.seed)

        rows: list[Row] = []
        for task in sorted(methods_by_task):
            methods = sorted(methods_by_task[task])
            seeds = sorted(seeds_by_task[task])
            for method_a, method_b in combinations(methods, 2):
                deltas: list[float] = []
                wins_a = 0
                wins_b = 0
                ties = 0
                for seed in seeds:
                    score_a = by_task_seed_method[(task, seed, method_a)]
                    score_b = by_task_seed_method[(task, seed, method_b)]
                    delta = score_a - score_b
                    deltas.append(delta)
                    if abs(delta) < 1e-12:
                        ties += 1
                    elif delta < 0:
                        wins_a += 1
                    else:
                        wins_b += 1
                rows.append(
                    {
                        "task": task,
                        "method_a": method_a,
                        "method_b": method_b,
                        "mean_delta_a_minus_b": float(mean(deltas)),
                        "std_delta": float(stdev(deltas)) if len(deltas) > 1 else 0.0,
                        "wins_a": wins_a,
                        "wins_b": wins_b,
                        "ties": ties,
                        "runs": len(deltas),
                    }
                )
        return rows

    @staticmethod
    def conclusion(summary: list[Row]) -> str:
        if not summary:
            return "# Baseline Evaluation Conclusion\n\nNo completed evaluations were recorded.\n"
        lines = ["# Baseline Evaluation Conclusion", ""]
        lines.append(
            "Lower validation score and lower simple regret are better. The oracle for simple regret is "
            "the best validation score observed by any compared method under the same task and seed."
        )
        grouped: dict[str, list[Row]] = defaultdict(list)
        by_method: dict[str, list[Row]] = defaultdict(list)
        for row in summary:
            grouped[row["task"]].append(row)
            by_method[row["method"]].append(row)

        overall = []
        for method, rows in by_method.items():
            overall.append(
                {
                    "method": method,
                    "tasks": len(rows),
                    "avg_simple_regret": mean(
                        row["simple_regret_mean"] for row in rows
                    ),
                    "avg_rank": mean(
                        1
                        + sorted(
                            grouped[row["task"]],
                            key=lambda item: item["best_val_score_mean"],
                        ).index(row)
                        for row in rows
                    ),
                }
            )
        overall = sorted(
            overall, key=lambda row: (row["avg_simple_regret"], row["avg_rank"])
        )
        lines.append("")
        lines.append("## Overall")
        lines.append("")
        lines.append(
            "| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |"
        )
        lines.append("| --- | --- | ---: | ---: | ---: |")
        for idx, row in enumerate(overall, start=1):
            lines.append(
                f"| {idx} | {row['method']} | {row['avg_simple_regret']:.4f} | "
                f"{row['avg_rank']:.2f} | {row['tasks']} |"
            )

        rank1_counts: dict[str, int] = {method: 0 for method in by_method}
        for rows in grouped.values():
            best_val = min(row["best_val_score_mean"] for row in rows)
            for row in rows:
                if abs(row["best_val_score_mean"] - best_val) < 1e-12:
                    rank1_counts[row["method"]] += 1

        rank1_sorted = sorted(
            rank1_counts.items(), key=lambda item: (-item[1], item[0])
        )
        best_rank1 = rank1_sorted[0][1]
        best_rank1_methods = [
            method for method, count in rank1_sorted if count == best_rank1
        ]

        lines.append("")
        lines.append("## Rank-1 Counts")
        lines.append("")
        lines.append("| Method | Rank-1 task count |")
        lines.append("| --- | ---: |")
        for method, count in rank1_sorted:
            lines.append(f"| {method} | {count} |")

        rank1_leader_text = ", ".join(f"**{method}**" for method in best_rank1_methods)
        lines.append("")
        lines.append(
            f"Most rank-1 finishes: {rank1_leader_text} with {best_rank1} task(s)."
        )

        winner = overall[0]
        lines.append("")
        lines.append(
            f"Across the selected tasks, **{winner['method']}** gives the best average simple regret "
            f"({winner['avg_simple_regret']:.4f}). "
            "Random Search is the sanity-check lower bound, Bayesian Optimization tests "
            "sample-efficient surrogate modeling, HyperRL-DQN tests the paper-style DQN setup "
            "with a configurable sequence encoder (default: LSTM), and OurMethod-LC-DQN adds "
            "learning-curve and derivative state features."
        )

        lines.append("")
        lines.append("## Per-Task Rankings")

        for task, rows in sorted(grouped.items()):
            lines.append("")
            lines.append(f"### {task}")
            lines.append("")
            lines.append(
                "| Rank | Method | Val score mean | Test score mean | Simple regret mean |"
            )
            lines.append("| --- | --- | ---: | ---: | ---: |")
            for idx, row in enumerate(
                sorted(rows, key=lambda item: item["best_val_score_mean"]), start=1
            ):
                lines.append(
                    f"| {idx} | {row['method']} | {row['best_val_score_mean']:.4f} | "
                    f"{row['best_test_score_mean']:.4f} | {row['simple_regret_mean']:.4f} |"
                )
        return "\n".join(lines) + "\n"


def _mean(rows: list[Row], key: str) -> float:
    return float(mean(float(row[key]) for row in rows))


def _std(rows: list[Row], key: str) -> float:
    if len(rows) <= 1:
        return 0.0
    return float(stdev(float(row[key]) for row in rows))


def _save_budget_performance_outputs(
    traces: list[OptimizationTrace], output_dir: Path
) -> None:
    eval_budget_rows = _performance_rows(traces, x_key="eval_budget")
    _write_performance_csv(
        eval_budget_rows,
        output_dir / "performance_vs_eval_budget.csv",
        x_key="eval_budget",
    )
    if eval_budget_rows:
        _write_budget_performance_plot(
            eval_budget_rows,
            output_dir / "performance_vs_eval_budget.png",
            x_key="eval_budget",
            x_label="Evaluation budget",
            title="Normalized Simple Regret vs. Evaluation Budget",
            log_x=False,
        )

    total_eval_rows = _performance_rows(traces, x_key="total_consumed_evals")
    _write_performance_csv(
        total_eval_rows,
        output_dir / "performance_vs_total_consumed_evals.csv",
        x_key="total_consumed_evals",
    )
    if total_eval_rows:
        _write_budget_performance_plot(
            total_eval_rows,
            output_dir / "performance_vs_total_consumed_evals.png",
            x_key="total_consumed_evals",
            x_label="Total consumed evaluations",
            title="Normalized Simple Regret vs. Total Consumed Evaluations",
            log_x=True,
        )


def _write_performance_csv(rows: list[Row], output_path: Path, x_key: str) -> None:
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                x_key,
                "method",
                "runs",
                "normalized_simple_regret_mean",
                "normalized_simple_regret_std",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def _performance_rows(traces: list[OptimizationTrace], x_key: str) -> list[Row]:
    normalizers = _normalizers_by_task_seed(traces)
    by_method_x: dict[tuple[str, int], list[float]] = defaultdict(list)
    for trace in traces:
        best_seen = float("inf")
        oracle, denom = normalizers[(trace.task, trace.seed)]
        train_cost = _meta_training_cost(trace)
        for record in sorted(trace.evaluations, key=lambda item: item.iteration):
            best_seen = min(best_seen, float(record.val_score))
            eval_budget = int(record.iteration) + 1
            x_value = (
                train_cost + eval_budget
                if x_key == "total_consumed_evals"
                else eval_budget
            )
            normalized_simple_regret = (best_seen - oracle) / denom
            by_method_x[(trace.method, x_value)].append(normalized_simple_regret)

    rows: list[Row] = []
    for (method, x_value), values in sorted(
        by_method_x.items(), key=lambda item: (item[0][1], item[0][0])
    ):
        rows.append(
            {
                x_key: x_value,
                "method": method,
                "runs": len(values),
                "normalized_simple_regret_mean": float(mean(values)),
                "normalized_simple_regret_std": (
                    float(stdev(values)) if len(values) > 1 else 0.0
                ),
            }
        )
    return rows


def _normalizers_by_task_seed(
    traces: list[OptimizationTrace],
) -> dict[tuple[str, int], tuple[float, float]]:
    values_by_task_seed: dict[tuple[str, int], list[float]] = defaultdict(list)
    for trace in traces:
        values_by_task_seed[(trace.task, trace.seed)].extend(
            float(record.val_score) for record in trace.evaluations
        )

    normalizers: dict[tuple[str, int], tuple[float, float]] = {}
    for key, values in values_by_task_seed.items():
        oracle = min(values)
        worst = max(values)
        normalizers[key] = (oracle, max(worst - oracle, 1e-12))
    return normalizers


def _meta_training_cost(trace: OptimizationTrace) -> int:
    if not trace.evaluations:
        return 0
    extra = trace.evaluations[0].extra
    total_episodes = extra.get("train_total_episodes")
    episode_budget = extra.get("train_episode_budget")
    if total_episodes is None or episode_budget is None:
        return 0
    return int(total_episodes) * int(episode_budget)


def _write_budget_performance_plot(
    rows: list[Row],
    output_path: Path,
    x_key: str,
    x_label: str,
    title: str,
    log_x: bool,
) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    series: dict[str, list[tuple[int, float]]] = defaultdict(list)
    series_std: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for row in rows:
        method = str(row["method"])
        x_value = int(row[x_key])
        series[method].append(
            (x_value, float(row["normalized_simple_regret_mean"]))
        )
        series_std[method].append(
            (x_value, float(row["normalized_simple_regret_std"]))
        )

    fig, ax = plt.subplots(figsize=(10, 6), dpi=180)
    for method in sorted(series):
        points = sorted(series[method])
        std_points = dict(series_std[method])
        xs = [budget for budget, _ in points]
        ys = [score for _, score in points]
        yerr = [std_points[budget] for budget in xs]
        line = ax.plot(xs, ys, marker="o", linewidth=2.0, markersize=4, label=method)
        color = line[0].get_color()
        if any(value > 0 for value in yerr):
            lower = [score - err for score, err in zip(ys, yerr, strict=True)]
            upper = [score + err for score, err in zip(ys, yerr, strict=True)]
            ax.fill_between(xs, lower, upper, color=color, alpha=0.14, linewidth=0)

    if log_x and min(x for points in series.values() for x, _ in points) > 0:
        ax.set_xscale("log")
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel("Per-task normalized simple regret (lower is better)")
    ax.grid(True, which="major", alpha=0.3)
    ax.legend(loc="best", frameon=True)
    ax.margins(x=0.02)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


@dataclass(slots=True)
class CrossDatasetEvaluator:
    """Evaluate cross-dataset DQN methods using shared weight inheritance.

    Unlike BaselineEvaluator which trains each method on each task independently,
    this evaluator trains a single DQN network across multiple tasks with weight
    persistence (meta-learning). The network is randomly assigned tasks during
    training episodes.

    This implements the Hyp-RL evaluation protocol where:
    - A single DQN network is trained across all tasks
    - Weights are inherited/shared across tasks
    - Meta-features condition the policy for task-awareness
    """

    tasks: list[Any]
    methods: list[BaseOptimizer]
    total_episodes: int = 150  # Total cross-dataset meta-training episodes to run
    evaluation_budget: int = 20  # Fixed per-task budget for final evaluation
    seeds: list[int] | None = None

    def __post_init__(self) -> None:
        self.seeds = self.seeds or [0, 1, 2, 3, 4]

    def run(self) -> list[OptimizationTrace]:
        """Run cross-dataset evaluation.

        Returns:
            Flattened list of OptimizationTrace objects from all methods and seeds
        """
        traces: list[OptimizationTrace] = []
        total_runs = len(self.seeds) * sum(
            1 if method.supports_cross_dataset else len(self.tasks)
            for method in self.methods
        )

        with tqdm(
            total=total_runs, desc="Cross-dataset evaluation", unit="run"
        ) as pbar:
            for seed in self.seeds:
                for method in self.methods:
                    if method.supports_cross_dataset:
                        # Method returns list of traces (cross-dataset style)
                        method_traces = method.optimize(
                            self.tasks,
                            self.total_episodes,
                            seed,
                            self.evaluation_budget,
                        )
                        traces.extend(method_traces)
                        pbar.update(1)
                    else:
                        # Non-meta baselines are evaluated independently with the
                        # same fixed evaluation budget used by the frozen DQN.
                        for task in self.tasks:
                            traces.append(
                                method.optimize(task, self.evaluation_budget, seed)
                            )
                            pbar.update(1)
        return traces

    def summarize(self, traces: list[OptimizationTrace]) -> list[Row]:
        """Summarize evaluation results (compatible with BaselineEvaluator)."""
        oracle_by_task_seed: dict[tuple[str, int], float] = {}
        for trace in traces:
            key = (trace.task, trace.seed)
            best_seen = min(record.val_score for record in trace.evaluations)
            oracle_by_task_seed[key] = min(
                oracle_by_task_seed.get(key, best_seen), best_seen
            )

        runs: list[Row] = []
        for trace in traces:
            best = trace.best_record
            oracle = oracle_by_task_seed[(trace.task, trace.seed)]
            runs.append(
                {
                    "task": trace.task,
                    "method": trace.method,
                    "seed": trace.seed,
                    "best_val_score": best.val_score,
                    "best_test_score": best.test_score,
                    "simple_regret": best.val_score - oracle,
                    "best_iteration": best.iteration,
                }
            )

        grouped: dict[tuple[str, str], list[Row]] = defaultdict(list)
        for row in runs:
            grouped[(row["task"], row["method"])].append(row)

        summary: list[Row] = []
        for (task, method), rows in sorted(grouped.items()):
            summary.append(
                {
                    "task": task,
                    "method": method,
                    "runs": len(rows),
                    "best_val_score_mean": _mean(rows, "best_val_score"),
                    "best_val_score_std": _std(rows, "best_val_score"),
                    "best_test_score_mean": _mean(rows, "best_test_score"),
                    "best_test_score_std": _std(rows, "best_test_score"),
                    "simple_regret_mean": _mean(rows, "simple_regret"),
                    "simple_regret_std": _std(rows, "simple_regret"),
                    "best_iteration_mean": _mean(rows, "best_iteration"),
                }
            )
        return summary

    def save(self, traces: list[OptimizationTrace], output_dir: Path) -> None:
        """Save evaluation results."""
        output_dir.mkdir(parents=True, exist_ok=True)
        serializable = [
            {
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
            for trace in traces
        ]
        (output_dir / "traces.json").write_text(
            json.dumps(serializable, indent=2), encoding="utf-8"
        )

        summary = self.summarize(traces)
        with (output_dir / "summary.csv").open(
            "w", newline="", encoding="utf-8"
        ) as handle:
            if summary:
                writer = csv.DictWriter(handle, fieldnames=list(summary[0].keys()))
                writer.writeheader()
                writer.writerows(summary)
        _save_budget_performance_outputs(traces, output_dir)
        (output_dir / "conclusion.md").write_text(
            BaselineEvaluator.conclusion(summary), encoding="utf-8"
        )
