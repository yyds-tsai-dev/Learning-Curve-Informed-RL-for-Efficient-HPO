# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 1.9608 | 2.69 | 35 |
| 2 | CrossDataset-HyperRL | 2.0097 | 2.77 | 35 |
| 3 | Bayesian Optimization | 2.3101 | 1.37 | 35 |
| 4 | CrossDataset-LC-DQN | 4.4337 | 3.17 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 27 |
| Random Search | 10 |
| CrossDataset-LC-DQN | 6 |
| CrossDataset-HyperRL | 5 |

Most rank-1 finishes: **Bayesian Optimization** with 27 task(s).

Across the selected tasks, **Random Search** gives the best average simple regret (1.9608). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-DQN tests the paper-style DQN setup with a configurable sequence encoder (default: LSTM), and OurMethod-LC-DQN adds learning-curve and derivative state features.

## Per-Task Rankings

### lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.2795 | 1.2839 | 0.0000 |
| 2 | Random Search | 1.4639 | 1.6108 | 0.1845 |
| 3 | CrossDataset-HyperRL | 1.6306 | 1.6547 | 0.3511 |
| 4 | CrossDataset-LC-DQN | 1.7793 | 1.7743 | 0.4999 |

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
| 3 | CrossDataset-LC-DQN | 9.1503 | 16.2996 | 0.0000 |
| 4 | Random Search | 9.1503 | 16.2996 | 0.0000 |

### lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 11.9718 | 11.2251 | 0.0000 |
| 2 | Random Search | 13.2963 | 12.5325 | 1.3245 |
| 3 | CrossDataset-HyperRL | 13.7033 | 12.7186 | 1.7315 |
| 4 | CrossDataset-LC-DQN | 15.7320 | 14.6580 | 3.7602 |

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
| 2 | Random Search | 12.6578 | 12.8722 | 1.9230 |
| 3 | CrossDataset-HyperRL | 13.0229 | 13.3149 | 2.2881 |
| 4 | CrossDataset-LC-DQN | 13.0229 | 13.3149 | 2.2881 |

### lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 19.4630 | 19.4701 | 0.0000 |
| 2 | Random Search | 19.4630 | 19.4763 | 0.0000 |
| 3 | CrossDataset-HyperRL | 19.9907 | 20.0534 | 0.5278 |
| 4 | CrossDataset-LC-DQN | 20.0185 | 19.9541 | 0.5556 |

### lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 38.0016 | 38.1855 | 0.0000 |
| 2 | Random Search | 40.6270 | 40.7777 | 2.6254 |
| 3 | CrossDataset-HyperRL | 41.1972 | 41.1102 | 3.1956 |
| 4 | CrossDataset-LC-DQN | 41.2065 | 41.1653 | 3.2048 |

### lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 35.1698 | 34.8944 | 0.0000 |
| 2 | CrossDataset-HyperRL | 35.4580 | 35.2621 | 0.2882 |
| 3 | Bayesian Optimization | 35.8026 | 35.5757 | 0.6328 |
| 4 | CrossDataset-LC-DQN | 36.0994 | 35.9135 | 0.9296 |

### lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 11.8836 | 11.7166 | 0.0000 |
| 2 | Random Search | 12.0636 | 11.2943 | 0.1801 |
| 3 | CrossDataset-LC-DQN | 14.5744 | 14.4782 | 2.6908 |
| 4 | Bayesian Optimization | 16.2749 | 16.7370 | 4.3913 |

### lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 21.0843 | 19.1057 | 0.0000 |
| 2 | CrossDataset-HyperRL | 22.2892 | 17.0732 | 1.2048 |
| 3 | CrossDataset-LC-DQN | 22.2892 | 19.9187 | 1.2048 |
| 4 | Random Search | 31.9277 | 26.0163 | 10.8434 |

### lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 9.1384 | 13.1579 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 9.9217 | 15.0877 | 0.7833 |
| 3 | Random Search | 14.8825 | 19.4737 | 5.7441 |
| 4 | CrossDataset-HyperRL | 16.1880 | 20.7018 | 7.0496 |

### lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 26.4608 | 27.6286 | 0.0000 |
| 2 | Random Search | 27.0451 | 28.2998 | 0.5843 |
| 3 | Bayesian Optimization | 27.3790 | 27.4049 | 0.9182 |
| 4 | CrossDataset-HyperRL | 27.5459 | 27.8523 | 1.0851 |

### lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 3.3473 | 5.3371 | 0.0000 |
| 2 | Bayesian Optimization | 3.7657 | 5.8989 | 0.4184 |
| 3 | CrossDataset-HyperRL | 4.1841 | 5.3371 | 0.8368 |
| 4 | Random Search | 4.6025 | 8.1461 | 1.2552 |

### lcbench_connect-4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.4484 | 28.4708 | 0.0000 |
| 2 | CrossDataset-HyperRL | 34.5160 | 34.2888 | 5.0676 |
| 3 | CrossDataset-LC-DQN | 34.5160 | 34.2888 | 5.0676 |
| 4 | Random Search | 34.5160 | 34.2888 | 5.0676 |

### lcbench_covertype

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.5901 | 29.4262 | 0.0000 |
| 2 | Random Search | 33.8178 | 33.6054 | 4.2277 |
| 3 | CrossDataset-HyperRL | 36.2660 | 36.2106 | 6.6759 |
| 4 | CrossDataset-LC-DQN | 36.5976 | 36.3655 | 7.0075 |

### lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.1261 | 28.7879 | 0.0000 |
| 2 | Random Search | 27.4775 | 32.1212 | 1.3513 |
| 3 | CrossDataset-HyperRL | 28.3784 | 30.3030 | 2.2523 |
| 4 | CrossDataset-LC-DQN | 28.3784 | 28.7879 | 2.2523 |

### lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 0.2502 | 0.2282 | 0.0000 |
| 2 | Bayesian Optimization | 0.4164 | 0.3738 | 0.1663 |
| 3 | CrossDataset-HyperRL | 0.4164 | 0.3738 | 0.1663 |
| 4 | Random Search | 0.4164 | 0.3738 | 0.1663 |

### lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.1137 | 35.6013 | 0.0000 |
| 2 | CrossDataset-HyperRL | 33.6628 | 35.6381 | 0.5491 |
| 3 | CrossDataset-LC-DQN | 33.7727 | 35.1600 | 0.6590 |
| 4 | Random Search | 34.4316 | 34.7186 | 1.3180 |

### lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 0.3548 | 0.3911 | 0.0000 |
| 2 | CrossDataset-HyperRL | 0.4589 | 0.4237 | 0.1041 |
| 3 | Bayesian Optimization | 71.7378 | 72.3821 | 71.3829 |
| 4 | CrossDataset-LC-DQN | 81.5747 | 82.1566 | 81.2199 |

### lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.5249 | 29.7565 | 0.0000 |
| 2 | Random Search | 31.4529 | 30.9680 | 1.9280 |
| 3 | CrossDataset-HyperRL | 32.0803 | 31.8488 | 2.5554 |
| 4 | CrossDataset-LC-DQN | 34.2251 | 34.3677 | 4.7002 |

### lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 37.7984 | 37.3589 | 0.0000 |
| 2 | Bayesian Optimization | 39.1217 | 38.4663 | 1.3233 |
| 3 | CrossDataset-LC-DQN | 39.7753 | 39.5628 | 1.9769 |
| 4 | CrossDataset-HyperRL | 40.8178 | 40.2577 | 3.0193 |

### lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.3056 | 24.7967 | 0.0000 |
| 2 | CrossDataset-HyperRL | 18.3056 | 23.9837 | 0.0000 |
| 3 | Random Search | 18.3056 | 23.5772 | 0.0000 |
| 4 | CrossDataset-LC-DQN | 18.4569 | 24.0854 | 0.1513 |

### lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 20.6761 | 19.3171 | 0.0000 |
| 2 | Random Search | 26.4884 | 25.3076 | 5.8123 |
| 3 | CrossDataset-HyperRL | 32.6640 | 31.7309 | 11.9879 |
| 4 | CrossDataset-LC-DQN | 33.0474 | 32.0149 | 12.3713 |

### lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 13.7045 | 14.8201 | 0.0000 |
| 2 | Random Search | 14.9893 | 15.2518 | 1.2848 |
| 3 | CrossDataset-HyperRL | 17.3448 | 16.6906 | 3.6403 |
| 4 | CrossDataset-LC-DQN | 19.7002 | 20.5755 | 5.9957 |

### lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.9802 | 2.5617 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 2.2631 | 2.9412 | 0.2829 |
| 3 | Random Search | 3.1117 | 3.3207 | 1.1315 |
| 4 | CrossDataset-HyperRL | 4.1018 | 3.3207 | 2.1216 |

### lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 2.9345 | 1.9697 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 3.3860 | 1.8182 | 0.4515 |
| 3 | CrossDataset-HyperRL | 3.6117 | 1.9697 | 0.6772 |
| 4 | Random Search | 4.5147 | 3.9394 | 1.5801 |

### lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 4.7238 | 4.9327 | 0.0000 |
| 2 | Random Search | 5.0125 | 5.0998 | 0.2887 |
| 3 | CrossDataset-HyperRL | 5.6948 | 5.6977 | 0.9710 |
| 4 | CrossDataset-LC-DQN | 5.8916 | 5.9527 | 1.1678 |

### lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 48.1101 | 47.8087 | 0.0000 |
| 2 | Random Search | 48.1101 | 47.8087 | 0.0000 |
| 3 | CrossDataset-HyperRL | 48.1335 | 47.5853 | 0.0235 |
| 4 | CrossDataset-LC-DQN | 48.1852 | 47.6325 | 0.0751 |

### lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 21.0879 | 21.5367 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 21.9247 | 21.7050 | 0.8368 |
| 3 | CrossDataset-HyperRL | 22.1757 | 23.3315 | 1.0879 |
| 4 | Random Search | 22.9289 | 22.7145 | 1.8410 |

### lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 13.5029 | 12.2047 | 0.0000 |
| 2 | CrossDataset-HyperRL | 15.8513 | 14.8294 | 2.3483 |
| 3 | CrossDataset-LC-DQN | 15.8513 | 14.9606 | 2.3483 |
| 4 | Random Search | 16.6340 | 16.2730 | 3.1311 |

### lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.3041 | 0.2456 | 0.0000 |
| 2 | Random Search | 2.1132 | 2.0481 | 1.8091 |
| 3 | CrossDataset-HyperRL | 2.1288 | 2.0794 | 1.8247 |
| 4 | CrossDataset-LC-DQN | 2.1678 | 2.2884 | 1.8637 |

### lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.3792 | 7.4556 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 5.9965 | 7.6331 | 0.6173 |
| 3 | Random Search | 6.7019 | 7.9290 | 1.3228 |
| 4 | CrossDataset-HyperRL | 7.4956 | 8.9349 | 2.1164 |

### lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.6170 | 31.1828 | 0.0000 |
| 2 | CrossDataset-HyperRL | 21.2766 | 26.1649 | 2.6596 |
| 3 | CrossDataset-LC-DQN | 26.0638 | 25.0896 | 7.4468 |
| 4 | Random Search | 30.3191 | 29.0323 | 11.7021 |

### lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 46.8239 | 46.8118 | 0.0000 |
| 2 | Bayesian Optimization | 48.4449 | 48.3708 | 1.6210 |
| 3 | CrossDataset-HyperRL | 48.7551 | 48.4748 | 1.9313 |
| 4 | CrossDataset-LC-DQN | 49.5928 | 49.2855 | 2.7689 |
