# Learning Curve-Informed RL for Efficient HPO

本專案是一個輕量的 HPO 評估框架，用來驗證 project proposal 裡的 learning-curve-informed reinforcement learning 想法。重點是比較一般 HPO baseline、Hyp-RL 風格的 DQN，以及加入 learning curve / derivative state features 的 LC-DQN 方法。

## 環境設定

本專案使用 Python 3.12。可以用 `uv` 建立本地環境並安裝相依套件：

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
```

## LCBench Baselines

LCBench 是主要的 tabular benchmark 介面。可以傳入官方下載的 LCBench JSON 檔，或先用小型 fixture 做 smoke test：

```bash
uv run python scripts/run_lcbench_baselines.py --data-path data/tiny_lcbench.json
```

若使用完整 LCBench 檔案，建議使用較大的 budget，例如 `--budget 20`，也可以用 `--dataset <LCBench dataset name>` 指定單一資料集。

目前的官方資料實驗指令是：

```bash
uv run python scripts/run_lcbench_baselines.py \
  --data-path data/lcbench/data_2k_lw.json \
  --datasets credit-g,Fashion-MNIST,Australian,adult,bank-marketing,MiniBooNE,APSFailure \
  --budget 20 \
  --seeds 5 \
  --output-dir results/lcbench
```

已實作的方法：

- `Random Search`
- `Bayesian Optimization`
- `HyperRL-DQN`：使用 replay buffer 與 target network 的 DQN，對齊 Hyp-RL 設定；sequence encoder 可設定為 `lstm` 或 `mlp`，預設為 `lstm`
- `OurMethod-LC-DQN`：和 `HyperRL-DQN` 使用同一個 DQN controller，但在 state 中加入 learning-curve value 與 derivative features

輸出會寫到 `results/lcbench/`：

- `summary.csv`
- `pairwise_comparisons.csv`
- `traces.json`
- `conclusion.md`

Budget sweep 的輸出也保留在：

- `results/lcbench_budget50/`
- `results/lcbench_budget100/`
- `results/lcbench_budget_sweep.md`
- `results/lcbench_budget500_20datasets/`

## Kaggle Playground Regression Benchmark

Kaggle Playground benchmark 使用固定的 15-task regression pool，定義在 `data/kaggle_playground/manifest.json`，snapshot date 是 `2026-06-01`。每一個 Kaggle Playground Series episode 都被視為一個 `KaggleRegressionTask`。

固定 task pool：

| Episode | Task                   | Target                     |
| ------- | ---------------------- | -------------------------- |
| S3E1    | California Housing     | `MedHouseVal`            |
| S3E6    | Paris Housing Price    | `price`                  |
| S3E8    | Gemstone Price         | `price`                  |
| S3E9    | Concrete Strength      | `Strength`               |
| S3E11   | Media Campaign Cost    | `cost`                   |
| S3E14   | Wild Blueberry Yield   | `yield`                  |
| S3E16   | Crab Age               | `Age`                    |
| S3E25   | Mohs Hardness          | `Hardness`               |
| S4E4    | Abalone                | `Rings`                  |
| S4E5    | Flood Prediction       | `FloodProbability`       |
| S4E9    | Used Car Prices        | `price`                  |
| S4E12   | Insurance              | `Premium Amount`         |
| S5E2    | Backpack Prediction    | `Price`                  |
| S5E4    | Podcast Listening Time | `Listening_Time_minutes` |
| S5E5    | Calorie Expenditure    | `Calories`               |

下載原始 competition files：

```bash
uv run python scripts/download_kaggle_playground.py --tasks all
```

建立 cached MLP learning-curve tables：

```bash
uv run python scripts/build_kaggle_playground_cache.py --tasks all
```

Cache 生成設定如下：每個 task 產生 256 組 MLP configurations，每組 configuration 訓練 25 epochs，且每組 configuration 使用 1 個 training seed。每個 Kaggle `train.csv` 會用 manifest 裡的固定 seed 切成 80% train、10% validation、10% held-out test。MLP fitting 只使用 training split 中 deterministic 抽出的 2,000 rows；validation score 與 held-out test score 仍然使用完整的 10% validation / 10% test split。Categorical preprocessing 只保留每個 categorical column 在 training split 裡最常見的前 32 個 categories，避免 high-cardinality one-hot encoding 爆掉。

共用的 MLP HPO search space 包含 learning rate、weight decay、hidden width、number of layers、dropout、batch size。Kaggle 實驗主要用 normalized simple regret 做跨 task 比較：oracle 是該 task cache table 裡最好的 validation score，reference-worst 是同一張 table 裡 validation score 的第 90 百分位。

### All-Methods Benchmark

執行所有方法、所有 15 個 Kaggle Regression Tasks：

```bash
uv run python scripts/run_kaggle_playground.py \
  --suite all-methods \
  --budget 20 \
  --seeds 5 \
  --total-episodes 150
