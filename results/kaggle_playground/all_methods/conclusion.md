# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 221.1293 | 1.67 | 15 |
| 2 | CrossDataset-LC-DQN | 453.9626 | 2.33 | 15 |
| 3 | CrossDataset-HyperRL | 769.7329 | 2.87 | 15 |
| 4 | Random Search | 803.1709 | 3.13 | 15 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 9 |
| CrossDataset-LC-DQN | 4 |
| CrossDataset-HyperRL | 2 |
| Random Search | 0 |

Most rank-1 finishes: **Bayesian Optimization** with 9 task(s).

Across the selected tasks, **Bayesian Optimization** gives the best average simple regret (221.1293). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-DQN tests the paper-style DQN setup with a configurable sequence encoder (default: LSTM), and OurMethod-LC-DQN adds learning-curve and derivative state features.

## Per-Task Rankings

### playground-series-s3e1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.6609 | 0.6606 | 0.0000 |
| 2 | Random Search | 0.6645 | 0.6619 | 0.0036 |
| 3 | CrossDataset-LC-DQN | 0.6651 | 0.6616 | 0.0042 |
| 4 | CrossDataset-HyperRL | 0.6669 | 0.6664 | 0.0061 |

### playground-series-s3e11

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.7338 | 29.7581 | 0.0087 |
| 2 | CrossDataset-LC-DQN | 29.7544 | 29.7725 | 0.0293 |
| 3 | CrossDataset-HyperRL | 29.7619 | 29.7806 | 0.0369 |
| 4 | Random Search | 29.7645 | 29.7806 | 0.0394 |

### playground-series-s3e14

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 613.1653 | 541.2888 | 0.1438 |
| 2 | CrossDataset-HyperRL | 613.5515 | 539.5589 | 0.5300 |
| 3 | Bayesian Optimization | 614.9782 | 542.6470 | 1.9567 |
| 4 | Random Search | 615.1853 | 542.8558 | 2.1638 |

### playground-series-s3e16

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 2.0424 | 2.0713 | 0.0018 |
| 2 | CrossDataset-LC-DQN | 2.0437 | 2.0756 | 0.0031 |
| 3 | Random Search | 2.0453 | 2.0794 | 0.0047 |
| 4 | CrossDataset-HyperRL | 2.0454 | 2.0764 | 0.0048 |

### playground-series-s3e25

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 1.3412 | 1.3145 | 0.0010 |
| 2 | Bayesian Optimization | 1.3428 | 1.3209 | 0.0026 |
| 3 | Random Search | 1.3431 | 1.3193 | 0.0029 |
| 4 | CrossDataset-LC-DQN | 1.3437 | 1.3211 | 0.0034 |

### playground-series-s3e6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 124162.5538 | 271754.7355 | 3233.2060 |
| 2 | CrossDataset-LC-DQN | 127598.2219 | 275412.8469 | 6668.8741 |
| 3 | CrossDataset-HyperRL | 131923.0207 | 277468.2761 | 10993.6730 |
| 4 | Random Search | 132737.3302 | 278756.3187 | 11807.9824 |

### playground-series-s3e8

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 717.7009 | 699.7819 | 14.4159 |
| 2 | Random Search | 721.8392 | 694.6135 | 18.5542 |
| 3 | CrossDataset-HyperRL | 740.9955 | 696.6543 | 37.7104 |
| 4 | CrossDataset-LC-DQN | 741.8713 | 728.2181 | 38.5863 |

### playground-series-s3e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 11.9380 | 12.5032 | 0.0154 |
| 2 | Bayesian Optimization | 11.9461 | 12.5255 | 0.0235 |
| 3 | Random Search | 11.9560 | 12.5048 | 0.0335 |
| 4 | CrossDataset-HyperRL | 11.9639 | 12.5302 | 0.0414 |

### playground-series-s4e12

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 868.7416 | 863.8520 | 0.1199 |
| 2 | CrossDataset-LC-DQN | 868.9822 | 864.0496 | 0.3605 |
| 3 | Random Search | 869.4274 | 864.3180 | 0.8057 |
| 4 | Bayesian Optimization | 869.7946 | 864.6394 | 1.1729 |

### playground-series-s4e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 1.9181 | 1.8930 | 0.0024 |
| 2 | Bayesian Optimization | 1.9188 | 1.8891 | 0.0031 |
| 3 | CrossDataset-HyperRL | 1.9267 | 1.9013 | 0.0109 |
| 4 | Random Search | 1.9314 | 1.9055 | 0.0157 |

### playground-series-s4e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.0206 | 0.0205 | 0.0000 |
| 2 | Random Search | 0.0206 | 0.0205 | 0.0001 |
| 3 | CrossDataset-LC-DQN | 0.0207 | 0.0206 | 0.0002 |
| 4 | CrossDataset-HyperRL | 0.0207 | 0.0206 | 0.0002 |

### playground-series-s4e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 67431.1094 | 79660.7228 | 66.0337 |
| 2 | CrossDataset-LC-DQN | 67466.2126 | 79699.7533 | 101.1369 |
| 3 | Random Search | 67582.7006 | 79803.6886 | 217.6249 |
| 4 | CrossDataset-HyperRL | 67878.7172 | 80136.6217 | 513.6416 |

### playground-series-s5e2

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 39.1008 | 39.0305 | 0.0072 |
| 2 | CrossDataset-HyperRL | 39.1037 | 39.0339 | 0.0100 |
| 3 | Bayesian Optimization | 39.1175 | 39.0460 | 0.0239 |
| 4 | Random Search | 39.1234 | 39.0545 | 0.0298 |

### playground-series-s5e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 13.6305 | 13.5444 | 0.0092 |
| 2 | Random Search | 13.7291 | 13.6341 | 0.1079 |
| 3 | CrossDataset-HyperRL | 13.7296 | 13.6277 | 0.1083 |
| 4 | CrossDataset-LC-DQN | 13.7950 | 13.6990 | 0.1737 |

### playground-series-s5e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 4.1614 | 4.2812 | 0.0811 |
| 2 | CrossDataset-HyperRL | 4.1788 | 4.3030 | 0.0984 |
| 3 | CrossDataset-LC-DQN | 4.1788 | 4.3030 | 0.0984 |
| 4 | Random Search | 4.2761 | 4.3870 | 0.1958 |
