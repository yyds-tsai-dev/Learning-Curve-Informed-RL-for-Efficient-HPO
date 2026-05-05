# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 1.8237 | 2.94 | 35 |
| 2 | Random Search | 1.9488 | 2.77 | 35 |
| 3 | Bayesian Optimization | 2.2982 | 1.46 | 35 |
| 4 | CrossDataset-HyperRL | 4.3848 | 2.83 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 27 |
| Random Search | 9 |
| CrossDataset-HyperRL | 7 |
| CrossDataset-LC-DQN | 7 |

Most rank-1 finishes: **Bayesian Optimization** with 27 task(s).

Across the selected tasks, **CrossDataset-LC-DQN** gives the best average simple regret (1.8237). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-DQN tests the paper-style DQN setup with a configurable sequence encoder (default: LSTM), and OurMethod-LC-DQN adds learning-curve and derivative state features.

## Per-Task Rankings

### lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.2795 | 1.2839 | 0.0000 |
| 2 | Random Search | 1.4639 | 1.6108 | 0.1845 |
| 3 | CrossDataset-LC-DQN | 1.9757 | 2.1172 | 0.6963 |
| 4 | CrossDataset-HyperRL | 2.3744 | 2.4442 | 1.0950 |

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
| 2 | Random Search | 9.1503 | 16.2996 | 0.0000 |
| 3 | CrossDataset-HyperRL | 9.8039 | 15.8590 | 0.6536 |
| 4 | CrossDataset-LC-DQN | 10.4575 | 15.8590 | 1.3072 |

### lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 11.9718 | 11.2251 | 0.0000 |
| 2 | CrossDataset-HyperRL | 12.1721 | 11.5065 | 0.2003 |
| 3 | Random Search | 13.2963 | 12.5325 | 1.3245 |
| 4 | CrossDataset-LC-DQN | 14.8340 | 13.6277 | 2.8621 |

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
| 3 | CrossDataset-LC-DQN | 12.8073 | 13.0166 | 2.0725 |
| 4 | CrossDataset-HyperRL | 12.8560 | 13.1028 | 2.1212 |

### lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 19.4630 | 19.4701 | 0.0000 |
| 2 | Random Search | 19.4630 | 19.4763 | 0.0000 |
| 3 | CrossDataset-LC-DQN | 19.8981 | 20.0844 | 0.4352 |
| 4 | CrossDataset-HyperRL | 20.5093 | 20.5187 | 1.0463 |

### lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 38.0016 | 38.1855 | 0.0000 |
| 2 | CrossDataset-HyperRL | 39.9328 | 40.1007 | 1.9311 |
| 3 | Random Search | 40.6270 | 40.7777 | 2.6254 |
| 4 | CrossDataset-LC-DQN | 40.7528 | 40.7209 | 2.7512 |

### lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 35.1219 | 34.9179 | 0.0000 |
| 2 | Random Search | 35.1698 | 34.8944 | 0.0479 |
| 3 | CrossDataset-LC-DQN | 35.5612 | 35.3669 | 0.4393 |
| 4 | Bayesian Optimization | 35.8026 | 35.5757 | 0.6807 |

### lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 11.7735 | 11.6228 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 11.7735 | 11.6228 | 0.0000 |
| 3 | Random Search | 12.0636 | 11.2943 | 0.2901 |
| 4 | Bayesian Optimization | 16.2749 | 16.7370 | 4.5014 |

### lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 21.0843 | 19.1057 | 0.0000 |
| 2 | CrossDataset-HyperRL | 21.0843 | 19.9187 | 0.0000 |
| 3 | CrossDataset-LC-DQN | 21.0843 | 19.9187 | 0.0000 |
| 4 | Random Search | 31.9277 | 26.0163 | 10.8434 |

### lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 9.1384 | 13.1579 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 10.1828 | 14.2105 | 1.0444 |
| 3 | CrossDataset-HyperRL | 14.0992 | 19.1228 | 4.9608 |
| 4 | Random Search | 14.8825 | 19.4737 | 5.7441 |

### lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 26.7947 | 27.5727 | 0.0000 |
| 2 | Random Search | 27.0451 | 28.2998 | 0.2504 |
| 3 | CrossDataset-HyperRL | 27.1285 | 28.4676 | 0.3339 |
| 4 | Bayesian Optimization | 27.3790 | 27.4049 | 0.5843 |

### lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.7657 | 5.8989 | 0.0000 |
| 2 | CrossDataset-HyperRL | 4.6025 | 6.7416 | 0.8368 |
| 3 | CrossDataset-LC-DQN | 4.6025 | 6.7416 | 0.8368 |
| 4 | Random Search | 4.6025 | 8.1461 | 0.8368 |

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
| 3 | CrossDataset-HyperRL | 35.7359 | 35.6890 | 6.1458 |
| 4 | CrossDataset-LC-DQN | 37.8415 | 37.5849 | 8.2515 |

### lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.1261 | 28.7879 | 0.0000 |
| 2 | CrossDataset-HyperRL | 27.4775 | 22.4242 | 1.3513 |
| 3 | Random Search | 27.4775 | 32.1212 | 1.3513 |
| 4 | CrossDataset-LC-DQN | 27.9279 | 30.9091 | 1.8018 |

### lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-HyperRL | 0.1567 | 0.1751 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 0.1567 | 0.1751 | 0.0000 |
| 3 | Bayesian Optimization | 0.4164 | 0.3738 | 0.2597 |
| 4 | Random Search | 0.4164 | 0.3738 | 0.2597 |

### lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.1137 | 35.6013 | 0.0000 |
| 2 | CrossDataset-HyperRL | 33.6628 | 35.0497 | 0.5491 |
| 3 | CrossDataset-LC-DQN | 33.9923 | 35.6013 | 0.8786 |
| 4 | Random Search | 34.4316 | 34.7186 | 1.3180 |

### lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 0.3548 | 0.3911 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 0.3826 | 0.3493 | 0.0277 |
| 3 | Bayesian Optimization | 71.7378 | 72.3821 | 71.3829 |
| 4 | CrossDataset-HyperRL | 78.9178 | 79.5399 | 78.5630 |

### lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 29.5249 | 29.7565 | 0.0000 |
| 2 | Random Search | 31.4529 | 30.9680 | 1.9280 |
| 3 | CrossDataset-HyperRL | 31.9834 | 31.8457 | 2.4585 |
| 4 | CrossDataset-LC-DQN | 32.8275 | 32.5689 | 3.3026 |

### lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 37.7984 | 37.3589 | 0.0000 |
| 2 | Bayesian Optimization | 39.1217 | 38.4663 | 1.3233 |
| 3 | CrossDataset-HyperRL | 41.8440 | 41.1335 | 4.0456 |
| 4 | CrossDataset-LC-DQN | 41.8872 | 41.2493 | 4.0888 |

### lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.3056 | 24.7967 | 0.0000 |
| 2 | CrossDataset-HyperRL | 18.3056 | 24.1870 | 0.0000 |
| 3 | Random Search | 18.3056 | 23.5772 | 0.0000 |
| 4 | CrossDataset-LC-DQN | 19.5159 | 24.6951 | 1.2103 |

### lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 20.6761 | 19.3171 | 0.0000 |
| 2 | Random Search | 26.4884 | 25.3076 | 5.8123 |
| 3 | CrossDataset-LC-DQN | 27.1847 | 26.0379 | 6.5086 |
| 4 | CrossDataset-HyperRL | 34.4501 | 33.4348 | 13.7740 |

### lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 13.7045 | 14.8201 | 0.0000 |
| 2 | Random Search | 14.9893 | 15.2518 | 1.2848 |
| 3 | CrossDataset-HyperRL | 16.0600 | 16.2590 | 2.3555 |
| 4 | CrossDataset-LC-DQN | 16.0600 | 16.2590 | 2.3555 |

### lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.9802 | 2.5617 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 2.8289 | 3.0361 | 0.8487 |
| 3 | Random Search | 3.1117 | 3.3207 | 1.1315 |
| 4 | CrossDataset-HyperRL | 3.6775 | 3.7951 | 1.6973 |

### lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 2.9345 | 1.9697 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 3.1603 | 2.5758 | 0.2257 |
| 3 | CrossDataset-HyperRL | 3.8375 | 2.5758 | 0.9029 |
| 4 | Random Search | 4.5147 | 3.9394 | 1.5801 |

### lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 4.7238 | 4.9327 | 0.0000 |
| 2 | Random Search | 5.0125 | 5.0998 | 0.2887 |
| 3 | CrossDataset-LC-DQN | 5.3930 | 5.3020 | 0.6692 |
| 4 | CrossDataset-HyperRL | 5.4324 | 5.4339 | 0.7086 |

### lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 48.1101 | 47.8087 | 0.0000 |
| 2 | Random Search | 48.1101 | 47.8087 | 0.0000 |
| 3 | CrossDataset-HyperRL | 48.2556 | 47.6703 | 0.1456 |
| 4 | CrossDataset-LC-DQN | 48.2744 | 47.4847 | 0.1643 |

### lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | CrossDataset-LC-DQN | 21.0042 | 20.5272 | 0.0000 |
| 2 | Bayesian Optimization | 21.0879 | 21.5367 | 0.0837 |
| 3 | CrossDataset-HyperRL | 22.8452 | 22.3780 | 1.8410 |
| 4 | Random Search | 22.9289 | 22.7145 | 1.9247 |

### lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 13.5029 | 12.2047 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 14.8728 | 12.9921 | 1.3699 |
| 3 | Random Search | 16.6340 | 16.2730 | 3.1311 |
| 4 | CrossDataset-HyperRL | 16.8297 | 14.8294 | 3.3268 |

### lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.3041 | 0.2456 | 0.0000 |
| 2 | Random Search | 2.1132 | 2.0481 | 1.8091 |
| 3 | CrossDataset-LC-DQN | 2.4719 | 2.3720 | 2.1678 |
| 4 | CrossDataset-HyperRL | 2.8072 | 2.8109 | 2.5031 |

### lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.3792 | 7.4556 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 5.9083 | 6.9231 | 0.5291 |
| 3 | Random Search | 6.7019 | 7.9290 | 1.3228 |
| 4 | CrossDataset-HyperRL | 6.7901 | 8.3432 | 1.4109 |

### lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.6170 | 31.1828 | 0.0000 |
| 2 | CrossDataset-LC-DQN | 27.1277 | 28.3154 | 8.5106 |
| 3 | CrossDataset-HyperRL | 29.7872 | 29.7491 | 11.1702 |
| 4 | Random Search | 30.3191 | 29.0323 | 11.7021 |

### lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 46.8239 | 46.8118 | 0.0000 |
| 2 | Bayesian Optimization | 48.4449 | 48.3708 | 1.6210 |
| 3 | CrossDataset-HyperRL | 49.0964 | 49.0724 | 2.2726 |
| 4 | CrossDataset-LC-DQN | 50.2288 | 50.5327 | 3.4049 |
