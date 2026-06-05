# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 1.9301 | 2.60 | 35 |
| 2 | Random Search | 1.9679 | 2.89 | 35 |
| 3 | Bayesian Optimization | 2.3172 | 1.40 | 35 |
| 4 | CrossDataset-HyperRL | 4.8779 | 3.11 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 28 |
| Random Search | 8 |
| CrossDataset-LC-DQN | 6 |
| CrossDataset-HyperRL | 5 |

Most rank-1 finishes: **Bayesian Optimization** with 28 task(s).

Across the selected tasks, **CrossDataset-LC-DQN** gives the best average simple regret (1.9301). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-DQN tests the paper-style DQN setup with a configurable sequence encoder (default: LSTM), and OurMethod-LC-DQN adds learning-curve and derivative state features.

## Per-Task Rankings

### lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.2795 | 1.2839 | 0.0000 |
| 2 | Random Search | 1.4639 | 1.6108 | 0.1845 |
| 3 | CrossDataset-HyperRL | 1.6306 | 1.6547 | 0.3511 |
| 4 | CrossDataset-LC-DQN | 2.0471 | 2.0774 | 0.7677 |

### lcbench_Amazon_employee_access

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.9205 | 5.7888 | 0.0000 |
| 2 | CrossDataset-HyperRL | 5.9205 | 5.7888 | 0.0000 |
| 3 | CrossDataset-LC-DQN | 5.9205 | 5.7888 | 0.0000 |
| 4 | Random Search | 5.9205 | 5.7888 | 0.0000 |

### lcbench_Australian

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 9.1503 | 16.2996 | 0.0000 |
| 2 | CrossDataset-HyperRL | 9.1503 | 16.2996 | 0.0000 |
| 3 | Random Search | 9.1503 | 16.2996 | 0.0000 |
| 4 | CrossDataset-LC-DQN | 9.8039 | 16.7401 | 0.6536 |

### lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 11.9718 | 11.2251 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 12.7730 | 12.0346 | 0.8011 |
| 3 | Random Search | 13.2963 | 12.5325 | 1.3245 |
| 4 | CrossDataset-HyperRL | 15.3831 | 14.5714 | 3.4113 |

### lcbench_KDDCup09_appetency

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.6733 | 1.7818 | 0.0000 |
| 2 | CrossDataset-HyperRL | 1.6733 | 1.7818 | 0.0000 |
| 3 | CrossDataset-LC-DQN | 1.6733 | 1.7818 | 0.0000 |
| 4 | Random Search | 1.6733 | 1.7818 | 0.0000 |

### lcbench_MiniBooNE

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.7348 | 10.9781 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 12.3344 | 12.6392 | 1.5996 |
| 3 | Random Search | 12.6578 | 12.8722 | 1.9230 |
| 4 | CrossDataset-HyperRL | 13.6315 | 13.9392 | 2.8967 |

### lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 19.4630 | 19.4701 | 0.0000 |
| 2 | Random Search | 19.4630 | 19.4763 | 0.0000 |
| 3 | CrossDataset-LC-DQN | 19.7963 | 20.0782 | 0.3333 |
| 4 | CrossDataset-HyperRL | 20.0833 | 20.0161 | 0.6204 |

### lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 38.0016 | 38.1855 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 40.5147 | 40.5709 | 2.5130 |
| 3 | Random Search | 40.6270 | 40.7777 | 2.6254 |
| 4 | CrossDataset-HyperRL | 40.8283 | 40.8215 | 2.8266 |

### lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 35.1060 | 34.8709 | 0.0000 |
| 2 | Random Search | 35.1698 | 34.8944 | 0.0638 |
| 3 | Bayesian Optimization | 35.8026 | 35.5757 | 0.6967 |
| 4 | CrossDataset-HyperRL | 36.4610 | 36.3033 | 1.3550 |

### lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 11.7535 | 11.6228 | 0.0000 |
| 2 | Random Search | 12.0636 | 11.2943 | 0.3101 |
| 3 | Bayesian Optimization | 16.2749 | 16.7370 | 4.5214 |
| 4 | CrossDataset-LC-DQN | 17.0951 | 17.4945 | 5.3416 |

### lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 21.0843 | 19.1057 | 0.0000 |
| 2 | CrossDataset-HyperRL | 22.2892 | 19.9187 | 1.2048 |
| 3 | CrossDataset-LC-DQN | 22.2892 | 19.9187 | 1.2048 |
| 4 | Random Search | 31.9277 | 26.0163 | 10.8434 |

### lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 9.1384 | 13.1579 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 13.5770 | 19.1228 | 4.4386 |
| 3 | Random Search | 14.8825 | 19.4737 | 5.7441 |
| 4 | CrossDataset-HyperRL | 19.0601 | 23.1579 | 9.9217 |

### lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 26.2104 | 27.8523 | 0.0000 |
| 2 | Random Search | 27.0451 | 28.2998 | 0.8347 |
| 3 | CrossDataset-LC-DQN | 27.2120 | 28.5235 | 1.0017 |
| 4 | Bayesian Optimization | 27.3790 | 27.4049 | 1.1686 |

### lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.7657 | 5.8989 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 3.7657 | 7.0225 | 0.0000 |
| 3 | Random Search | 4.6025 | 8.1461 | 0.8368 |
| 4 | CrossDataset-HyperRL | 5.0209 | 6.4607 | 1.2552 |

### lcbench_connect-4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.4484 | 28.4708 | 0.0000 |
| 2 | CrossDataset-HyperRL | 34.5026 | 34.2978 | 5.0542 |
| 3 | CrossDataset-LC-DQN | 34.5160 | 34.2888 | 5.0676 |
| 4 | Random Search | 34.5160 | 34.2888 | 5.0676 |

### lcbench_covertype

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.5901 | 29.4262 | 0.0000 |
| 2 | Random Search | 33.8178 | 33.6054 | 4.2277 |
| 3 | CrossDataset-HyperRL | 36.1609 | 35.8205 | 6.5708 |
| 4 | CrossDataset-LC-DQN | 38.1607 | 37.9698 | 8.5706 |

### lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.1261 | 28.7879 | 0.0000 |
| 2 | CrossDataset-HyperRL | 27.0270 | 30.3030 | 0.9009 |
| 3 | CrossDataset-LC-DQN | 27.0270 | 30.3030 | 0.9009 |
| 4 | Random Search | 27.4775 | 32.1212 | 1.3513 |

### lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 0.0426 | 0.0607 | 0.0000 |
| 2 | CrossDataset-HyperRL | 0.2784 | 0.3207 | 0.2358 |
| 3 | Bayesian Optimization | 0.4164 | 0.3738 | 0.3738 |
| 4 | Random Search | 0.4164 | 0.3738 | 0.3738 |

### lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.1137 | 35.6013 | 0.0000 |
| 2 | CrossDataset-HyperRL | 33.8276 | 35.0497 | 0.7139 |
| 3 | CrossDataset-LC-DQN | 33.8825 | 35.3807 | 0.7688 |
| 4 | Random Search | 34.4316 | 34.7186 | 1.3180 |

### lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 0.3548 | 0.3911 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 0.7711 | 0.7211 | 0.4162 |
| 3 | Bayesian Optimization | 71.7378 | 72.3821 | 71.3829 |
| 4 | CrossDataset-HyperRL | 77.5373 | 77.8155 | 77.1824 |

### lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.5249 | 29.7565 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 30.7657 | 30.5229 | 1.2408 |
| 3 | Random Search | 31.4529 | 30.9680 | 1.9280 |
| 4 | CrossDataset-HyperRL | 36.5913 | 36.7876 | 7.0664 |

### lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 37.7984 | 37.3589 | 0.0000 |
| 2 | Bayesian Optimization | 39.1217 | 38.4663 | 1.3233 |
| 3 | CrossDataset-LC-DQN | 39.7213 | 38.8571 | 1.9229 |
| 4 | CrossDataset-HyperRL | 41.0500 | 40.5038 | 3.2516 |

### lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.3056 | 24.7967 | 0.0000 |
| 2 | Random Search | 18.3056 | 23.5772 | 0.0000 |
| 3 | CrossDataset-HyperRL | 18.6082 | 23.8821 | 0.3026 |
| 4 | CrossDataset-LC-DQN | 18.6082 | 23.5772 | 0.3026 |

### lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 20.6761 | 19.3171 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 25.6912 | 24.5909 | 5.0151 |
| 3 | Random Search | 26.4884 | 25.3076 | 5.8123 |
| 4 | CrossDataset-HyperRL | 35.1261 | 34.5977 | 14.4501 |

### lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 13.7045 | 14.8201 | 0.0000 |
| 2 | CrossDataset-HyperRL | 14.9893 | 14.3885 | 1.2848 |
| 3 | Random Search | 14.9893 | 15.2518 | 1.2848 |
| 4 | CrossDataset-LC-DQN | 19.2719 | 22.7338 | 5.5675 |

### lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.9802 | 2.5617 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 3.1117 | 3.1309 | 1.1315 |
| 3 | Random Search | 3.1117 | 3.3207 | 1.1315 |
| 4 | CrossDataset-HyperRL | 5.3748 | 5.3131 | 3.3946 |

### lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 2.9345 | 1.9697 | 0.0000 |
| 2 | CrossDataset-HyperRL | 3.8375 | 2.1212 | 0.9029 |
| 3 | CrossDataset-LC-DQN | 4.0632 | 2.5758 | 1.1287 |
| 4 | Random Search | 4.5147 | 3.9394 | 1.5801 |

### lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 4.7238 | 4.9327 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 4.8025 | 4.9591 | 0.0787 |
| 3 | Random Search | 5.0125 | 5.0998 | 0.2887 |
| 4 | CrossDataset-HyperRL | 6.1934 | 6.1725 | 1.4696 |

### lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 48.1101 | 47.8087 | 0.0000 |
| 2 | Random Search | 48.1101 | 47.8087 | 0.0000 |
| 3 | CrossDataset-LC-DQN | 48.1711 | 47.6357 | 0.0610 |
| 4 | CrossDataset-HyperRL | 48.3354 | 47.4501 | 0.2254 |

### lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 21.0879 | 21.5367 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 22.4268 | 22.7706 | 1.3389 |
| 3 | Random Search | 22.9289 | 22.7145 | 1.8410 |
| 4 | CrossDataset-HyperRL | 23.8494 | 23.7241 | 2.7615 |

### lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 13.5029 | 12.2047 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 16.2427 | 16.2730 | 2.7397 |
| 3 | Random Search | 16.6340 | 16.2730 | 3.1311 |
| 4 | CrossDataset-HyperRL | 17.4168 | 16.6667 | 3.9139 |

### lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.3041 | 0.2456 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 0.8986 | 0.8851 | 0.5945 |
| 3 | Random Search | 2.1132 | 2.0481 | 1.8091 |
| 4 | CrossDataset-HyperRL | 2.1444 | 2.0742 | 1.8403 |

### lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.3792 | 7.4556 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 6.2610 | 7.6923 | 0.8818 |
| 3 | Random Search | 6.7019 | 7.9290 | 1.3228 |
| 4 | CrossDataset-HyperRL | 8.3774 | 9.2308 | 2.9982 |

### lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.6170 | 31.1828 | 0.0000 |
| 2 | CrossDataset-HyperRL | 27.6596 | 31.1828 | 9.0426 |
| 3 | CrossDataset-LC-DQN | 29.7872 | 26.8817 | 11.1702 |
| 4 | Random Search | 30.3191 | 29.0323 | 11.7021 |

### lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 46.8083 | 46.8378 | 0.0000 |
| 2 | Random Search | 46.8239 | 46.8118 | 0.0155 |
| 3 | Bayesian Optimization | 48.4449 | 48.3708 | 1.6365 |
| 4 | CrossDataset-HyperRL | 50.1280 | 50.2105 | 3.3196 |
