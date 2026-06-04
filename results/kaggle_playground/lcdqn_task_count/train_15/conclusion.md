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
| 1 | CrossDataset-LC-DQN | 0.6651 | 0.6616 | 0.0000 |

### playground-series-s3e11

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 29.7544 | 29.7725 | 0.0000 |

### playground-series-s3e14

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 613.1653 | 541.2888 | 0.0000 |

### playground-series-s3e16

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 2.0437 | 2.0756 | 0.0000 |

### playground-series-s3e25

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 1.3437 | 1.3211 | 0.0000 |

### playground-series-s3e6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 127598.2219 | 275412.8469 | 0.0000 |

### playground-series-s3e8

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 741.8713 | 728.2181 | 0.0000 |

### playground-series-s3e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 11.9380 | 12.5032 | 0.0000 |

### playground-series-s4e12

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 868.9822 | 864.0496 | 0.0000 |

### playground-series-s4e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 1.9181 | 1.8930 | 0.0000 |

### playground-series-s4e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 0.0207 | 0.0206 | 0.0000 |

### playground-series-s4e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 67466.2126 | 79699.7533 | 0.0000 |

### playground-series-s5e2

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 39.1008 | 39.0305 | 0.0000 |

### playground-series-s5e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 13.7950 | 13.6990 | 0.0000 |

### playground-series-s5e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 4.1788 | 4.3030 | 0.0000 |
