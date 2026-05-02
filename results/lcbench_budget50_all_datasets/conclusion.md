# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.2533 | 1.2903 | 0.0512 |
| 2 | Random Search | 1.4699 | 1.5152 | 0.2678 |
| 3 | HyperRL-MLP | 1.5234 | 1.5662 | 0.3214 |
| 4 | OurMethod-LC-DQN-MLP | 1.5318 | 1.5877 | 0.3297 |

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
| 2 | HyperRL-MLP | 9.1503 | 16.2996 | 0.1307 |
| 3 | Bayesian Optimization | 9.2810 | 15.8590 | 0.2614 |
| 4 | OurMethod-LC-DQN-MLP | 9.2810 | 16.6520 | 0.2614 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.8373 | 10.1922 | 0.1460 |
| 2 | OurMethod-LC-DQN-MLP | 11.0531 | 10.3039 | 0.3618 |
| 3 | Random Search | 11.2922 | 10.4918 | 0.6009 |
| 4 | HyperRL-MLP | 11.4989 | 10.7550 | 0.8076 |

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
| 3 | OurMethod-LC-DQN-MLP | 11.3392 | 11.5568 | 1.4932 |
| 4 | HyperRL-MLP | 11.4310 | 11.6756 | 1.5850 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 18.9037 | 19.0557 | 0.1037 |
| 2 | Bayesian Optimization | 19.0407 | 19.1289 | 0.2407 |
| 3 | OurMethod-LC-DQN-MLP | 19.0944 | 19.1748 | 0.2944 |
| 4 | Random Search | 19.4963 | 19.5284 | 0.6963 |

## lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.7045 | 36.9143 | 0.0000 |
| 2 | Random Search | 38.4603 | 38.6168 | 1.7559 |
| 3 | OurMethod-LC-DQN-MLP | 38.5601 | 38.7601 | 1.8556 |
| 4 | HyperRL-MLP | 39.5626 | 39.6434 | 2.8582 |

## lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.7722 | 33.7485 | 0.0000 |
| 2 | Random Search | 34.2134 | 33.9370 | 0.4412 |
| 3 | OurMethod-LC-DQN-MLP | 34.3738 | 34.1456 | 0.6016 |
| 4 | HyperRL-MLP | 34.4772 | 34.2682 | 0.7050 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 11.6495 | 11.3600 | 0.0360 |
| 2 | OurMethod-LC-DQN-MLP | 11.6595 | 11.3453 | 0.0460 |
| 3 | HyperRL-MLP | 11.6795 | 11.3949 | 0.0660 |
| 4 | Bayesian Optimization | 14.0282 | 14.2825 | 2.4147 |

## lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 21.5663 | 19.4309 | 0.4819 |
| 2 | Random Search | 22.2892 | 19.5122 | 1.2048 |
| 3 | HyperRL-MLP | 23.0120 | 21.1382 | 1.9277 |
| 4 | Bayesian Optimization | 24.5783 | 23.0081 | 3.4940 |

## lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 4.2820 | 7.3333 | 0.0000 |
| 2 | HyperRL-MLP | 7.4151 | 10.7719 | 3.1332 |
| 3 | OurMethod-LC-DQN-MLP | 7.7807 | 11.4386 | 3.4987 |
| 4 | Random Search | 8.0418 | 11.5789 | 3.7598 |

## lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.0434 | 28.0649 | 0.3339 |
| 2 | OurMethod-LC-DQN-MLP | 26.3272 | 27.7740 | 0.6177 |
| 3 | Random Search | 26.3272 | 28.1096 | 0.6177 |
| 4 | HyperRL-MLP | 26.4775 | 28.1320 | 0.7679 |

## lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 3.3473 | 6.0674 | 0.0837 |
| 2 | OurMethod-LC-DQN-MLP | 3.4310 | 6.0674 | 0.1674 |
| 3 | HyperRL-MLP | 3.8494 | 5.7865 | 0.5858 |
| 4 | Bayesian Optimization | 4.0167 | 5.7865 | 0.7531 |

## lcbench_connect-4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 28.2688 | 27.8715 | 1.7445 |
| 2 | Random Search | 29.3266 | 28.9965 | 2.8022 |
| 3 | HyperRL-MLP | 29.5073 | 29.0764 | 2.9830 |
| 4 | OurMethod-LC-DQN-MLP | 29.5127 | 29.0791 | 2.9883 |

## lcbench_covertype

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 23.1785 | 23.1012 | 0.0000 |
| 2 | Random Search | 31.2002 | 30.9789 | 8.0217 |
| 3 | OurMethod-LC-DQN-MLP | 31.5354 | 31.3093 | 8.3569 |
| 4 | HyperRL-MLP | 31.9120 | 31.7400 | 8.7335 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 26.8468 | 29.6364 | 0.9910 |
| 2 | Bayesian Optimization | 26.8468 | 30.4848 | 0.9910 |
| 3 | OurMethod-LC-DQN-MLP | 26.9369 | 29.0303 | 1.0811 |
| 4 | HyperRL-MLP | 27.2973 | 30.0606 | 1.4414 |

## lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 0.1354 | 0.1552 | 0.0309 |
| 2 | Random Search | 0.2619 | 0.2757 | 0.1574 |
| 3 | Bayesian Optimization | 0.2643 | 0.2556 | 0.1597 |
| 4 | HyperRL-MLP | 0.3215 | 0.2982 | 0.2169 |

## lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.4102 | 35.7411 | 0.0439 |
| 2 | OurMethod-LC-DQN-MLP | 33.6409 | 35.1894 | 0.2746 |
| 3 | Random Search | 33.6518 | 35.3292 | 0.2856 |
| 4 | HyperRL-MLP | 33.8166 | 35.0791 | 0.4503 |

## lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 0.1592 | 20.0033 | 0.1235 |
| 2 | OurMethod-LC-DQN-MLP | 0.2105 | 20.0526 | 0.1748 |
| 3 | Random Search | 14.7743 | 14.9287 | 14.7386 |
| 4 | Bayesian Optimization | 28.7526 | 48.8202 | 28.7169 |

## lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 28.8303 | 28.7823 | 0.5535 |
| 2 | Bayesian Optimization | 28.9336 | 28.8559 | 0.6568 |
| 3 | Random Search | 29.3423 | 29.2385 | 1.0655 |
| 4 | HyperRL-MLP | 30.0858 | 29.9493 | 1.8090 |

## lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.8403 | 33.4858 | 0.0000 |
| 2 | Random Search | 35.6066 | 34.9920 | 1.7662 |
| 3 | OurMethod-LC-DQN-MLP | 36.0581 | 35.3981 | 2.2178 |
| 4 | HyperRL-MLP | 36.8035 | 36.0531 | 2.9632 |

## lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.1543 | 24.2683 | 0.1210 |
| 2 | Random Search | 18.2148 | 24.2480 | 0.1815 |
| 3 | OurMethod-LC-DQN-MLP | 18.3359 | 24.2073 | 0.3026 |
| 4 | HyperRL-MLP | 18.3964 | 23.9634 | 0.3631 |

## lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 16.4945 | 15.2644 | 0.0000 |
| 2 | Random Search | 19.8607 | 18.6058 | 3.3663 |
| 3 | OurMethod-LC-DQN-MLP | 21.4975 | 20.4084 | 5.0030 |
| 4 | HyperRL-MLP | 22.5691 | 21.4604 | 6.0747 |

## lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 15.4176 | 15.7986 | 0.7281 |
| 2 | Random Search | 15.6745 | 15.9424 | 0.9850 |
| 3 | HyperRL-MLP | 16.5311 | 17.2086 | 1.8415 |
| 4 | Bayesian Optimization | 17.0021 | 17.6691 | 2.3126 |

## lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.4144 | 2.2770 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 1.9236 | 2.2581 | 0.5092 |
| 3 | HyperRL-MLP | 2.0085 | 2.4099 | 0.5941 |
| 4 | Random Search | 2.5460 | 2.6755 | 1.1315 |

## lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 2.7540 | 1.8485 | 0.0903 |
| 2 | HyperRL-MLP | 2.8894 | 1.6970 | 0.2257 |
| 3 | Bayesian Optimization | 3.0248 | 1.8788 | 0.3612 |
| 4 | Random Search | 3.0700 | 1.8182 | 0.4063 |

## lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.9339 | 4.1502 | 0.0184 |
| 2 | Random Search | 4.2094 | 4.4034 | 0.2939 |
| 3 | OurMethod-LC-DQN-MLP | 4.3406 | 4.4368 | 0.4251 |
| 4 | HyperRL-MLP | 4.6162 | 4.7411 | 0.7007 |

## lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 47.9495 | 47.6709 | 0.0779 |
| 2 | HyperRL-MLP | 48.0293 | 47.7112 | 0.1578 |
| 3 | OurMethod-LC-DQN-MLP | 48.0518 | 47.9453 | 0.1803 |
| 4 | Random Search | 48.1101 | 47.8861 | 0.2385 |

## lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 20.2008 | 19.1587 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 20.6527 | 20.2916 | 0.4519 |
| 3 | HyperRL-MLP | 20.6695 | 20.3814 | 0.4686 |
| 4 | Random Search | 20.9874 | 20.0112 | 0.7866 |

## lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 12.4070 | 11.4961 | 1.6047 |
| 2 | OurMethod-LC-DQN-MLP | 12.5636 | 12.1522 | 1.7613 |
| 3 | Bayesian Optimization | 12.6810 | 11.9160 | 1.8787 |
| 4 | Random Search | 12.9941 | 12.9396 | 2.1918 |

## lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.8219 | 0.8192 | 0.3649 |
| 2 | HyperRL-MLP | 1.0496 | 1.0355 | 0.5926 |
| 3 | Random Search | 1.1120 | 1.1202 | 0.6550 |
| 4 | OurMethod-LC-DQN-MLP | 1.1868 | 1.1661 | 0.7299 |

## lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.2028 | 7.1953 | 0.0000 |
| 2 | HyperRL-MLP | 5.6790 | 7.6923 | 0.4762 |
| 3 | OurMethod-LC-DQN-MLP | 5.8377 | 7.8935 | 0.6349 |
| 4 | Random Search | 6.3492 | 8.1302 | 1.1464 |

## lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.9362 | 29.9642 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 22.8723 | 23.6559 | 3.9362 |
| 3 | Random Search | 23.5106 | 25.3047 | 4.5745 |
| 4 | HyperRL-MLP | 23.8298 | 25.3763 | 4.8936 |

## lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.2367 | 37.2343 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 40.0248 | 40.1164 | 3.7881 |
| 3 | HyperRL-MLP | 40.9540 | 40.9468 | 4.7173 |
| 4 | Random Search | 41.2968 | 41.4177 | 5.0601 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 1.2637 | 2.51 | 35 |
| 2 | Bayesian Optimization | 1.2898 | 1.74 | 35 |
| 3 | HyperRL-MLP | 1.5550 | 3.03 | 35 |
| 4 | Random Search | 1.7516 | 2.71 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 23 |
| OurMethod-LC-DQN-MLP | 7 |
| HyperRL-MLP | 6 |
| Random Search | 6 |

Most rank-1 finishes: **Bayesian Optimization** with 23 task(s).

Across the selected tasks, **OurMethod-LC-DQN-MLP** gives the best average simple regret (1.2637). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.
