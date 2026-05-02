# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.2533 | 1.2903 | 0.0512 |
| 2 | HyperRL-MLP | 1.3628 | 1.3740 | 0.1607 |
| 3 | Random Search | 1.4699 | 1.5152 | 0.2678 |
| 4 | OurMethod-LC-DQN-MLP | 1.5794 | 1.6372 | 0.3773 |

## lcbench_Amazon_employee_access

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.9205 | 5.7888 | 0.0000 |
| 2 | HyperRL-MLP | 5.9205 | 5.7888 | 0.0000 |
| 3 | OurMethod-LC-DQN-MLP | 5.9205 | 5.7888 | 0.0000 |
| 4 | Random Search | 5.9205 | 5.7888 | 0.0000 |

## lcbench_Australian

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 9.1503 | 16.2115 | 0.1307 |
| 2 | Bayesian Optimization | 9.2810 | 15.8590 | 0.2614 |
| 3 | HyperRL-MLP | 9.4118 | 16.2996 | 0.3922 |
| 4 | OurMethod-LC-DQN-MLP | 9.4118 | 16.3877 | 0.3922 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.8373 | 10.1922 | 0.1085 |
| 2 | Random Search | 11.2922 | 10.4918 | 0.5634 |
| 3 | HyperRL-MLP | 11.4666 | 10.7576 | 0.7378 |
| 4 | OurMethod-LC-DQN-MLP | 11.9899 | 11.1991 | 1.2611 |

## lcbench_KDDCup09_appetency

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.6733 | 1.7830 | 0.0000 |
| 2 | HyperRL-MLP | 1.6733 | 1.7818 | 0.0000 |
| 3 | OurMethod-LC-DQN-MLP | 1.6733 | 1.7818 | 0.0000 |
| 4 | Random Search | 1.6733 | 1.7818 | 0.0000 |

## lcbench_MiniBooNE

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 9.8460 | 9.9930 | 0.0000 |
| 2 | Random Search | 10.7104 | 10.9301 | 0.8645 |
| 3 | OurMethod-LC-DQN-MLP | 11.1423 | 11.3970 | 1.2964 |
| 4 | HyperRL-MLP | 11.7015 | 11.9752 | 1.8555 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 18.4889 | 18.6462 | 0.0667 |
| 2 | Bayesian Optimization | 19.0407 | 19.1289 | 0.6185 |
| 3 | HyperRL-MLP | 19.4426 | 19.5620 | 1.0204 |
| 4 | Random Search | 19.4963 | 19.5284 | 1.0741 |

## lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.7045 | 36.9143 | 0.0124 |
| 2 | HyperRL-MLP | 38.1407 | 38.3256 | 1.4486 |
| 3 | OurMethod-LC-DQN-MLP | 38.1885 | 38.3583 | 1.4964 |
| 4 | Random Search | 38.4603 | 38.6168 | 1.7683 |

## lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.7722 | 33.7485 | 0.0000 |
| 2 | HyperRL-MLP | 34.1790 | 33.9759 | 0.4067 |
| 3 | Random Search | 34.2134 | 33.9370 | 0.4412 |
| 4 | OurMethod-LC-DQN-MLP | 34.5008 | 34.2525 | 0.7286 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 11.6495 | 11.3600 | 0.0100 |
| 2 | OurMethod-LC-DQN-MLP | 11.6955 | 11.4136 | 0.0560 |
| 3 | HyperRL-MLP | 11.7375 | 11.3895 | 0.0980 |
| 4 | Bayesian Optimization | 14.0282 | 14.2825 | 2.3887 |

## lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 21.6867 | 19.9187 | 0.2410 |
| 2 | HyperRL-MLP | 22.1687 | 20.0813 | 0.7229 |
| 3 | Random Search | 22.2892 | 19.5122 | 0.8434 |
| 4 | Bayesian Optimization | 24.5783 | 23.0081 | 3.1325 |

## lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 4.2820 | 7.3333 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 6.8407 | 9.6491 | 2.5587 |
| 3 | HyperRL-MLP | 8.0418 | 11.6491 | 3.7598 |
| 4 | Random Search | 8.0418 | 11.5789 | 3.7598 |

## lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.0434 | 28.0649 | 0.3339 |
| 2 | OurMethod-LC-DQN-MLP | 26.2771 | 27.9642 | 0.5676 |
| 3 | Random Search | 26.3272 | 28.1096 | 0.6177 |
| 4 | HyperRL-MLP | 26.4608 | 27.8747 | 0.7513 |

## lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 3.3473 | 6.0674 | 0.1674 |
| 2 | HyperRL-MLP | 3.4310 | 6.0674 | 0.2510 |
| 3 | OurMethod-LC-DQN-MLP | 3.5146 | 6.3483 | 0.3347 |
| 4 | Bayesian Optimization | 4.0167 | 5.7865 | 0.8368 |

## lcbench_connect-4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 27.7681 | 27.3279 | 1.2438 |
| 2 | Bayesian Optimization | 28.2688 | 27.8715 | 1.7445 |
| 3 | Random Search | 29.3266 | 28.9965 | 2.8022 |
| 4 | OurMethod-LC-DQN-MLP | 30.4244 | 30.0964 | 3.9001 |

## lcbench_covertype

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 23.1785 | 23.1012 | 0.0534 |
| 2 | Random Search | 31.2002 | 30.9789 | 8.0751 |
| 3 | HyperRL-MLP | 31.2100 | 30.9477 | 8.0849 |
| 4 | OurMethod-LC-DQN-MLP | 32.9929 | 32.8813 | 9.8678 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 26.8468 | 29.6364 | 0.6306 |
| 2 | Bayesian Optimization | 26.8468 | 30.4848 | 0.6306 |
| 3 | OurMethod-LC-DQN-MLP | 26.9369 | 28.5455 | 0.7207 |
| 4 | HyperRL-MLP | 27.4775 | 29.4545 | 1.2613 |

## lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 0.2382 | 0.2244 | 0.1061 |
| 2 | Random Search | 0.2619 | 0.2757 | 0.1298 |
| 3 | Bayesian Optimization | 0.2643 | 0.2556 | 0.1321 |
| 4 | HyperRL-MLP | 0.3319 | 0.2953 | 0.1997 |

## lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.4102 | 35.7411 | 0.0988 |
| 2 | HyperRL-MLP | 33.5310 | 34.8878 | 0.2197 |
| 3 | OurMethod-LC-DQN-MLP | 33.6518 | 34.9982 | 0.3405 |
| 4 | Random Search | 33.6518 | 35.3292 | 0.3405 |

## lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 0.0704 | 19.8964 | 0.0347 |
| 2 | HyperRL-MLP | 0.0968 | 0.1606 | 0.0610 |
| 3 | Random Search | 14.7743 | 14.9287 | 14.7386 |
| 4 | Bayesian Optimization | 28.7526 | 48.8202 | 28.7169 |

## lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 28.9336 | 28.8559 | 0.6568 |
| 2 | OurMethod-LC-DQN-MLP | 29.1753 | 29.1056 | 0.8985 |
| 3 | Random Search | 29.3423 | 29.2385 | 1.0655 |
| 4 | HyperRL-MLP | 29.4437 | 29.3708 | 1.1670 |

## lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.8403 | 33.4858 | 0.0000 |
| 2 | Random Search | 35.6066 | 34.9920 | 1.7662 |
| 3 | HyperRL-MLP | 35.6606 | 34.9899 | 1.8202 |
| 4 | OurMethod-LC-DQN-MLP | 36.4546 | 35.9424 | 2.6142 |

## lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.1543 | 24.2683 | 0.0605 |
| 2 | Random Search | 18.2148 | 24.2480 | 0.1210 |
| 3 | OurMethod-LC-DQN-MLP | 18.2451 | 23.9431 | 0.1513 |
| 4 | HyperRL-MLP | 18.3964 | 23.9431 | 0.3026 |

## lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 16.4945 | 15.2644 | 0.2987 |
| 2 | Random Search | 19.8607 | 18.6058 | 3.6650 |
| 3 | HyperRL-MLP | 20.7568 | 19.5740 | 4.5610 |
| 4 | OurMethod-LC-DQN-MLP | 21.1362 | 19.9243 | 4.9405 |

## lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 14.4754 | 14.9928 | 0.6424 |
| 2 | OurMethod-LC-DQN-MLP | 14.5610 | 15.7698 | 0.7281 |
| 3 | Random Search | 15.6745 | 15.9424 | 1.8415 |
| 4 | Bayesian Optimization | 17.0021 | 17.6691 | 3.1692 |

## lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.4144 | 2.2770 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 2.0934 | 2.3340 | 0.6789 |
| 3 | HyperRL-MLP | 2.1782 | 2.5047 | 0.7638 |
| 4 | Random Search | 2.5460 | 2.6755 | 1.1315 |

## lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 2.7088 | 2.0000 | 0.1354 |
| 2 | HyperRL-MLP | 2.8442 | 1.7576 | 0.2709 |
| 3 | Bayesian Optimization | 3.0248 | 1.8788 | 0.4515 |
| 4 | Random Search | 3.0700 | 1.8182 | 0.4966 |

## lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.9339 | 4.1502 | 0.0184 |
| 2 | Random Search | 4.2094 | 4.4034 | 0.2939 |
| 3 | HyperRL-MLP | 4.2593 | 4.4843 | 0.3438 |
| 4 | OurMethod-LC-DQN-MLP | 4.4482 | 4.6461 | 0.5327 |

## lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 47.9495 | 47.6709 | 0.0657 |
| 2 | OurMethod-LC-DQN-MLP | 47.9842 | 47.8333 | 0.1005 |
| 3 | HyperRL-MLP | 48.0659 | 47.6363 | 0.1822 |
| 4 | Random Search | 48.1101 | 47.8861 | 0.2263 |

## lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 20.2008 | 19.1587 | 0.0000 |
| 2 | HyperRL-MLP | 20.7197 | 19.7532 | 0.5188 |
| 3 | OurMethod-LC-DQN-MLP | 20.9038 | 20.0112 | 0.7029 |
| 4 | Random Search | 20.9874 | 20.0112 | 0.7866 |

## lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 11.7808 | 11.8373 | 1.6830 |
| 2 | OurMethod-LC-DQN-MLP | 12.0939 | 11.2861 | 1.9961 |
| 3 | Bayesian Optimization | 12.6810 | 11.9160 | 2.5832 |
| 4 | Random Search | 12.9941 | 12.9396 | 2.8963 |

## lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 0.7490 | 0.7381 | 0.2920 |
| 2 | Bayesian Optimization | 0.8219 | 0.8192 | 0.3649 |
| 3 | OurMethod-LC-DQN-MLP | 0.9779 | 0.9237 | 0.5209 |
| 4 | Random Search | 1.1120 | 1.1202 | 0.6550 |

## lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.2028 | 7.1953 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 5.6085 | 7.4320 | 0.4056 |
| 3 | HyperRL-MLP | 6.0317 | 8.0237 | 0.8289 |
| 4 | Random Search | 6.3492 | 8.1302 | 1.1464 |

## lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.9362 | 29.9642 | 0.0000 |
| 2 | HyperRL-MLP | 21.8085 | 25.2330 | 2.8723 |
| 3 | OurMethod-LC-DQN-MLP | 22.9787 | 26.0932 | 4.0426 |
| 4 | Random Search | 23.5106 | 25.3047 | 4.5745 |

## lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.2367 | 37.2343 | 0.0000 |
| 2 | Random Search | 41.2968 | 41.4177 | 5.0601 |
| 3 | OurMethod-LC-DQN-MLP | 42.0973 | 42.0912 | 5.8605 |
| 4 | HyperRL-MLP | 44.3450 | 44.2945 | 8.1083 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.3368 | 1.74 | 35 |
| 2 | HyperRL-MLP | 1.3438 | 2.63 | 35 |
| 3 | OurMethod-LC-DQN-MLP | 1.3902 | 2.71 | 35 |
| 4 | Random Search | 1.7986 | 2.91 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 22 |
| OurMethod-LC-DQN-MLP | 7 |
| HyperRL-MLP | 6 |
| Random Search | 6 |

Most rank-1 finishes: **Bayesian Optimization** with 22 task(s).

Across the selected tasks, **Bayesian Optimization** gives the best average simple regret (1.3368). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.
