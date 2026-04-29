from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev
from typing import Any

from .optimizers import BaseOptimizer, OptimizationTrace


class BaselineEvaluator:
    """Run HPO methods on one or more tasks and aggregate baseline statistics."""

    def __init__(
        self,
        tasks: list[Any],
        methods: list[BaseOptimizer],
        budget: int = 20,
        seeds: list[int] | None = None,
    ) -> None:
        self.tasks = tasks
        self.methods = methods
        self.budget = budget
        self.seeds = seeds or [0, 1, 2, 3, 4]

    def run(self) -> list[OptimizationTrace]:
        traces: list[OptimizationTrace] = []
        for task in self.tasks:
            for seed in self.seeds:
                for method in self.methods:
                    traces.append(method.optimize(task, budget=self.budget, seed=seed))
        return traces

    def summarize(self, traces: list[OptimizationTrace]) -> list[dict[str, Any]]:
        oracle_by_task_seed: dict[tuple[str, int], float] = {}
        for trace in traces:
            key = (trace.task, trace.seed)
            best_seen = min(record.val_score for record in trace.evaluations)
            oracle_by_task_seed[key] = min(oracle_by_task_seed.get(key, best_seen), best_seen)

        runs: list[dict[str, Any]] = []
        for trace in traces:
            best = trace.best_record
            oracle = oracle_by_task_seed[(trace.task, trace.seed)]
            runs.append(
                {
                    "task": trace.task,
                    "method": trace.method,
                    "seed": trace.seed,
                    "best_val_rmse": best.val_score,
                    "best_test_rmse": best.test_score,
                    "simple_regret": best.val_score - oracle,
                    "best_iteration": best.iteration,
                }
            )

        grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for row in runs:
            grouped[(row["task"], row["method"])].append(row)

        summary: list[dict[str, Any]] = []
        for (task, method), rows in sorted(grouped.items()):
            summary.append(
                {
                    "task": task,
                    "method": method,
                    "runs": len(rows),
                    "best_val_rmse_mean": _mean(rows, "best_val_rmse"),
                    "best_val_rmse_std": _std(rows, "best_val_rmse"),
                    "best_test_rmse_mean": _mean(rows, "best_test_rmse"),
                    "best_test_rmse_std": _std(rows, "best_test_rmse"),
                    "simple_regret_mean": _mean(rows, "simple_regret"),
                    "simple_regret_std": _std(rows, "simple_regret"),
                    "best_iteration_mean": _mean(rows, "best_iteration"),
                }
            )
        return summary

    def save(self, traces: list[OptimizationTrace], output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        serializable = []
        for trace in traces:
            serializable.append(
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
            )
        (output_dir / "traces.json").write_text(json.dumps(serializable, indent=2), encoding="utf-8")

        summary = self.summarize(traces)
        with (output_dir / "summary.csv").open("w", newline="", encoding="utf-8") as handle:
            if summary:
                writer = csv.DictWriter(handle, fieldnames=list(summary[0].keys()))
                writer.writeheader()
                writer.writerows(summary)
        pairwise = self.pairwise_comparisons(traces)
        with (output_dir / "pairwise_comparisons.csv").open("w", newline="", encoding="utf-8") as handle:
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
            if pairwise:
                writer.writerows(pairwise)
        (output_dir / "conclusion.md").write_text(self.conclusion(summary), encoding="utf-8")

    @staticmethod
    def pairwise_comparisons(traces: list[OptimizationTrace]) -> list[dict[str, Any]]:
        by_task_seed_method: dict[tuple[str, int, str], float] = {}
        methods_by_task: dict[str, set[str]] = defaultdict(set)
        seeds_by_task: dict[str, set[int]] = defaultdict(set)
        for trace in traces:
            by_task_seed_method[(trace.task, trace.seed, trace.method)] = trace.best_record.val_score
            methods_by_task[trace.task].add(trace.method)
            seeds_by_task[trace.task].add(trace.seed)

        rows: list[dict[str, Any]] = []
        for task in sorted(methods_by_task):
            methods = sorted(methods_by_task[task])
            seeds = sorted(seeds_by_task[task])
            for idx, method_a in enumerate(methods):
                for method_b in methods[idx + 1 :]:
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
    def conclusion(summary: list[dict[str, Any]]) -> str:
        ranked = sorted(summary, key=lambda row: row["best_val_rmse_mean"])
        lines = ["# Baseline Evaluation Conclusion", ""]
        lines.append(
            "Lower RMSE and lower simple regret are better. The oracle for simple regret is "
            "the best validation RMSE observed by any compared method under the same task and seed."
        )
        lines.append("")
        lines.append("| Rank | Method | Val RMSE mean | Test RMSE mean | Simple regret mean |")
        lines.append("| --- | --- | ---: | ---: | ---: |")
        for idx, row in enumerate(ranked, start=1):
            lines.append(
                f"| {idx} | {row['method']} | {row['best_val_rmse_mean']:.4f} | "
                f"{row['best_test_rmse_mean']:.4f} | {row['simple_regret_mean']:.4f} |"
            )

        winner = ranked[0]
        lines.append("")
        lines.append(
            f"On this toy regression task, **{winner['method']}** gives the strongest average "
            f"validation RMSE ({winner['best_val_rmse_mean']:.4f}). The gap between methods is "
            "small in this deliberately simple task, so the result should be treated as a smoke "
            "test for the protocol rather than decisive evidence. Random Search is the "
            "sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate "
            "modeling, and HyperRL tests a sequential RL-style policy that can consume learning "
            "curve trend features."
        )
        lines.append("")
        lines.append(
            "This is a lightweight baseline scaffold, not yet a full reproduction of Hyp-RL's "
            "LSTM policy. It is intended to make the evaluation protocol concrete before plugging "
            "in HPOBench/NAS-Bench-360 or a learned cross-dataset policy."
        )
        return "\n".join(lines) + "\n"


def _mean(rows: list[dict[str, Any]], key: str) -> float:
    return float(mean(float(row[key]) for row in rows))


def _std(rows: list[dict[str, Any]], key: str) -> float:
    if len(rows) <= 1:
        return 0.0
    return float(stdev(float(row[key]) for row in rows))
