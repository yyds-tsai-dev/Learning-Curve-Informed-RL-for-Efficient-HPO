# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 1.9787 | 2.49 | 35 |
| 2 | Bayesian Optimization | 2.3280 | 1.49 | 35 |
| 3 | CrossDataset-HyperRL | 2.6826 | 3.06 | 35 |
| 4 | CrossDataset-LC-DQN | 2.9141 | 2.97 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 27 |
| Random Search | 9 |
| CrossDataset-HyperRL | 6 |
| CrossDataset-LC-DQN | 6 |

Most rank-1 finishes: **Bayesian Optimization** with 27 task(s).

Across the selected tasks, **Random Search** gives the best average simple regret (1.9787). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-DQN tests the paper-style DQN setup with a configurable sequence encoder (default: LSTM), and OurMethod-LC-DQN adds learning-curve and derivative state features.

## Per-Task Rankings

### lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.2795 | 1.2839 | 0.0000 |
| 2 | Random Search | 1.4639 | 1.6108 | 0.1845 |
| 3 | CrossDataset-LC-DQN | 1.6306 | 1.6547 | 0.3511 |
| 4 | CrossDataset-HyperRL | 2.0531 | 2.0335 | 0.7736 |

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
| 2 | CrossDataset-LC-DQN | 9.1503 | 17.1806 | 0.0000 |
| 3 | Random Search | 9.1503 | 16.2996 | 0.0000 |
| 4 | CrossDataset-HyperRL | 9.8039 | 14.9780 | 0.6536 |

### lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 11.9718 | 11.2251 | 0.0000 |
| 2 | Random Search | 13.2963 | 12.5325 | 1.3245 |
| 3 | CrossDataset-HyperRL | 14.2525 | 13.3550 | 2.2807 |
| 4 | CrossDataset-LC-DQN | 14.3236 | 13.4502 | 2.3517 |

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
| 3 | CrossDataset-LC-DQN | 13.0229 | 13.3731 | 2.2881 |
| 4 | CrossDataset-HyperRL | 13.7775 | 14.0301 | 3.0427 |

### lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 19.4630 | 19.4701 | 0.0000 |
| 2 | Random Search | 19.4630 | 19.4763 | 0.0000 |
| 3 | CrossDataset-LC-DQN | 20.0648 | 20.2023 | 0.6019 |
| 4 | CrossDataset-HyperRL | 20.1204 | 20.4318 | 0.6574 |

### lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 38.0016 | 38.1855 | 0.0000 |
| 2 | Random Search | 40.6270 | 40.7777 | 2.6254 |
| 3 | CrossDataset-LC-DQN | 41.0782 | 41.0052 | 3.0765 |
| 4 | CrossDataset-HyperRL | 41.1645 | 41.1496 | 3.1629 |

### lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 35.1698 | 34.8944 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 35.4580 | 35.2621 | 0.2882 |
| 3 | CrossDataset-HyperRL | 35.7207 | 35.5244 | 0.5509 |
| 4 | Bayesian Optimization | 35.8026 | 35.5757 | 0.6328 |

### lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 11.5135 | 11.1133 | 0.0000 |
| 2 | Random Search | 12.0636 | 11.2943 | 0.5502 |
| 3 | CrossDataset-LC-DQN | 16.1448 | 16.1338 | 4.6314 |
| 4 | Bayesian Optimization | 16.2749 | 16.7370 | 4.7614 |

### lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 21.0843 | 19.1057 | 0.0000 |
| 2 | CrossDataset-HyperRL | 22.2892 | 19.9187 | 1.2048 |
| 3 | Random Search | 31.9277 | 26.0163 | 10.8434 |
| 4 | CrossDataset-LC-DQN | 37.3494 | 39.8374 | 16.2651 |

### lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 9.1384 | 13.1579 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 14.0992 | 19.1228 | 4.9608 |
| 3 | Random Search | 14.8825 | 19.4737 | 5.7441 |
| 4 | CrossDataset-HyperRL | 19.8433 | 26.3158 | 10.7050 |

### lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 26.4608 | 27.6286 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 26.4608 | 27.6286 | 0.0000 |
| 3 | Random Search | 27.0451 | 28.2998 | 0.5843 |
| 4 | Bayesian Optimization | 27.3790 | 27.4049 | 0.9182 |

### lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 3.3473 | 5.3371 | 0.0000 |
| 2 | Bayesian Optimization | 3.7657 | 5.8989 | 0.4184 |
| 3 | Random Search | 4.6025 | 8.1461 | 1.2552 |
| 4 | CrossDataset-HyperRL | 5.0209 | 6.4607 | 1.6736 |

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
| 3 | CrossDataset-LC-DQN | 36.1266 | 36.0870 | 6.5366 |
| 4 | CrossDataset-HyperRL | 37.4578 | 37.3403 | 7.8677 |

### lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.1261 | 28.7879 | 0.0000 |
| 2 | CrossDataset-HyperRL | 27.4775 | 27.8788 | 1.3513 |
| 3 | Random Search | 27.4775 | 32.1212 | 1.3513 |
| 4 | CrossDataset-LC-DQN | 27.9279 | 30.9091 | 1.8018 |

### lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 0.2784 | 0.3207 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 0.3241 | 0.3105 | 0.0456 |
| 3 | Bayesian Optimization | 0.4164 | 0.3738 | 0.1380 |
| 4 | Random Search | 0.4164 | 0.3738 | 0.1380 |

### lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.1137 | 35.6013 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 33.6628 | 35.0497 | 0.5491 |
| 3 | Random Search | 34.4316 | 34.7186 | 1.3180 |
| 4 | CrossDataset-HyperRL | 34.8709 | 36.4104 | 1.7573 |

### lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 0.0704 | 0.1401 | 0.0000 |
| 2 | Random Search | 0.3548 | 0.3911 | 0.2844 |
| 3 | CrossDataset-HyperRL | 0.6740 | 0.6561 | 0.6035 |
| 4 | Bayesian Optimization | 71.7378 | 72.3821 | 71.6674 |

### lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.5249 | 29.7565 | 0.0000 |
| 2 | Random Search | 31.4529 | 30.9680 | 1.9280 |
| 3 | CrossDataset-HyperRL | 32.7860 | 32.9831 | 3.2611 |
| 4 | CrossDataset-LC-DQN | 33.7177 | 33.8299 | 4.1928 |

### lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 37.7984 | 37.3589 | 0.0000 |
| 2 | Bayesian Optimization | 39.1217 | 38.4663 | 1.3233 |
| 3 | CrossDataset-LC-DQN | 41.0500 | 40.5038 | 3.2516 |
| 4 | CrossDataset-HyperRL | 41.7090 | 41.1371 | 3.9106 |

### lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.3056 | 24.7967 | 0.0000 |
| 2 | CrossDataset-HyperRL | 18.3056 | 23.8821 | 0.0000 |
| 3 | Random Search | 18.3056 | 23.5772 | 0.0000 |
| 4 | CrossDataset-LC-DQN | 18.6082 | 23.1707 | 0.3026 |

### lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 20.6761 | 19.3171 | 0.0000 |
| 2 | Random Search | 26.4884 | 25.3076 | 5.8123 |
| 3 | CrossDataset-HyperRL | 31.7356 | 31.4469 | 11.0595 |
| 4 | CrossDataset-LC-DQN | 33.0071 | 32.3191 | 12.3310 |

### lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 13.7045 | 14.8201 | 0.0000 |
| 2 | Random Search | 14.9893 | 15.2518 | 1.2848 |
| 3 | CrossDataset-HyperRL | 15.6317 | 15.1079 | 1.9272 |
| 4 | CrossDataset-LC-DQN | 20.1285 | 20.1439 | 6.4240 |

### lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.9802 | 2.5617 | 0.0000 |
| 2 | Random Search | 3.1117 | 3.3207 | 1.1315 |
| 3 | CrossDataset-LC-DQN | 3.6775 | 3.7951 | 1.6973 |
| 4 | CrossDataset-HyperRL | 5.7991 | 5.5977 | 3.8189 |

### lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 2.9345 | 1.9697 | 0.0000 |
| 2 | CrossDataset-HyperRL | 3.6117 | 2.1212 | 0.6772 |
| 3 | CrossDataset-LC-DQN | 4.0632 | 2.1212 | 1.1287 |
| 4 | Random Search | 4.5147 | 3.9394 | 1.5801 |

### lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 4.7238 | 4.9327 | 0.0000 |
| 2 | Random Search | 5.0125 | 5.0998 | 0.2887 |
| 3 | CrossDataset-HyperRL | 5.9179 | 5.9791 | 1.1941 |
| 4 | CrossDataset-LC-DQN | 5.9441 | 5.9263 | 1.2203 |

### lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 48.1101 | 47.8087 | 0.0000 |
| 2 | Random Search | 48.1101 | 47.8087 | 0.0000 |
| 3 | CrossDataset-LC-DQN | 48.2415 | 47.7395 | 0.1315 |
| 4 | CrossDataset-HyperRL | 48.3777 | 47.5570 | 0.2676 |

### lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 21.0879 | 21.5367 | 0.0000 |
| 2 | Random Search | 22.9289 | 22.7145 | 1.8410 |
| 3 | CrossDataset-LC-DQN | 23.9331 | 25.4066 | 2.8452 |
| 4 | CrossDataset-HyperRL | 24.6025 | 24.4532 | 3.5146 |

### lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 13.5029 | 12.2047 | 0.0000 |
| 2 | Random Search | 16.6340 | 16.2730 | 3.1311 |
| 3 | CrossDataset-HyperRL | 18.1996 | 16.9291 | 4.6967 |
| 4 | CrossDataset-LC-DQN | 18.1996 | 16.9291 | 4.6967 |

### lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.3041 | 0.2456 | 0.0000 |
| 2 | Random Search | 2.1132 | 2.0481 | 1.8091 |
| 3 | CrossDataset-HyperRL | 2.1444 | 2.0742 | 1.8403 |
| 4 | CrossDataset-LC-DQN | 2.5655 | 2.5078 | 2.2614 |

### lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.3792 | 7.4556 | 0.0000 |
| 2 | Random Search | 6.7019 | 7.9290 | 1.3228 |
| 3 | CrossDataset-LC-DQN | 6.7901 | 8.3432 | 1.4109 |
| 4 | CrossDataset-HyperRL | 9.1711 | 9.3491 | 3.7919 |

### lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.6170 | 31.1828 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 26.5957 | 29.7491 | 7.9787 |
| 3 | CrossDataset-HyperRL | 27.6596 | 30.4659 | 9.0426 |
| 4 | Random Search | 30.3191 | 29.0323 | 11.7021 |

### lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 46.8239 | 46.8118 | 0.0000 |
| 2 | Bayesian Optimization | 48.4449 | 48.3708 | 1.6210 |
| 3 | CrossDataset-LC-DQN | 50.1280 | 50.2105 | 3.3041 |
| 4 | CrossDataset-HyperRL | 50.3607 | 50.1585 | 3.5368 |
