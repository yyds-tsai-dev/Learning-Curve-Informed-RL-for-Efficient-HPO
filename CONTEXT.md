# Context Glossary

## Kaggle Regression Task

A Kaggle Regression Task is one Kaggle Playground Series regression episode treated as one hyperparameter-optimization task.

Each task represents a distinct tabular regression dataset. The task exposes the same kind of learning-curve-based optimization surface expected by LC-DQN experiments, so methods can be compared across a shared pool of tasks.

For Kaggle Regression Tasks, the optimization surface is a cached learning-curve table produced by training small MLP regressors on the episode data. The shared HPO search space covers MLP training and architecture hyperparameters.

The benchmark cache uses 256 configurations per task, 25 epochs per configuration, and one seed per configuration. Scores are computed from fixed splits of each Kaggle `train.csv`; Kaggle hidden test labels are not used.

Each Kaggle `train.csv` is split into 80% train, 10% validation, and 10% held-out test. The training split fits the MLP. The validation split provides the learning curve and HPO selection score. The held-out test split provides the final reporting score.

Kaggle Regression Tasks use one shared tabular preprocessing protocol. Identifier-like columns are excluded. Numeric features are imputed and scaled. Categorical features are imputed and one-hot encoded. Targets are scaled for model training while reported scores remain interpretable for the task.

## Task Meta-Features

Task Meta-Features are dataset-level descriptors used to condition cross-task Hyp-RL and LC-DQN policies.

For Kaggle Regression Tasks, Task Meta-Features follow the Hyp-RL paper Table 1 style descriptors: 16 dataset/preprocessing-only features covering instance count, processed feature count, dimensionality ratios, and skewness/kurtosis summaries from the preprocessed training feature matrix. They do not include HPO cache outcomes, oracle scores, target distribution statistics, model performance, or other values that would leak benchmark answers into the policy.

Hyp-RL and LC-DQN use the same Task Meta-Features. LC-DQN differs by additionally using learning-curve features observed during configuration evaluation.

## Task Pool

A Task Pool is the fixed collection of Kaggle Regression Tasks used in an experiment.

When comparing the effect of task count, smaller pools are nested subsets of the larger pool. This keeps the comparison focused on the number of available training tasks rather than on unrelated differences in dataset selection.

The Kaggle Regression Task Pool is a manually selected whitelist of 15 tasks fixed at a snapshot date. It is not dynamically regenerated from Kaggle listings during an experiment.

The fixed Kaggle Regression Task Pool contains: S3E1 California Housing, S3E6 Paris Housing Price, S3E8 Gemstone Price, S3E9 Concrete Strength, S3E11 Media Campaign Cost, S3E14 Wild Blueberry Yield, S3E16 Crab Age, S3E25 Mohs Hardness, S4E4 Abalone, S4E5 Flood Prediction, S4E9 Used Car Prices, S4E12 Insurance, S5E2 Backpack Prediction, S5E4 Podcast Listening Time, and S5E5 Calorie Expenditure.

Task identity and acquisition are manifest-driven. The repository records competition slugs, task names, targets, metric direction, and subset order. Raw Kaggle data is acquired through a Kaggle API helper and is not part of the source-controlled benchmark definition.

## LCBench Classification Task

An LCBench Classification Task is one OpenML tabular classification dataset represented as a learning-curve hyperparameter-optimization task.

LCBench Classification Tasks are distinct from Kaggle Regression Tasks: their underlying supervised problem is classification, while the HPO benchmark compares optimizers by how well they select neural-network hyperparameters from precomputed learning curves.

## LC-DQN Task-Count Comparison

The LC-DQN Task-Count Comparison measures whether LC-DQN performance improves as the number of training tasks increases.

The comparison uses task counts of 1, 5, 10, and 15 drawn from the shared Task Pool.

For this comparison, LC-DQN is always evaluated on all 15 tasks in the Task Pool. Only the number of meta-training tasks changes. The training task subsets are nested so that the 1-task subset is contained in the 5-task subset, the 5-task subset is contained in the 10-task subset, and the 10-task subset is contained in the 15-task subset.

The nested order is: S3E1 California Housing; S4E4 Abalone; S4E12 Insurance; S3E14 Wild Blueberry Yield; S4E9 Used Car Prices; S3E9 Concrete Strength; S3E16 Crab Age; S5E5 Calorie Expenditure; S3E11 Media Campaign Cost; S5E4 Podcast Listening Time; S3E6 Paris Housing Price; S3E8 Gemstone Price; S3E25 Mohs Hardness; S4E5 Flood Prediction; S5E2 Backpack Prediction.

## Kaggle All-Methods Benchmark

The Kaggle All-Methods Benchmark compares all supported HPO methods on the full 15-task Kaggle Regression Task Pool.

It answers which method performs best on the new task pool, separately from the LC-DQN Task-Count Comparison.

Both Kaggle experiment suites use 20 HPO evaluations per task and 5 optimizer seeds as the main benchmark setting. Cross-task LC-DQN meta-training uses 150 total episodes with 20 evaluations per meta-training episode.

## Normalized Simple Regret

Normalized Simple Regret is the primary metric for comparing performance across Kaggle Regression Tasks.

It rescales each task's simple regret before aggregation so that tasks with larger target-value scales do not dominate the benchmark summary.

For each task, normalization uses the task's cached HPO table. The oracle is the best validation score in that table. The reference-worst is a high-percentile validation score from the same table, used as the upper end of the min-max scale.
