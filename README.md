# Learning Curve-Informed RL for Efficient HPO

This repository contains a lightweight HPO evaluation scaffold for the project proposal.

## LCBench Baselines

Python 3.12 is used for this project. Create the local uv environment and install dependencies with:

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
```

LCBench is the primary tabular benchmark interface. Pass the official downloaded LCBench JSON
from figshare, or run the tiny fixture for a smoke test:

```bash
uv run python scripts/run_lcbench_baselines.py --data-path data/tiny_lcbench.json
```

For the full LCBench file, use a larger budget, for example `--budget 20`, and optionally
`--dataset <LCBench dataset name>`.

The current official-data result was generated with:

```bash
uv run python scripts/run_lcbench_baselines.py \
  --data-path data/lcbench/data_2k_lw.json \
  --datasets credit-g,Fashion-MNIST,Australian,adult,bank-marketing,MiniBooNE,APSFailure \
  --budget 20 \
  --seeds 5 \
  --output-dir results/lcbench
```

Implemented methods:

- `Random Search`
- `Bayesian Optimization`
- `HyperRL-DQN`: DQN with replay buffer and target network, matching the Hyp-RL setup with a
  configurable sequence encoder (`lstm` or `mlp`, default `lstm`)
- `OurMethod-LC-DQN`: the same DQN controller with learning-curve and derivative features appended
  to the state

Outputs are written to `results/lcbench/`:

- `summary.csv`
- `pairwise_comparisons.csv`
- `traces.json`
- `conclusion.md`

Budget sweep outputs are also available:

- `results/lcbench_budget50/`
- `results/lcbench_budget100/`
- `results/lcbench_budget_sweep.md`
- `results/lcbench_budget500_20datasets/`

## Kaggle Playground Regression Benchmark

The Kaggle Playground benchmark uses a fixed 15-task regression pool defined in
`data/kaggle_playground/manifest.json` at snapshot date `2026-06-01`. Each
Kaggle Playground Series episode is treated as one `KaggleRegressionTask`, and
raw Kaggle data is not committed.

Fixed task pool:

| Episode | Task | Target |
| --- | --- | --- |
| S3E1 | California Housing | `MedHouseVal` |
| S3E6 | Paris Housing Price | `price` |
| S3E8 | Gemstone Price | `price` |
| S3E9 | Concrete Strength | `Strength` |
| S3E11 | Media Campaign Cost | `cost` |
| S3E14 | Wild Blueberry Yield | `yield` |
| S3E16 | Crab Age | `Age` |
| S3E25 | Mohs Hardness | `Hardness` |
| S4E4 | Abalone | `Rings` |
| S4E5 | Flood Prediction | `FloodProbability` |
| S4E9 | Used Car Prices | `price` |
| S4E12 | Insurance | `Premium Amount` |
| S5E2 | Backpack Prediction | `Price` |
| S5E4 | Podcast Listening Time | `Listening_Time_minutes` |
| S5E5 | Calorie Expenditure | `Calories` |

Download raw competition files:

```bash
uv run python scripts/download_kaggle_playground.py --tasks all
```

Build cached MLP learning-curve tables:

```bash
uv run python scripts/build_kaggle_playground_cache.py --tasks all
```

Cache generation uses 256 MLP configurations per task, 25 epochs per
configuration, and one seed per configuration. Each Kaggle `train.csv` is split
with the fixed manifest seed into 80% train, 10% validation, and 10% held-out
test. MLP fitting is capped to a deterministic 2,000-row subset of the training
split per task; validation and held-out test scores are still computed on the
full 10% validation and 10% test splits. Categorical preprocessing keeps the top
32 training-split categories per column to avoid high-cardinality one-hot
explosions.

The shared MLP HPO search space covers learning rate, weight decay, hidden
width, number of layers, dropout, and batch size. The primary Kaggle summary
metric is normalized simple regret, using each task cache's best validation
score as the oracle and the 90th percentile validation score as the
reference-worst point.

Run all methods on all 15 tasks:

```bash
uv run python scripts/run_kaggle_playground.py \
  --suite all-methods \
  --budget 20 \
  --seeds 5 \
  --total-episodes 150
```

Settings:

- evaluation tasks: all 15 Kaggle Regression Tasks
- HPO evaluation budget: 20 configurations per task
- optimizer seeds: 5
- cross-dataset DQN meta-training: 150 total episodes
- meta-training episode budget: 20 evaluations
- methods: `Random Search`, `Bayesian Optimization`, `CrossDataset-HyperRL`,
  `CrossDataset-LC-DQN`
- outputs: `results/kaggle_playground/all_methods/`

Current result summary:

| Rank | Method | Mean normalized simple regret | Avg per-task rank | Rank-1 tasks |
| ---: | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.0150 | 1.67 | 9 |
| 2 | CrossDataset-LC-DQN | 0.0217 | 2.33 | 4 |
| 3 | Random Search | 0.0243 | 3.13 | 0 |
| 4 | CrossDataset-HyperRL | 0.0251 | 2.87 | 2 |

Run the LC-DQN task-count sweep:

```bash
uv run python scripts/run_kaggle_playground.py \
  --suite lcdqn-task-count \
  --budget 20 \
  --seeds 5 \
  --total-episodes 150
```

Settings:

- method: `CrossDataset-LC-DQN`
- meta-training task counts: 1, 5, 10, and 15
- meta-training subsets: nested prefixes of the manifest `nested_order`
- evaluation tasks: always all 15 tasks
- final evaluation budget: 20 configurations per task
- optimizer seeds: 5
- outputs: `results/kaggle_playground/lcdqn_task_count/`

Current LC-DQN task-count result:

| Meta-training tasks | Runs | Mean normalized simple regret | Std | SE |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 75 | 0.0223 | 0.0193 | 0.0022 |
| 5 | 75 | 0.0229 | 0.0197 | 0.0023 |
| 10 | 75 | 0.0255 | 0.0211 | 0.0024 |
| 15 | 75 | 0.0217 | 0.0220 | 0.0025 |

The best mean score is at 15 meta-training tasks, but the curve is not
monotonic across the tested task counts.

## Toy Regression Baseline

The earlier synthetic regression smoke test is still available:

```bash
uv run python scripts/run_toy_regression.py --budget 20 --seeds 5
```
