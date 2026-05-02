# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.5437 | 1.6045 | 0.0762 |
| 2 | Random Search | 1.7377 | 1.8022 | 0.2702 |
| 3 | HyperRL-MLP | 1.7781 | 1.8102 | 0.3106 |
| 4 | OurMethod-LC-DQN-MLP | 1.8043 | 1.8166 | 0.3368 |

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
| 1 | Random Search | 9.4118 | 16.2996 | 0.2614 |
| 2 | Bayesian Optimization | 9.4118 | 15.8590 | 0.2614 |
| 3 | OurMethod-LC-DQN-MLP | 9.4118 | 16.2115 | 0.2614 |
| 4 | HyperRL-MLP | 9.8039 | 16.2996 | 0.6536 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 12.3259 | 11.6476 | 0.9045 |
| 2 | HyperRL-MLP | 12.6024 | 11.8407 | 1.1810 |
| 3 | Random Search | 12.7626 | 11.9065 | 1.3413 |
| 4 | OurMethod-LC-DQN-MLP | 13.3131 | 12.3827 | 1.8917 |

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
| 1 | Bayesian Optimization | 10.9796 | 11.2581 | 0.4514 |
| 2 | OurMethod-LC-DQN-MLP | 11.3127 | 11.5116 | 0.7845 |
| 3 | HyperRL-MLP | 11.9171 | 12.2585 | 1.3889 |
| 4 | Random Search | 12.3379 | 12.6196 | 1.8096 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 19.2685 | 19.3361 | 0.1481 |
| 2 | OurMethod-LC-DQN-MLP | 19.6407 | 19.6836 | 0.5204 |
| 3 | Random Search | 19.7593 | 19.8238 | 0.6389 |
| 4 | HyperRL-MLP | 19.7722 | 19.8163 | 0.6519 |

## lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 38.5784 | 38.7735 | 0.3205 |
| 2 | HyperRL-MLP | 39.3699 | 39.5082 | 1.1120 |
| 3 | Random Search | 39.7449 | 39.8446 | 1.4870 |
| 4 | OurMethod-LC-DQN-MLP | 39.8189 | 39.8833 | 1.5610 |

## lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 34.8443 | 34.6541 | 0.4759 |
| 2 | Random Search | 35.0003 | 34.7757 | 0.6318 |
| 3 | Bayesian Optimization | 35.0215 | 34.8540 | 0.6530 |
| 4 | OurMethod-LC-DQN-MLP | 35.2449 | 34.9942 | 0.8764 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 12.0156 | 11.6174 | 0.0000 |
| 2 | HyperRL-MLP | 13.3660 | 13.3829 | 1.3504 |
| 3 | OurMethod-LC-DQN-MLP | 13.5821 | 13.5947 | 1.5665 |
| 4 | Bayesian Optimization | 15.0185 | 15.3254 | 3.0029 |

## lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 22.5301 | 20.2439 | 0.6024 |
| 2 | HyperRL-MLP | 23.8554 | 20.9756 | 1.9277 |
| 3 | Random Search | 28.3133 | 25.9350 | 6.3855 |
| 4 | Bayesian Optimization | 30.3614 | 29.8374 | 8.4337 |

## lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 8.3551 | 11.7193 | 1.4621 |
| 2 | Random Search | 9.9217 | 13.9298 | 3.0287 |
| 3 | Bayesian Optimization | 10.0261 | 14.4561 | 3.1332 |
| 4 | HyperRL-MLP | 10.7572 | 15.3333 | 3.8642 |

## lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 26.3773 | 28.1767 | 0.1336 |
| 2 | HyperRL-MLP | 26.6611 | 28.2886 | 0.4174 |
| 3 | Bayesian Optimization | 26.8280 | 27.9530 | 0.5843 |
| 4 | OurMethod-LC-DQN-MLP | 27.0117 | 28.2327 | 0.7679 |

## lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 3.8494 | 6.0674 | 0.1674 |
| 2 | Random Search | 4.0167 | 6.3483 | 0.3347 |
| 3 | Bayesian Optimization | 4.1841 | 5.7303 | 0.5021 |
| 4 | OurMethod-LC-DQN-MLP | 4.5188 | 6.7416 | 0.8368 |

## lcbench_connect-4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 31.0269 | 30.7863 | 1.0135 |
| 2 | OurMethod-LC-DQN-MLP | 31.0269 | 30.7863 | 1.0135 |
| 3 | Random Search | 31.0269 | 30.7863 | 1.0135 |
| 4 | Bayesian Optimization | 33.5025 | 33.1252 | 3.4891 |

## lcbench_covertype

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 31.6750 | 31.5214 | 2.7916 |
| 2 | OurMethod-LC-DQN-MLP | 32.7960 | 32.5885 | 3.9126 |
| 3 | HyperRL-MLP | 33.7370 | 33.5560 | 4.8536 |
| 4 | Random Search | 34.2039 | 34.0279 | 5.3205 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 27.1171 | 30.3030 | 0.7207 |
| 2 | OurMethod-LC-DQN-MLP | 27.2973 | 29.6364 | 0.9009 |
| 3 | HyperRL-MLP | 27.4775 | 29.8788 | 1.0811 |
| 4 | Bayesian Optimization | 28.1081 | 30.3636 | 1.7117 |

## lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 0.2341 | 20.0091 | 0.0143 |
| 2 | OurMethod-LC-DQN-MLP | 0.3210 | 0.2984 | 0.1013 |
| 3 | Bayesian Optimization | 0.3354 | 0.3132 | 0.1156 |
| 4 | Random Search | 0.3669 | 0.3473 | 0.1471 |

## lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.4761 | 35.7117 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 33.8605 | 35.1894 | 0.3844 |
| 3 | Random Search | 34.1241 | 35.3071 | 0.6480 |
| 4 | HyperRL-MLP | 34.2120 | 35.2777 | 0.7359 |

## lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 15.6026 | 15.6566 | 15.3907 |
| 2 | HyperRL-MLP | 31.4415 | 31.6574 | 31.2296 |
| 3 | Random Search | 31.6857 | 31.9437 | 31.4737 |
| 4 | Bayesian Optimization | 44.3653 | 64.4584 | 44.1534 |

## lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 30.7159 | 30.5285 | 1.4954 |
| 2 | Bayesian Optimization | 31.3736 | 31.4365 | 2.1531 |
| 3 | Random Search | 31.4520 | 31.3073 | 2.2315 |
| 4 | OurMethod-LC-DQN-MLP | 31.9059 | 31.9174 | 2.6854 |

## lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.6566 | 36.0531 | 0.9809 |
| 2 | Random Search | 37.6288 | 37.0433 | 1.9531 |
| 3 | HyperRL-MLP | 38.0544 | 37.3987 | 2.3787 |
| 4 | OurMethod-LC-DQN-MLP | 38.3105 | 37.7367 | 2.6348 |

## lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.4266 | 24.1260 | 0.1210 |
| 2 | Random Search | 18.4569 | 24.1667 | 0.1513 |
| 3 | OurMethod-LC-DQN-MLP | 18.4871 | 24.4106 | 0.1815 |
| 4 | HyperRL-MLP | 18.7897 | 24.1870 | 0.4841 |

## lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 24.7952 | 23.7417 | 3.8809 |
| 2 | Random Search | 25.5076 | 24.5057 | 4.5933 |
| 3 | HyperRL-MLP | 26.0323 | 25.0223 | 5.1181 |
| 4 | OurMethod-LC-DQN-MLP | 26.9284 | 26.0054 | 6.0141 |

## lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 15.7173 | 16.2878 | 0.8994 |
| 2 | Random Search | 17.0021 | 17.2374 | 2.1842 |
| 3 | Bayesian Optimization | 17.5589 | 17.9856 | 2.7409 |
| 4 | HyperRL-MLP | 17.9443 | 18.3597 | 3.1263 |

## lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 2.2065 | 2.4288 | 0.0000 |
| 2 | Random Search | 3.1117 | 3.2827 | 0.9052 |
| 3 | Bayesian Optimization | 3.1683 | 3.7192 | 0.9618 |
| 4 | HyperRL-MLP | 3.4795 | 3.3776 | 1.2730 |

## lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 3.1151 | 2.2424 | 0.3160 |
| 2 | Bayesian Optimization | 3.2506 | 2.0606 | 0.4515 |
| 3 | Random Search | 3.2957 | 2.2121 | 0.4966 |
| 4 | HyperRL-MLP | 3.4312 | 2.0303 | 0.6321 |

## lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 4.7553 | 4.8800 | 0.3307 |
| 2 | HyperRL-MLP | 4.8655 | 4.9802 | 0.4409 |
| 3 | Random Search | 5.0282 | 5.0787 | 0.6036 |
| 4 | OurMethod-LC-DQN-MLP | 5.1673 | 5.2334 | 0.7427 |

## lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 48.1260 | 48.0019 | 0.0150 |
| 2 | Random Search | 48.1833 | 47.9050 | 0.0723 |
| 3 | HyperRL-MLP | 48.2274 | 47.8402 | 0.1164 |
| 4 | OurMethod-LC-DQN-MLP | 48.2519 | 48.0233 | 0.1409 |

## lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 21.2050 | 21.0320 | 0.5858 |
| 2 | OurMethod-LC-DQN-MLP | 21.4393 | 20.6282 | 0.8201 |
| 3 | Random Search | 21.6736 | 21.0208 | 1.0544 |
| 4 | Bayesian Optimization | 22.2092 | 22.2546 | 1.5900 |

## lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 13.5421 | 13.4121 | 0.6262 |
| 2 | OurMethod-LC-DQN-MLP | 14.1292 | 14.1995 | 1.2133 |
| 3 | HyperRL-MLP | 14.8337 | 14.3570 | 1.9178 |
| 4 | Bayesian Optimization | 15.7339 | 15.2493 | 2.8180 |

## lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 1.6578 | 1.6635 | 0.5552 |
| 2 | HyperRL-MLP | 1.7249 | 1.7064 | 0.6223 |
| 3 | Random Search | 1.7873 | 1.7879 | 0.6847 |
| 4 | Bayesian Optimization | 2.1117 | 2.1285 | 1.0090 |

## lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 6.1552 | 7.8225 | 0.3704 |
| 2 | OurMethod-LC-DQN-MLP | 6.2787 | 7.9527 | 0.4938 |
| 3 | HyperRL-MLP | 6.6843 | 8.0828 | 0.8995 |
| 4 | Random Search | 6.9136 | 8.7219 | 1.1287 |

## lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 23.0851 | 25.5914 | 2.1277 |
| 2 | HyperRL-MLP | 24.0426 | 24.4444 | 3.0851 |
| 3 | OurMethod-LC-DQN-MLP | 24.2553 | 23.3692 | 3.2979 |
| 4 | Random Search | 24.4681 | 24.7312 | 3.5106 |

## lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 44.4893 | 44.6334 | 1.4070 |
| 2 | HyperRL-MLP | 44.9593 | 45.0366 | 1.8770 |
| 3 | OurMethod-LC-DQN-MLP | 45.5658 | 45.5781 | 2.4835 |
| 4 | Bayesian Optimization | 45.8900 | 45.8806 | 2.8077 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 1.5900 | 2.63 | 35 |
| 2 | HyperRL-MLP | 2.1852 | 2.54 | 35 |
| 3 | Random Search | 2.2071 | 2.57 | 35 |
| 4 | Bayesian Optimization | 2.6598 | 2.26 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 17 |
| OurMethod-LC-DQN-MLP | 11 |
| Random Search | 9 |
| HyperRL-MLP | 8 |

Most rank-1 finishes: **Bayesian Optimization** with 17 task(s).

Across the selected tasks, **OurMethod-LC-DQN-MLP** gives the best average simple regret (1.5900). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.
