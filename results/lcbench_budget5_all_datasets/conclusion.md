# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |         1.9019 |          1.9872 |             0.2273 |
| 2    | HyperRL-MLP           |         2.0495 |          2.0606 |             0.3749 |
| 3    | Bayesian Optimization |         2.3804 |          2.3692 |             0.7058 |
| 4    | Random Search         |         2.6065 |          2.6491 |             0.9319 |

## lcbench_Amazon_employee_access

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Random Search         |         5.9288 |          5.7962 |             0.0083 |
| 2    | Bayesian Optimization |         6.0972 |          5.9552 |             0.1766 |
| 3    | OurMethod-LC-DQN-MLP  |         6.1772 |          6.0514 |             0.2567 |
| 4    | HyperRL-MLP           |         8.7938 |          8.5759 |             2.8733 |

## lcbench_Australian

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |        10.1961 |         16.5639 |             0.3922 |
| 2    | HyperRL-MLP           |        10.5882 |         16.2115 |             0.7843 |
| 3    | OurMethod-LC-DQN-MLP  |        11.3726 |         16.3877 |             1.5686 |
| 4    | Random Search         |        12.1569 |         17.4449 |             2.3529 |

## lcbench_Fashion-MNIST

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        13.3260 |         12.5844 |             0.7249 |
| 2    | OurMethod-LC-DQN-MLP  |        14.7461 |         13.9835 |             2.1450 |
| 3    | Random Search         |        15.0239 |         14.1229 |             2.4228 |
| 4    | Bayesian Optimization |        15.7385 |         14.7550 |             3.1374 |

## lcbench_KDDCup09_appetency

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |         2.0658 |          2.1467 |             0.3925 |
| 2    | Random Search         |         2.4295 |          2.5309 |             0.7561 |
| 3    | HyperRL-MLP           |         2.4349 |          2.5261 |             0.7616 |
| 4    | OurMethod-LC-DQN-MLP  |         2.7786 |          2.8448 |             1.1053 |

## lcbench_MiniBooNE

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        12.7892 |         13.0544 |             0.8346 |
| 2    | Random Search         |        13.7991 |         14.0376 |             1.8444 |
| 3    | OurMethod-LC-DQN-MLP  |        14.0724 |         14.3479 |             2.1177 |
| 4    | Bayesian Optimization |        14.8868 |         15.1256 |             2.9322 |

## lcbench_adult

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        19.7315 |         19.7469 |             0.7741 |
| 2    | Bayesian Optimization |        20.4741 |         20.4430 |             1.5167 |
| 3    | OurMethod-LC-DQN-MLP  |        20.4778 |         20.4418 |             1.5204 |
| 4    | Random Search         |        20.8685 |         20.8376 |             1.9111 |

## lcbench_airlines

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        39.4815 |         39.5790 |             0.1833 |
| 2    | OurMethod-LC-DQN-MLP  |        40.6544 |         40.6221 |             1.3562 |
| 3    | Random Search         |        40.7033 |         40.6959 |             1.4052 |
| 4    | Bayesian Optimization |        41.0020 |         41.0087 |             1.7039 |

## lcbench_albert

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        35.0526 |         34.8839 |             0.1653 |
| 2    | OurMethod-LC-DQN-MLP  |        35.8535 |         35.6400 |             0.9662 |
| 3    | Random Search         |        35.9092 |         35.6860 |             1.0219 |
| 4    | Bayesian Optimization |        36.7103 |         36.5142 |             1.8230 |

## lcbench_bank-marketing

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        14.1502 |         14.2007 |             1.1944 |
| 2    | HyperRL-MLP           |        14.2003 |         14.3602 |             1.2444 |
| 3    | Bayesian Optimization |        15.6327 |         15.9474 |             2.6768 |
| 4    | Random Search         |        16.7910 |         17.1526 |             3.8352 |

## lcbench_blood-transfusion-service-center

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        26.8675 |         24.8780 |             0.2410 |
| 2    | OurMethod-LC-DQN-MLP  |        31.9277 |         30.7317 |             5.3012 |
| 3    | Bayesian Optimization |        33.4940 |         32.5203 |             6.8675 |
| 4    | Random Search         |        33.4940 |         32.4390 |             6.8675 |

## lcbench_car

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        15.9791 |         20.8772 |             6.6319 |
| 2    | Bayesian Optimization |        17.0235 |         22.7018 |             7.6762 |
| 3    | OurMethod-LC-DQN-MLP  |        22.2977 |         27.8246 |            12.9504 |
| 4    | Random Search         |        22.6110 |         27.5789 |            13.2637 |

## lcbench_christine

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |        27.3957 |         28.2662 |             0.2170 |
| 2    | HyperRL-MLP           |        27.5459 |         29.3400 |             0.3673 |
| 3    | Random Search         |        27.7963 |         28.6689 |             0.6177 |
| 4    | OurMethod-LC-DQN-MLP  |        27.9466 |         29.0380 |             0.7679 |

