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
| 1 | CrossDataset-LC-DQN | 0.6627 | 0.6636 | 0.0000 |

### playground-series-s3e11

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 29.7643 | 29.7880 | 0.0000 |

### playground-series-s3e14

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 614.7552 | 540.9330 | 0.0000 |

### playground-series-s3e16

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 2.0436 | 2.0750 | 0.0000 |

### playground-series-s3e25

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 1.3428 | 1.3186 | 0.0000 |

### playground-series-s3e6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 135937.4359 | 278432.2501 | 0.0000 |

### playground-series-s3e8

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 721.2446 | 693.2271 | 0.0000 |

### playground-series-s3e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 11.9622 | 12.5652 | 0.0000 |

### playground-series-s4e12

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 869.0667 | 864.1602 | 0.0000 |

### playground-series-s4e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 1.9293 | 1.8910 | 0.0000 |

### playground-series-s4e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 0.0206 | 0.0205 | 0.0000 |

### playground-series-s4e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 67550.1786 | 79773.1876 | 0.0000 |

### playground-series-s5e2

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 39.1064 | 39.0364 | 0.0000 |

### playground-series-s5e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 13.7150 | 13.6218 | 0.0000 |

### playground-series-s5e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 4.2736 | 4.3857 | 0.0000 |
