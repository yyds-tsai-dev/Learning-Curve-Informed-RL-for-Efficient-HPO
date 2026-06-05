# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1547.4892 | 2.00 | 15 |
| 2 | CrossDataset-LC-DQN | 1663.3846 | 2.40 | 15 |
| 3 | Random Search | 2398.8204 | 2.73 | 15 |
| 4 | CrossDataset-HyperRL | 2576.0170 | 2.87 | 15 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 8 |
| CrossDataset-HyperRL | 3 |
| CrossDataset-LC-DQN | 3 |
| Random Search | 1 |

Most rank-1 finishes: **Bayesian Optimization** with 8 task(s).

Across the selected tasks, **Bayesian Optimization** gives the best average simple regret (1547.4892). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-DQN tests the paper-style DQN setup with a configurable sequence encoder (default: LSTM), and OurMethod-LC-DQN adds learning-curve and derivative state features.

## Per-Task Rankings

### playground-series-s3e1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.6632 | 0.6618 | 0.0019 |
| 2 | CrossDataset-LC-DQN | 0.6635 | 0.6599 | 0.0021 |
| 3 | CrossDataset-HyperRL | 0.6640 | 0.6646 | 0.0026 |
| 4 | Random Search | 0.6685 | 0.6664 | 0.0071 |

### playground-series-s3e11

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.7514 | 29.7734 | 0.0118 |
| 2 | CrossDataset-HyperRL | 29.7629 | 29.7780 | 0.0234 |
| 3 | Random Search | 29.7863 | 29.8022 | 0.0468 |
| 4 | CrossDataset-LC-DQN | 29.8366 | 29.8486 | 0.0970 |

### playground-series-s3e14

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 614.6634 | 543.5549 | 1.2940 |
| 2 | Random Search | 615.3499 | 542.4579 | 1.9805 |
| 3 | Bayesian Optimization | 615.4365 | 541.6705 | 2.0671 |
| 4 | CrossDataset-LC-DQN | 615.7635 | 540.5902 | 2.3940 |

### playground-series-s3e16

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 2.0454 | 2.0738 | 0.0018 |
| 2 | Bayesian Optimization | 2.0458 | 2.0727 | 0.0022 |
| 3 | Random Search | 2.0469 | 2.0793 | 0.0033 |
| 4 | CrossDataset-HyperRL | 2.0506 | 2.0777 | 0.0070 |

### playground-series-s3e25

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 1.3414 | 1.3146 | 0.0023 |
| 2 | CrossDataset-LC-DQN | 1.3418 | 1.3153 | 0.0027 |
| 3 | Bayesian Optimization | 1.3429 | 1.3215 | 0.0038 |
| 4 | Random Search | 1.3432 | 1.3199 | 0.0041 |

### playground-series-s3e6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 145376.7128 | 285410.5969 | 23019.7817 |
| 2 | CrossDataset-LC-DQN | 146493.3095 | 283772.8767 | 24136.3784 |
| 3 | Random Search | 158064.8557 | 290527.0958 | 35707.9246 |
| 4 | CrossDataset-HyperRL | 160340.2245 | 291471.1542 | 37983.2934 |

### playground-series-s3e8

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 719.8273 | 698.7100 | 11.2136 |
| 2 | CrossDataset-LC-DQN | 720.7883 | 698.0560 | 12.1745 |
| 3 | Random Search | 735.3080 | 708.1007 | 26.6943 |
| 4 | CrossDataset-HyperRL | 739.0402 | 701.7367 | 30.4264 |

### playground-series-s3e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 11.9576 | 12.4780 | 0.0274 |
| 2 | Random Search | 11.9591 | 12.5097 | 0.0289 |
| 3 | CrossDataset-HyperRL | 11.9656 | 12.4843 | 0.0354 |
| 4 | Bayesian Optimization | 11.9726 | 12.5199 | 0.0424 |

### playground-series-s4e12

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 869.9893 | 864.9138 | 0.7930 |
| 2 | Random Search | 870.3002 | 864.9110 | 1.1039 |
| 3 | Bayesian Optimization | 871.4307 | 866.0595 | 2.2344 |
| 4 | CrossDataset-HyperRL | 871.5341 | 868.4179 | 2.3378 |

### playground-series-s4e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.9251 | 1.8939 | 0.0079 |
| 2 | CrossDataset-LC-DQN | 1.9254 | 1.8929 | 0.0082 |
| 3 | CrossDataset-HyperRL | 1.9333 | 1.9024 | 0.0160 |
| 4 | Random Search | 1.9360 | 1.8982 | 0.0188 |

### playground-series-s4e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.0206 | 0.0205 | 0.0001 |
| 2 | CrossDataset-HyperRL | 0.0207 | 0.0206 | 0.0001 |
| 3 | CrossDataset-LC-DQN | 0.0207 | 0.0206 | 0.0001 |
| 4 | Random Search | 0.0207 | 0.0206 | 0.0001 |

### playground-series-s4e9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 67668.2956 | 79919.7968 | 176.4305 |
| 2 | Random Search | 67735.9884 | 79918.8568 | 244.1233 |
| 3 | CrossDataset-HyperRL | 68113.9379 | 80273.2707 | 622.0728 |
| 4 | CrossDataset-LC-DQN | 68290.1513 | 80405.0542 | 798.2862 |

### playground-series-s5e2

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 39.1168 | 39.0474 | 0.0100 |
| 2 | Random Search | 39.1558 | 39.0893 | 0.0490 |
| 3 | CrossDataset-LC-DQN | 39.1737 | 39.0964 | 0.0670 |
| 4 | Bayesian Optimization | 39.2553 | 39.1822 | 0.1485 |

### playground-series-s5e4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 13.7855 | 13.6854 | 0.1186 |
| 2 | CrossDataset-LC-DQN | 13.8950 | 13.7752 | 0.2281 |
| 3 | Bayesian Optimization | 13.9154 | 13.8261 | 0.2484 |
| 4 | CrossDataset-HyperRL | 13.9345 | 13.8352 | 0.2676 |

### playground-series-s5e5

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 4.2176 | 4.3400 | 0.1439 |
| 2 | Random Search | 4.2761 | 4.3870 | 0.2024 |
| 3 | CrossDataset-LC-DQN | 4.3815 | 4.5114 | 0.3078 |
| 4 | CrossDataset-HyperRL | 4.5404 | 4.6694 | 0.4667 |
