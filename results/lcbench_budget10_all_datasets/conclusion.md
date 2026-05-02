# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |         1.9436 |          1.9530 |             0.1678 |
| 2    | Random Search         |         2.0543 |          2.0965 |             0.2785 |
| 3    | OurMethod-LC-DQN-MLP  |         2.0638 |          2.0933 |             0.2880 |
| 4    | HyperRL-MLP           |         2.3006 |          2.3278 |             0.5249 |

## lcbench_Amazon_employee_access

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |         5.9205 |          5.7888 |             0.0000 |
| 2    | HyperRL-MLP           |         5.9205 |          5.7888 |             0.0000 |
| 3    | OurMethod-LC-DQN-MLP  |         5.9205 |          5.7888 |             0.0000 |
| 4    | Random Search         |         5.9205 |          5.7888 |             0.0000 |

## lcbench_Australian

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |         9.6732 |         15.5066 |             0.3922 |
| 2    | OurMethod-LC-DQN-MLP  |         9.6732 |         16.4758 |             0.3922 |
| 3    | Random Search         |         9.6732 |         16.1233 |             0.3922 |
| 4    | HyperRL-MLP           |        10.1961 |         16.4758 |             0.9150 |

## lcbench_Fashion-MNIST

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Random Search         |        12.9487 |         12.1126 |             0.2390 |
| 2    | OurMethod-LC-DQN-MLP  |        13.6736 |         12.7758 |             0.9639 |
| 3    | HyperRL-MLP           |        13.6904 |         12.8026 |             0.9807 |
| 4    | Bayesian Optimization |        15.1906 |         14.4121 |             2.4809 |

## lcbench_KDDCup09_appetency

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |         1.6733 |          1.7818 |             0.0000 |
| 2    | OurMethod-LC-DQN-MLP  |         1.6733 |          1.7818 |             0.0000 |
| 3    | Bayesian Optimization |         1.7240 |          1.8218 |             0.0507 |
| 4    | Random Search         |         2.0568 |          2.1467 |             0.3835 |

## lcbench_MiniBooNE

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        11.8872 |         12.1355 |             0.3707 |
| 2    | HyperRL-MLP           |        12.0214 |         12.2501 |             0.5049 |
| 3    | Random Search         |        12.5799 |         12.8503 |             1.0634 |
| 4    | Bayesian Optimization |        13.6169 |         13.8679 |             2.1004 |

## lcbench_adult

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        19.8722 |         20.0087 |             0.8482 |
| 2    | Bayesian Optimization |        19.8926 |         19.9193 |             0.8685 |
| 3    | Random Search         |        19.9093 |         19.9342 |             0.8852 |
| 4    | OurMethod-LC-DQN-MLP  |        19.9426 |         19.9851 |             0.9185 |

## lcbench_airlines

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        39.1358 |         39.2616 |             0.0000 |
| 2    | HyperRL-MLP           |        39.8437 |         39.8725 |             0.7079 |
| 3    | Random Search         |        39.8786 |         39.9460 |             0.7428 |
| 4    | Bayesian Optimization |        40.7367 |         40.8073 |             1.6009 |

## lcbench_albert

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        34.8722 |         34.6273 |             0.1878 |
| 2    | Random Search         |        35.1090 |         34.8645 |             0.4246 |
| 3    | HyperRL-MLP           |        35.5957 |         35.3727 |             0.9113 |
| 4    | Bayesian Optimization |        36.1996 |         36.0262 |             1.5152 |

## lcbench_bank-marketing

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        14.2383 |         14.3468 |             0.5722 |
| 2    | HyperRL-MLP           |        14.3463 |         14.5693 |             0.6802 |
| 3    | Random Search         |        14.8344 |         15.1203 |             1.1684 |
| 4    | Bayesian Optimization |        15.2426 |         15.5895 |             1.5765 |

## lcbench_blood-transfusion-service-center

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        29.2771 |         26.9106 |             3.6145 |
| 2    | HyperRL-MLP           |        29.5181 |         28.0488 |             3.8554 |
| 3    | Bayesian Optimization |        30.7229 |         30.4878 |             5.0602 |
| 4    | Random Search         |        31.9277 |         30.4065 |             6.2651 |

## lcbench_car

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        10.7050 |         14.7719 |             1.3055 |
| 2    | OurMethod-LC-DQN-MLP  |        11.3838 |         15.7544 |             1.9843 |
| 3    | Random Search         |        11.4882 |         16.3509 |             2.0888 |
| 4    | Bayesian Optimization |        14.0992 |         18.6667 |             4.6997 |