```

實驗設定：

- evaluation tasks：全部 15 個 Kaggle Regression Tasks
- HPO evaluation budget：每個 task 20 次 configuration evaluations
- optimizer seeds：5
- cross-dataset DQN meta-training：150 total episodes
- meta-training episode budget：每個 episode 20 evaluations
- methods：`Random Search`、`Bayesian Optimization`、`CrossDataset-HyperRL`、`CrossDataset-LC-DQN`
- outputs：`results/kaggle_playground/all_methods/`

目前結果摘要如下。數值越低越好。

| Rank | Method                | Mean normalized simple regret | Avg per-task rank | Rank-1 tasks |
| ---: | --------------------- | ----------------------------: | ----------------: | -----------: |
|    1 | Bayesian Optimization |                        0.0150 |              1.67 |            9 |
|    2 | CrossDataset-LC-DQN   |                        0.0217 |              2.33 |            4 |
|    3 | Random Search         |                        0.0243 |              3.13 |            0 |
|    4 | CrossDataset-HyperRL  |                        0.0251 |              2.87 |            2 |

在這個設定下，我們的方法 `CrossDataset-LC-DQN` 是第二名：15 個 Kaggle regression tasks、每個 task 20 次 HPO evaluations、5 個 optimizer seeds、150 個 cross-dataset DQN meta-training episodes。它的 mean normalized simple regret 是 `0.0217`，平均 per-task rank 是 `2.33`，有 4 個 tasks 拿到 rank 1。這表示 learning-curve features 有幫助，因為 `CrossDataset-LC-DQN` 優於同樣是 cross-dataset DQN 的 `CrossDataset-HyperRL`，但整體仍輸給 `Bayesian Optimization`。

### LC-DQN Task-Count Sweep 與冷啟動

執行 LC-DQN task-count sweep：

```bash
uv run python scripts/run_kaggle_playground.py \
  --suite lcdqn-task-count \
  --budget 20 \
  --seeds 5 \
  --total-episodes 150
```

實驗設定：

- method：`CrossDataset-LC-DQN`
- meta-training task counts：1、5、10、15
- meta-training subsets：manifest `nested_order` 的 nested prefixes
- evaluation tasks：永遠是全部 15 個 tasks
- final evaluation budget：每個 task 20 次 configuration evaluations
- optimizer seeds：5
- outputs：`results/kaggle_playground/lcdqn_task_count/`

目前 LC-DQN task-count 結果如下。每個 task-count setting 都在 15 個 evaluation tasks x 5 seeds 上評估，所以 runs 是 75。

| Meta-training tasks | Runs | Mean normalized simple regret |    Std |     SE |
| ------------------: | ---: | ----------------------------: | -----: | -----: |
|                   1 |   75 |                        0.0223 | 0.0193 | 0.0022 |
|                   5 |   75 |                        0.0229 | 0.0197 | 0.0023 |
|                  10 |   75 |                        0.0255 | 0.0211 | 0.0024 |
|                  15 |   75 |                        0.0217 | 0.0220 | 0.0025 |

## Toy Regression Baseline

早期的 synthetic regression smoke test 仍然可以執行：

```bash
uv run python scripts/run_toy_regression.py --budget 20 --seeds 5
```