## lcbench_cnae-9

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |         6.1088 |          6.6292 |             2.4268 |
| 2    | OurMethod-LC-DQN-MLP  |        15.0628 |         17.4157 |            11.3808 |
| 3    | Random Search         |        15.7322 |         17.8652 |            12.0502 |
| 4    | Bayesian Optimization |        17.9916 |         18.4270 |            14.3096 |

## lcbench_connect-4

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        32.7715 |         32.5376 |             1.7445 |
| 2    | Random Search         |        35.3675 |         35.1500 |             4.3406 |
| 3    | HyperRL-MLP           |        36.6060 |         36.3235 |             5.5791 |
| 4    | Bayesian Optimization |        38.9798 |         38.7216 |             7.9529 |

## lcbench_covertype

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        35.5588 |         35.3415 |             0.8558 |
| 2    | OurMethod-LC-DQN-MLP  |        37.1601 |         36.8874 |             2.4571 |
| 3    | Random Search         |        39.6955 |         39.4213 |             4.9924 |
| 4    | Bayesian Optimization |        41.2492 |         40.9331 |             6.5462 |

## lcbench_credit-g

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        28.8288 |         30.3636 |             0.8108 |
| 2    | Random Search         |        28.8288 |         31.4545 |             0.8108 |
| 3    | OurMethod-LC-DQN-MLP  |        29.2793 |         31.3333 |             1.2613 |
| 4    | Bayesian Optimization |        29.4595 |         29.4545 |             1.4414 |

## lcbench_dionis

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |         0.3701 |          0.3788 |             0.0300 |
| 2    | Random Search         |         0.3919 |          0.3949 |             0.0517 |
| 3    | OurMethod-LC-DQN-MLP  |         0.5651 |          0.5411 |             0.2250 |
| 4    | HyperRL-MLP           |         0.5999 |          0.5829 |             0.2597 |

## lcbench_fabert

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |        34.4865 |         36.2707 |             0.6809 |
| 2    | HyperRL-MLP           |        34.5854 |         36.0942 |             0.7798 |
| 3    | OurMethod-LC-DQN-MLP  |        37.4410 |         39.3674 |             3.6354 |
| 4    | Random Search         |        39.2532 |         40.5370 |             5.4476 |

## lcbench_helena

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        50.0733 |         50.2313 |            18.4070 |
| 2    | HyperRL-MLP           |        50.9362 |         51.2362 |            19.2700 |
| 3    | Random Search         |        67.0137 |         67.3197 |            35.3475 |
| 4    | Bayesian Optimization |        67.5382 |         68.0039 |            35.8719 |

## lcbench_higgs

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        32.4668 |         32.4422 |             1.7611 |
| 2    | Random Search         |        34.3100 |         34.2990 |             3.6042 |
| 3    | OurMethod-LC-DQN-MLP  |        35.4649 |         35.4926 |             4.7592 |
| 4    | Bayesian Optimization |        35.7924 |         35.9148 |             5.0867 |

## lcbench_jannis

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |        40.1458 |         39.5882 |             1.7014 |
| 2    | HyperRL-MLP           |        40.4116 |         39.9023 |             1.9672 |
| 3    | Random Search         |        42.4954 |         41.9535 |             4.0510 |
| 4    | Bayesian Optimization |        43.2019 |         42.8373 |             4.7575 |

## lcbench_jasmine

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |        18.9410 |         23.8821 |             0.2118 |
| 2    | HyperRL-MLP           |        19.3949 |         24.1870 |             0.6657 |
| 3    | OurMethod-LC-DQN-MLP  |        20.3933 |         24.2683 |             1.6641 |
| 4    | Random Search         |        20.5144 |         24.5325 |             1.7852 |

## lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        28.1998 |         27.1629 |             3.7820 |
| 2    | OurMethod-LC-DQN-MLP  |        31.8809 |         31.2684 |             7.4632 |
| 3    | Random Search         |        32.5328 |         31.9554 |             8.1150 |
| 4    | Bayesian Optimization |        35.6468 |         35.2414 |            11.2291 |

## lcbench_kc1

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        21.1135 |         21.0360 |             2.0557 |
| 2    | Bayesian Optimization |        21.1563 |         21.9856 |             2.0985 |
| 3    | OurMethod-LC-DQN-MLP  |        21.5846 |         22.5612 |             2.5268 |
| 4    | Random Search         |        22.0557 |         22.5899 |             2.9979 |

