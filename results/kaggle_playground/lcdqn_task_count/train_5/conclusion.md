# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 0.0000 | 1.00 | 15 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| CrossDataset-LC-DQN | 15 |

Most rank-1 finishes: **CrossDataset-LC-DQN** with 15 task(s).

Across the selected tasks, **CrossDataset-LC-DQN** gives the best average simple regret (0.0000). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-DQN tests the paper-style DQN setup with a configurable sequence encoder (default: LSTM), and OurMethod-LC-DQN adds learning-curve and derivative state features.

## Per-Task Rankings

### playground-series-s3e1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 0.6633 | 0.6608 | 0.0000 |

### playground-series-s3e11

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 29.7661 | 29.7873 | 0.0000 |

### playground-series-s3e14

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 615.1714 | 543.2274 | 0.0000 |

### playground-series-s3e16

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 2.0425 | 2.0731 | 0.0000 |

### playground-series-s3e25

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 1.3422 | 1.3167 | 0.0000 |

### playground-series-s3e6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 133344.4149 | 277895.3399 | 0.0000 |

### playground-series-s3e8

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 736.1051 | 704.3539 | 0.0000 |

### playground-series-s3e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 11.9717 | 12.4950 | 0.0000 |

### playground-series-s4e12

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 868.6984 | 863.8228 | 0.0000 |

### playground-series-s4e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 1.9243 | 1.8964 | 0.0000 |

### playground-series-s4e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 0.0206 | 0.0204 | 0.0000 |

### playground-series-s4e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 67555.5432 | 79788.7633 | 0.0000 |

### playground-series-s5e2

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 39.0979 | 39.0274 | 0.0000 |

### playground-series-s5e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 13.8134 | 13.7090 | 0.0000 |

### playground-series-s5e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 4.1871 | 4.3110 | 0.0000 |
