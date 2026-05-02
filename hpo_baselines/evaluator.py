from __future__ import annotations

import csv
import json
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from statistics import mean, stdev
from typing import Any

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
        for task in self.tasks:
            for seed in self.seeds:
                for method in self.methods:
                    traces.append(method.optimize(task, budget=self.budget, seed=seed))
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

        for task, rows in sorted(grouped.items()):
            lines.append("")
            lines.append(f"## {task}")
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
            "sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup "
            "with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative "
            "state features."
        )
        return "\n".join(lines) + "\n"


def _mean(rows: list[Row], key: str) -> float:
    return float(mean(float(row[key]) for row in rows))


def _std(rows: list[Row], key: str) -> float:
    if len(rows) <= 1:
        return 0.0
    return float(stdev(float(row[key]) for row in rows))
