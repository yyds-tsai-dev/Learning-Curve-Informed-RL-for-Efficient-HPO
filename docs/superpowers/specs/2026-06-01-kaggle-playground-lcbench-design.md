# Kaggle Playground Regression Benchmark Design

Date: 2026-06-01

## Purpose

Add Kaggle Playground Series regression episodes as the next LCBench-style benchmark surface for learning-curve-informed HPO.

The work has two deliverables:

1. Choose 15 fixed Kaggle regression tasks for all methods.
2. Compare whether LC-DQN improves as the number of meta-training tasks increases across 1, 5, 10, and 15 tasks.

## Design Choice

Use an LCBench-compatible cached HPO table for each Kaggle task.

Each Kaggle regression episode becomes one HPO task. Raw Kaggle `train.csv` data is converted into a finite table of MLP hyperparameter configurations, validation learning curves, final validation scores, and held-out test scores. Optimizers then query the cached table instead of training models online during HPO evaluation.

This keeps the new benchmark close to the existing `LCBenchTask` design: one task exposes a finite set of candidate configurations and learning curves, while optimizers remain responsible for choosing which configurations to evaluate.

## Task Pool

The benchmark uses a fixed 15-task whitelist, not a dynamic Kaggle listing.

| Order | Episode | Task |
| --- | --- | --- |
| 1 | S3E1 | California Housing |
| 2 | S3E6 | Paris Housing Price |
| 3 | S3E8 | Gemstone Price |
| 4 | S3E9 | Concrete Strength |
| 5 | S3E11 | Media Campaign Cost |
| 6 | S3E14 | Wild Blueberry Yield |
| 7 | S3E16 | Crab Age |
| 8 | S3E25 | Mohs Hardness |
| 9 | S4E4 | Abalone |
| 10 | S4E5 | Flood Prediction |
| 11 | S4E9 | Used Car Prices |
| 12 | S4E12 | Insurance |
| 13 | S5E2 | Backpack Prediction |
| 14 | S5E4 | Podcast Listening Time |
| 15 | S5E5 | Calorie Expenditure |

The task pool excludes binary classification episodes and time-series forecasting episodes so the benchmark remains a tabular regression pool.

## Nested LC-DQN Training Order

The LC-DQN task-count sweep uses a balanced nested order:

| Count | Meta-training tasks |
| --- | --- |
| 1 | S3E1 |
| 5 | S3E1, S4E4, S4E12, S3E14, S4E9 |
| 10 | S3E1, S4E4, S4E12, S3E14, S4E9, S3E9, S3E16, S5E5, S3E11, S5E4 |
| 15 | All fixed task-pool tasks |

Evaluation is always on all 15 tasks. Only the number of meta-training tasks changes.

## Data Acquisition

Task identity and data acquisition are manifest-driven.

The repository should store a manifest containing:

- competition slug
- display name
- target column
- metric direction
- task-pool membership
- nested subset order

Raw Kaggle data should be downloaded with a helper script, for example:

```bash
uv run python scripts/download_kaggle_playground.py --tasks all
```

Raw CSV and zip files should live under `data/kaggle_playground/raw/<slug>/` and stay out of git. The source-controlled benchmark definition is the manifest plus cache-building code, not the Kaggle raw data.

## Cache Generation

Each task cache contains:

- 256 MLP configurations per task
- 25 epochs per configuration
- 1 training seed per configuration
- fixed 80% train, 10% validation, 10% held-out test split from Kaggle `train.csv`
- deterministic capped MLP fitting subset: at most 2,000 rows from the training split
- categorical cardinality cap: keep at most the top 32 training-split categories per categorical column

The hidden Kaggle competition test set is not used because labels are unavailable. The held-out test score comes from the internal 10% test split.

The capped training subset controls cache-generation runtime. Preprocessing
statistics are fitted on the fixed training split; MLP fitting and task
meta-features use the deterministic capped training subset. Validation scores,
test scores, per-task oracle, and per-task reference-worst are all tied to the
same fixed task split/cache table. Validation and held-out test splits are not
capped. The categorical cap prevents high-cardinality identifiers, dates, and
free-form strings from exploding the one-hot feature space; values outside the
top categories are encoded as all-zero for that source column.