## lcbench_kr-vs-kp

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |         4.8939 |          4.8197 |             1.4993 |
| 2    | OurMethod-LC-DQN-MLP  |         6.7327 |          7.3055 |             3.3380 |
| 3    | Random Search         |        10.0424 |          9.8672 |             6.6478 |
| 4    | Bayesian Optimization |        12.2489 |         12.1632 |             8.8543 |

## lcbench_mfeat-factors

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |         3.8826 |          2.2121 |             0.4515 |
| 2    | OurMethod-LC-DQN-MLP  |         5.2822 |          3.2424 |             1.8510 |
| 3    | Bayesian Optimization |         6.9074 |          5.2121 |             3.4763 |
| 4    | Random Search         |         7.9007 |          6.8182 |             4.4695 |

## lcbench_nomao

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |         5.1830 |          5.2598 |             0.3753 |
| 2    | OurMethod-LC-DQN-MLP  |         5.7578 |          5.7083 |             0.9500 |
| 3    | Random Search         |         6.2223 |          6.2341 |             1.4145 |
| 4    | Bayesian Optimization |         6.7104 |          6.4978 |             1.9026 |

## lcbench_numerai28.6

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | Bayesian Optimization |        48.2077 |         47.9654 |             0.0592 |
| 2    | Random Search         |        48.2913 |         47.8685 |             0.1427 |
| 3    | HyperRL-MLP           |        48.3805 |         47.4507 |             0.2320 |
| 4    | OurMethod-LC-DQN-MLP  |        48.3946 |         47.5772 |             0.2460 |

## lcbench_phoneme

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        22.9289 |         22.7370 |             1.0377 |
| 2    | OurMethod-LC-DQN-MLP  |        24.2176 |         23.6343 |             2.3264 |
| 3    | Random Search         |        24.3347 |         23.7914 |             2.4435 |
| 4    | Bayesian Optimization |        25.4728 |         25.1038 |             3.5816 |

## lcbench_segment

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        16.0078 |         15.1181 |             2.2701 |
| 2    | Random Search         |        24.5793 |         24.9869 |            10.8415 |
| 3    | OurMethod-LC-DQN-MLP  |        31.3503 |         31.9423 |            17.6125 |
| 4    | Bayesian Optimization |        31.4286 |         33.0446 |            17.6908 |

## lcbench_shuttle

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | OurMethod-LC-DQN-MLP  |         2.3924 |          2.4535 |             0.7782 |
| 2    | Random Search         |         2.5858 |          2.5893 |             0.9716 |
| 3    | HyperRL-MLP           |         2.6310 |          2.6290 |             1.0168 |
| 4    | Bayesian Optimization |         2.9632 |          2.9655 |             1.3490 |

## lcbench_sylvine

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |         7.5661 |          8.8876 |             0.2646 |
| 2    | Bayesian Optimization |         9.8765 |         11.1479 |             2.5750 |
| 3    | OurMethod-LC-DQN-MLP  |         9.9118 |         11.0414 |             2.6102 |
| 4    | Random Search         |        11.1464 |         12.9704 |             3.8448 |

## lcbench_vehicle

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        27.7660 |         28.2437 |             2.9787 |
| 2    | Bayesian Optimization |        31.9149 |         31.4695 |             7.1277 |
| 3    | OurMethod-LC-DQN-MLP  |        35.7447 |         36.5591 |            10.9574 |
| 4    | Random Search         |        37.5532 |         37.7061 |            12.7660 |

## lcbench_volkert

| Rank | Method                | Val score mean | Test score mean | Simple regret mean |
| ---- | --------------------- | -------------: | --------------: | -----------------: |
| 1    | HyperRL-MLP           |        46.5369 |         46.8129 |             2.0461 |
| 2    | Random Search         |        49.4222 |         49.4725 |             4.9314 |
| 3    | OurMethod-LC-DQN-MLP  |        49.6440 |         49.7542 |             5.1532 |
| 4    | Bayesian Optimization |        53.2909 |         53.3274 |             8.8001 |

## Overall

| Rank | Method                | Avg simple regret | Avg per-task rank | Tasks |
| ---- | --------------------- | ----------------: | ----------------: | ----: |
| 1    | HyperRL-MLP           |            1.9527 |              1.63 |    35 |
| 2    | OurMethod-LC-DQN-MLP  |            3.8436 |              2.43 |    35 |
| 3    | Random Search         |            4.8373 |              3.00 |    35 |
| 4    | Bayesian Optimization |            5.0243 |              2.94 |    35 |

## Rank-1 Counts

| Method                | Rank-1 task count |
| --------------------- | ----------------: |
| HyperRL-MLP           |                21 |
| Bayesian Optimization |                 7 |
| OurMethod-LC-DQN-MLP  |                 6 |
| Random Search         |                 2 |

Most rank-1 finishes: **HyperRL-MLP** with 21 task(s).

Across the selected tasks, **HyperRL-MLP** gives the best average simple regret (1.9527). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.
