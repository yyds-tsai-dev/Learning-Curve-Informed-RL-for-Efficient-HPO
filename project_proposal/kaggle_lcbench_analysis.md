# Kaggle vs. LCBench: Analysis for §5 (Experimental Results)

Draft text and supporting numbers for adding the Kaggle Playground results to the
report and comparing them against the existing LCBench results. Metric is
*normalized simple regret* (lower is better; 0 = matched the oracle config).
Headline framing: **(1) cold-start efficiency** and **(2) curve-feature ablation
(LC-DQN vs. HyperRL)**.

Methods: Bayesian Optimization (BO), Random Search, CrossDataset-HyperRL
(meta-RL, scalar reward only), CrossDataset-LC-DQN (full method, adds
learning-curve derivative features).

---

## 0. Key benchmark difference (state this once, up front)

| | LCBench | Kaggle Playground |
|---|---|---|
| Task type | 35 classification tasks | 15 regression tasks |
| Metric | balanced-error units (**raw**) | RMSE → **normalized** simple regret in [0,1] |
| Curves | MLP, 50 epochs | 25 epochs |
| **Seeds per task** | **1** (`runs=1`, `std=0` everywhere) | **5** |

The seed count and the raw-vs-normalized metric are the two facts that explain why
the Kaggle ablation is clean and the LCBench one is not. State the benchmark
difference explicitly: the two suites test cross-task-*type* generalization
(classification vs. regression).

---

## 1. Cold-start efficiency (headline, Kaggle-led)

> On the Kaggle regression suite, CrossDataset-LC-DQN gives the lowest normalized
> simple regret at the first trial — **0.191** vs. **0.523** for both BO and Random
> Search (−63%) and **0.334** for HyperRL (−43%). This is the clearest evidence that
> learning-curve derivative features provide a useful inductive bias at the
> cold-start, where BO has no surrogate yet and falls back to random sampling. The
> advantage is concentrated in the first 1–2 trials: BO overtakes from trial 2
> (0.097 vs. 0.124) and is best asymptotically. So the contribution is *sample
> efficiency under tight budgets*, not asymptotic accuracy.

Supporting numbers (Kaggle, normalized simple regret):

| Budget | LC-DQN | HyperRL | BO | Random |
|---:|---:|---:|---:|---:|
| 1 | **0.191** | 0.334 | 0.523 | 0.523 |
| 2 | 0.124 | 0.203 | **0.097** | **0.097** |
| 5 | 0.062 | 0.073 | **0.054** | 0.067 |
| 15 | 0.0263 | 0.0302 | **0.0179** | 0.0274 |
| 20 | 0.0217 | 0.0251 | **0.0150** | 0.0243 |

- BO and Random are identical at budgets 1–3 (BO has no surrogate yet).
- LC-DQN's edge is real but lives at trial 1–2; from trial ~2 onward BO leads.

---

## 2. Curve-feature ablation (LC-DQN vs. HyperRL)

> Isolating the effect of curve features (LC-DQN adds them; HyperRL does not): on
> Kaggle, LC-DQN dominates HyperRL at every budget and on average per-task rank
> (2.33 vs. 2.87), and HyperRL never leads at any budget — curve features help
> cleanly here. On LCBench the picture is mixed: LC-DQN leads HyperRL on per-task
> rank at budgets 20 and 150 but trails at 50 and 100, with no consistent ordering.

**Overall per-task rank (lower is better), Kaggle:**

| Method | Avg rank |
|---|---:|
| BO | 1.67 |
| LC-DQN | 2.33 |
| HyperRL | 2.87 |
| Random | 3.13 |

**LCBench per-task rank by budget (LC-DQN vs. HyperRL highlighted):**

| Budget | LC-DQN | HyperRL | BO | Random | who leads (LC-DQN vs HyperRL) |
|---:|---:|---:|---:|---:|---|
| 20 | 2.94 | 2.83 | 1.46 | 2.77 | ~tie (HyperRL +0.11) |
| 50 | 2.83 | **2.31** | 1.57 | 3.29 | HyperRL |
| 100 | 2.97 | 3.06 | 1.49 | 2.49 | LC-DQN (both weak) |
| 150 | **2.60** | 3.11 | 1.40 | 2.89 | LC-DQN |

Note: across **both** benchmarks BO wins per-task rank and rank-1 counts (LCBench
BO rank 1.40–1.57, winning 24–28 of 35 tasks at every budget; Kaggle BO rank 1.67).
Frame BO as the strong non-learning baseline; the ablation claim is specifically
LC-DQN vs. HyperRL among learning-based methods.

---

## 3. Why LCBench cannot cleanly confirm the ablation

Ranked by how strongly the data supports each reason.

1. **Single seed → no statistical power (strongest, directly evidenced).** Every
   LCBench row is one run with `std=0`; each task's rank turns on a single
   lucky/unlucky draw. HyperRL's own average regret lurches across budgets
   (4.38 → 1.17 → 2.68 → 4.88) — that instability *is* the noise. Kaggle's 5 seeds
   is why its ordering is stable. This alone can explain the inconsistency.
2. **Raw, heterogeneous metric scale (directly evidenced).** LCBench tables
   aggregate *un-normalized* regret, so a few high-error tasks (e.g. Fashion-MNIST)
   dominate the average, and the five curve-derivative features (final value,
   slope, curvature, mean first/second difference, total improvement) are computed
   on per-task curves of wildly different scales — without normalization they do
   not transfer across tasks, washing out LC-DQN's edge. Kaggle normalizes both.
3. **Classification vs. regression curve shape (plausible).** LCBench's 50-epoch
   accuracy curves saturate/plateau early, so the last-window slope and curvature
   ≈ 0 and the curve features carry little late-stage signal; RMSE regression
   curves are smoother and more informative for finite-difference derivatives.
4. **Capacity/variance (plausible).** The +5 input dimensions cost extra
   parameters, fit on heterogeneous 35-task meta-training with only one seed; the
   added variance can swamp the weak signal.

---

## 4. Honest one-paragraph framing for the report

> Curve features deliver a real, measurable cold-start win on a controlled,
> normalized, multi-seed benchmark (Kaggle); LCBench's single-seed, raw-scale,
> early-saturating setup lacks the resolution to confirm or deny it. This is itself
> a finding about the benchmark design needed to evaluate curve-aware HPO: cheap,
> normalized, multi-seed regression suites expose the early-budget signal that
> coarse single-seed classification benchmarks hide.

---

## 5. Caveats / things to double-check before submission

- LCBench `summary.csv`/`conclusion.md` report **raw** simple regret, but the
  LCBench *figures* in the report are titled "Normalized Simple Regret" — so the
  plots are comparable to Kaggle but the tables are not. Put only normalized numbers
  in the cross-benchmark text.
- The Kaggle task-count study (train_1/5/10/15) showed final regret
  0.0223/0.0229/0.0255/0.0217 — **non-monotone** and all within ~1 SE (≈0.0025):
  no significant transfer benefit from more source tasks. Mention only if you keep
  that sub-experiment.
- No formal significance tests exist in any results file; lead with per-task rank
  and rank-1 counts, not raw average regret.