## lcbench_christine

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        26.8781 |         28.2774 |             0.1169 |
| 2    | OurMethod-LC-DQN-MLP  |        26.9449 |         28.4004 |             0.1836 |
| 3    | Random Search         |        27.1119 |         28.1208 |             0.3506 |
| 4    | Bayesian Optimization |        27.1786 |         28.1320 |             0.4174 |

## lcbench_cnae-9

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |         3.3473 |          5.7865 |             0.0837 |
| 2    | Random Search         |         4.2678 |          6.1798 |             1.0042 |
| 3    | Bayesian Optimization |         4.6862 |          5.7303 |             1.4226 |
| 4    | HyperRL-MLP           |         4.6862 |          6.8539 |             1.4226 |

## lcbench_connect-4

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        31.0269 |         30.7863 |             0.0000 |
| 2    | OurMethod-LC-DQN-MLP  |        31.0269 |         30.7863 |             0.0000 |
| 3    | Random Search         |        31.5638 |         31.2502 |             0.5369 |
| 4    | Bayesian Optimization |        34.5160 |         34.2888 |             3.4891 |

## lcbench_covertype

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        34.5953 |         34.4097 |             0.8479 |
| 2    | Random Search         |        35.1133 |         34.8954 |             1.3659 |
| 3    | HyperRL-MLP           |        35.7659 |         35.5514 |             2.0185 |
| 4    | Bayesian Optimization |        38.4654 |         38.2338 |             4.7180 |

## lcbench_credit-g

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        27.1171 |         29.8182 |             0.1802 |
| 2    | HyperRL-MLP           |        27.7477 |         30.7273 |             0.8108 |
| 3    | Random Search         |        27.8378 |         30.1818 |             0.9009 |
| 4    | Bayesian Optimization |        28.5586 |         29.3333 |             1.6216 |

## lcbench_dionis

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |         0.3401 |          0.3218 |             0.0409 |
| 2    | Random Search         |         0.3673 |          0.3577 |             0.0680 |
| 3    | OurMethod-LC-DQN-MLP  |         0.3895 |          0.3654 |             0.0902 |
| 4    | HyperRL-MLP           |         0.4758 |          0.4593 |             0.1765 |

## lcbench_fabert

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |        33.5530 |         35.6675 |             0.1428 |
| 2    | Random Search         |        34.3328 |         35.4101 |             0.9226 |
| 3    | OurMethod-LC-DQN-MLP  |        34.3987 |         35.5793 |             0.9885 |
| 4    | HyperRL-MLP           |        35.5519 |         36.6164 |             2.1417 |

## lcbench_helena

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        30.9850 |         31.2028 |            14.8982 |
| 2    | Bayesian Optimization |        48.2876 |         48.6463 |            32.2008 |
| 3    | OurMethod-LC-DQN-MLP  |        62.0855 |         62.3557 |            45.9987 |
| 4    | Random Search         |        62.8334 |         63.2769 |            46.7465 |

## lcbench_higgs

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        31.4280 |         31.3852 |             1.8081 |
| 2    | Random Search         |        31.7048 |         31.6244 |             2.0849 |
| 3    | HyperRL-MLP           |        33.4161 |         33.5524 |             3.7961 |
| 4    | Bayesian Optimization |        34.6356 |         34.6514 |             5.0157 |

## lcbench_jannis

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        36.9655 |         36.3991 |             0.4451 |
| 2    | HyperRL-MLP           |        38.4271 |         37.7968 |             1.9067 |
| 3    | Random Search         |        38.8733 |         38.3519 |             2.3528 |
| 4    | Bayesian Optimization |        40.7357 |         40.2526 |             4.2152 |

## lcbench_jasmine

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Random Search         |        18.4569 |         24.1667 |             0.2421 |
| 2    | OurMethod-LC-DQN-MLP  |        18.4871 |         23.8211 |             0.2723 |
| 3    | Bayesian Optimization |        18.6082 |         24.0447 |             0.3933 |
| 4    | HyperRL-MLP           |        19.2436 |         24.2886 |             1.0287 |

## lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        21.9919 |         20.8222 |             0.7508 |
| 2    | HyperRL-MLP           |        27.0777 |         26.2218 |             5.8365 |
| 3    | Random Search         |        27.4369 |         26.6072 |             6.1958 |
| 4    | Bayesian Optimization |        34.8940 |         34.3935 |            13.6529 |

## lcbench_kc1

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        17.9015 |         18.1295 |             3.7259 |
| 2    | Bayesian Optimization |        18.0728 |         18.5612 |             3.8972 |
| 3    | OurMethod-LC-DQN-MLP  |        19.5717 |         19.6835 |             5.3961 |
| 4    | Random Search         |        20.2570 |         20.5180 |             6.0814 |