The shared MLP HPO search space should cover:

- learning rate
- weight decay
- hidden width
- number of layers
- dropout
- batch size

Each cached configuration stores:

- hyperparameter configuration
- per-epoch validation RMSE learning curve
- final validation RMSE
- final held-out test RMSE
- task metadata
- cache-generation seed and split metadata

## Preprocessing

All tasks use one shared preprocessing protocol:

- drop identifier-like columns such as `id` and `Id`
- read the target column from the manifest
- numeric features: median imputation and standard scaling
- categorical features: most-frequent imputation and one-hot encoding with unknown categories ignored
- target: scaled for training, with reported RMSE kept interpretable for the task

The goal is to make task differences come from the datasets, not from episode-specific Kaggle notebook feature engineering.

## Meta-Features

Kaggle regression tasks should expose task-level meta-features through `meta_features()`.

Existing cross-dataset Hyp-RL and LC-DQN already consume task meta-features through the shared `_meta_features(task)` helper. The helper reads `task.meta_features()` when available and L2-normalizes the returned vector before the cross-dataset controller uses it. With the LSTM network, the meta-feature vector initializes the LSTM hidden and cell states. The same vector is also included in each history row.

Kaggle task meta-features must use only dataset and preprocessing statistics, not HPO cache performance or target distribution statistics. They must not include oracle scores, reference-worst scores, validation RMSE summaries, test RMSE summaries, winning configuration properties, target moments, or any other value derived from the cached HPO outcomes.

Use this fixed 16-dimensional vector, matching the Hyp-RL paper Table 1 descriptor style. Counts use the deterministic capped training subset used for MLP fitting. Feature counts and skewness/kurtosis summaries use the fully preprocessed feature matrix after numeric imputation/scaling and categorical one-hot encoding.

| Index | Feature |
| --- | --- |
| 0 | Number of Instances |
| 1 | Log Number of Instances |
| 2 | Number of Features |
| 3 | Log Number of Features |
| 4 | Data Set Dimensionality |
| 5 | Log Data Set Dimensionality |
| 6 | Inverse Data Set Dimensionality |
| 7 | Log Inverse Data Set Dimensionality |
| 8 | Kurtosis Min |
| 9 | Kurtosis Max |
| 10 | Kurtosis Mean |
| 11 | Kurtosis Standard Deviation |
| 12 | Skewness Min |
| 13 | Skewness Max |
| 14 | Skewness Mean |
| 15 | Skewness Standard Deviation |

`Number of Instances` is `n_train_rows`. `Number of Features` is the processed feature dimension visible to the model after one-hot encoding. `Data Set Dimensionality` is `n_features / max(n_instances, 1)`, and inverse dimensionality is `n_instances / max(n_features, 1)`. Log features use `log1p`. Skewness and excess kurtosis are computed per processed feature column on `x_train`; zero-variance columns contribute `0` for both skewness and kurtosis. Summary standard deviations use population standard deviation.

Hyp-RL and LC-DQN use this same 16-dimensional task meta-feature vector. LC-DQN's additional information comes only from learning-curve and derivative features observed after evaluating configurations.

## Task Adapter

Add a `KaggleRegressionTask` adapter parallel to `LCBenchTask`.

It should expose the same optimizer-facing behavior:

- `name`
- `search_space`
- `candidate_configs`
- `candidate_vectors`
- `metric_name()`
- `evaluate(config, seed) -> EvalResult`
- `meta_features()`

`evaluate` should return cached values:

- `learning_curve`: validation RMSE curve
- `val_score`: final validation RMSE
- `test_score`: final held-out test RMSE
- `metadata`: task name, slug, config id, and split/cache identifiers

## Metrics

The primary metric is normalized simple regret:

```text
(best_found_val_score - oracle_val_score)
/
(reference_worst_val_score - oracle_val_score + eps)
```

For each task:

- `oracle_val_score` is the best final validation score in that task's cached HPO table.
- `reference_worst_val_score` is the 90th percentile final validation score in the same cached table.
- lower is better.

The 90th percentile reference-worst prevents one failed or extreme configuration from making regrets look artificially small.

Auxiliary metrics:

- final validation RMSE
- held-out test RMSE
- best iteration
- raw simple regret

## Experiment Suites

### All-Methods Benchmark

Purpose: compare HPO methods fairly on the new 15-task Kaggle regression pool.

Settings:

- tasks: all 15
- methods: Random Search, Bayesian Optimization, HyperRL-DQN, LC-DQN
- HPO evaluation budget: 20 configurations per task
- optimizer seeds: 5
- primary metric: normalized simple regret

Expected outputs:

```text
results/kaggle_playground/all_methods/
  summary.csv
  pairwise_comparisons.csv
  traces.json
  conclusion.md
  performance_vs_eval_budget.csv
  performance_vs_eval_budget.png
```

### LC-DQN Task-Count Sweep

Purpose: test whether LC-DQN performance improves as the number of meta-training tasks increases.

Settings:

- method: LC-DQN only
- meta-training task counts: 1, 5, 10, 15
- meta-training task subsets: balanced nested order
- evaluation tasks: all 15
- total meta-training episodes: 150
- meta-training episode budget: 20 evaluations
- final evaluation budget: 20 configurations per task
- optimizer seeds: 5
- primary metric: mean normalized simple regret on all 15 evaluation tasks

Expected outputs:

```text
results/kaggle_playground/lcdqn_task_count/
  summary_by_task_count.csv
  traces.json
  normalized_simple_regret_by_task_count.csv
  normalized_simple_regret_by_task_count.png
  conclusion.md
```

The main plot uses:

- x-axis: number of meta-training tasks, `{1, 5, 10, 15}`
- y-axis: mean normalized simple regret across all 15 evaluation tasks
- error bars: standard error

CSV outputs should include mean, standard deviation, and standard error.

## Required Code Changes

Add manifest and data/cache scripts:

- `data/kaggle_playground/manifest.json`
- `scripts/download_kaggle_playground.py`
- `scripts/build_kaggle_playground_cache.py`
- `scripts/run_kaggle_playground.py`

Add benchmark components:

- `KaggleRegressionTask`
- cache loading and validation utilities
- normalized simple regret computation
- task-count sweep runner

Extend cross-dataset evaluation so LC-DQN can meta-train on one task list and evaluate on a separate fixed task list.

## Testing Strategy

Use a small smoke fixture before running full Kaggle caches:

- a tiny manifest with one or two synthetic CSV-like regression tasks
- a tiny cache with a few configurations and short learning curves

Test coverage should verify:

- manifest parsing
- preprocessing handles numeric and categorical columns
- Kaggle task meta-features contain the fixed 16-dimensional Hyp-RL Table 1 style dataset/preprocessing vector
- Kaggle task meta-features do not depend on HPO cache scores
- cache builder writes valid learning curves and metadata
- `KaggleRegressionTask.evaluate` returns cached `EvalResult` values
- normalized simple regret uses the table oracle and 90th percentile reference-worst
- LC-DQN task-count runner trains on nested subsets but evaluates on all tasks

Full Kaggle benchmark generation is an integration workflow and should be documented as slower than unit tests.

## Source Checks

Live source checks on 2026-06-01 confirmed the task-pool direction with Kaggle pages for examples including:

- https://www.kaggle.com/competitions/playground-series-s3e1
- https://www.kaggle.com/competitions/playground-series-s3e6
- https://www.kaggle.com/competitions/playground-series-s3e8
- https://www.kaggle.com/competitions/playground-series-s3e9
- https://www.kaggle.com/competitions/playground-series-s4e4
- https://www.kaggle.com/competitions/playground-series-s4e12
- https://www.kaggle.com/competitions/playground-series-s5e5

The repository's local LCBench file has 35 datasets with 2000 configurations each. The Kaggle cache deliberately uses 256 configurations per task as a runtime-conscious benchmark size.
