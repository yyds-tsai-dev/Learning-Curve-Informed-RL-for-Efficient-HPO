# LCBench Budget Sweep

Data source: official LCBench lightweight archive from figshare.

- Download URL: https://ndownloader.figshare.com/files/21188598
- Local JSON: `data/lcbench/data_2k_lw.json`
- Datasets: `credit-g`, `Fashion-MNIST`, `Australian`, `adult`, `bank-marketing`, `MiniBooNE`, `APSFailure`
- Seeds: 5
- Metric: validation score, computed as `100 - accuracy`; lower is better

## Overall Comparison

| Budget | Rank | Method | Avg simple regret | Avg per-task rank |
| ---: | ---: | --- | ---: | ---: |
| 20 | 1 | Bayesian Optimization | 0.6531 | 2.29 |
| 20 | 2 | Random Search | 0.7840 | 2.00 |
| 20 | 3 | OurMethod-LC-DQN-MLP | 0.9583 | 2.71 |
| 20 | 4 | HyperRL-MLP | 1.0090 | 3.00 |
| 50 | 1 | Bayesian Optimization | 0.1959 | 1.29 |
| 50 | 2 | Random Search | 0.5804 | 2.29 |
| 50 | 3 | OurMethod-LC-DQN-MLP | 0.6703 | 3.14 |
| 50 | 4 | HyperRL-MLP | 0.8639 | 3.29 |
| 100 | 1 | Bayesian Optimization | 0.3193 | 1.29 |
| 100 | 2 | HyperRL-MLP | 0.5398 | 2.86 |
| 100 | 3 | OurMethod-LC-DQN-MLP | 0.5779 | 2.71 |
| 100 | 4 | Random Search | 0.7272 | 3.14 |

## Takeaways

Longer budgets help the DQN-based methods. Our method improves monotonically in average simple
regret as budget increases: `0.9583 -> 0.6703 -> 0.5779`.

The learning-curve features help relative to HyperRL-MLP at budgets 20 and 50. At budget 100,
HyperRL-MLP has slightly lower average simple regret, while OurMethod-LC-DQN-MLP has the better
average per-task rank.

Bayesian Optimization remains the strongest overall method in this sweep. This suggests that simply
increasing the budget is not enough for the current online MLP-DQN to consistently beat BO; the next
likely improvement is cross-dataset pretraining or tuning the DQN reward/exploration schedule.