## lcbench_kr-vs-kp

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |         3.6209 |          3.7381 |             0.7355 |
| 2    | Random Search         |         4.1018 |          4.4213 |             1.2164 |
| 3    | Bayesian Optimization |         4.2716 |          4.3074 |             1.3861 |
| 4    | OurMethod-LC-DQN-MLP  |         4.3564 |          4.3454 |             1.4710 |

## lcbench_mfeat-factors

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |         3.5666 |          2.6061 |             0.6321 |
| 2    | Random Search         |         3.6569 |          2.1818 |             0.7223 |
| 3    | Bayesian Optimization |         3.7472 |          2.6061 |             0.8126 |
| 4    | HyperRL-MLP           |         3.7472 |          2.2424 |             0.8126 |

## lcbench_nomao

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |         5.0230 |          5.0910 |             0.4855 |
| 2    | Random Search         |         5.1489 |          5.2194 |             0.6115 |
| 3    | HyperRL-MLP           |         5.2828 |          5.3249 |             0.7453 |
| 4    | Bayesian Optimization |         5.3064 |          5.3864 |             0.7689 |

## lcbench_numerai28.6

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |        48.1533 |         47.9893 |             0.0131 |
| 2    | Random Search         |        48.1908 |         47.8628 |             0.0507 |
| 3    | OurMethod-LC-DQN-MLP  |        48.2951 |         47.6929 |             0.1550 |
| 4    | HyperRL-MLP           |        48.2969 |         47.5432 |             0.1568 |

## lcbench_phoneme

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        21.4561 |         20.9310 |             0.0000 |
| 2    | Random Search         |        22.5105 |         21.7162 |             1.0544 |
| 3    | HyperRL-MLP           |        22.6444 |         22.0079 |             1.1883 |
| 4    | Bayesian Optimization |        24.0669 |         23.8811 |             2.6109 |

## lcbench_segment

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        13.6595 |         13.7270 |             0.8219 |
| 2    | Random Search         |        14.3249 |         14.1995 |             1.4873 |
| 3    | HyperRL-MLP           |        19.0215 |         19.0551 |             6.1840 |
| 4    | Bayesian Optimization |        20.6262 |         20.5249 |             7.7886 |

## lcbench_shuttle

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |         1.5549 |          1.5266 |             0.0889 |
| 2    | HyperRL-MLP           |         1.7982 |          1.8130 |             0.3322 |
| 3    | Random Search         |         1.9651 |          1.9509 |             0.4991 |
| 4    | Bayesian Optimization |         2.6575 |          2.6573 |             1.1915 |

## lcbench_sylvine

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |         6.7549 |          8.5089 |             0.5644 |
| 2    | HyperRL-MLP           |         6.8959 |          8.6982 |             0.7055 |
| 3    | Random Search         |         7.4956 |          9.2308 |             1.3051 |
| 4    | Bayesian Optimization |         7.6720 |          8.9467 |             1.4815 |

## lcbench_vehicle

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        25.4255 |         25.5914 |             1.5957 |
| 2    | Bayesian Optimization |        25.9574 |         23.7276 |             2.1277 |
| 3    | Random Search         |        28.7234 |         28.0287 |             4.8936 |
| 4    | HyperRL-MLP           |        30.6383 |         30.5376 |             6.8085 |

## lcbench_volkert

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Random Search         |        45.3362 |         45.3807 |             0.4669 |
| 2    | OurMethod-LC-DQN-MLP  |        45.5968 |         45.6738 |             0.7275 |
| 3    | HyperRL-MLP           |        47.1574 |         47.4500 |             2.2881 |
| 4    | Bayesian Optimization |        49.8906 |         49.8197 |             5.0213 |

## Overall

| Rank | Method                | Avg simple regret | Avg per-task rank | Tasks |
| ---- | --------------------- | ----------------: | ----------------: | ----: |
| 1    | HyperRL-MLP           |            1.9734 |              2.51 |    35 |
| 2    | OurMethod-LC-DQN-MLP  |            2.0823 |              1.80 |    35 |
| 3    | Random Search         |            2.7169 |              2.60 |    35 |
| 4    | Bayesian Optimization |            3.2841 |              3.09 |    35 |

## Rank-1 Counts

| Method                | Rank-1 task count |
| --------------------- | ----------------: |
| OurMethod-LC-DQN-MLP  |                22 |
| HyperRL-MLP           |                 9 |
| Bayesian Optimization |                 6 |
| Random Search         |                 5 |

Most rank-1 finishes: **OurMethod-LC-DQN-MLP** with 22 task(s).

Across the selected tasks, **HyperRL-MLP** gives the best average simple regret (1.9734). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.
