# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.5437 | 1.6045 | 0.1154 |
| 2 | OurMethod-LC-DQN-MLP | 1.6627 | 1.7145 | 0.2345 |
| 3 | Random Search | 1.7377 | 1.8022 | 0.3095 |
| 4 | HyperRL-MLP | 1.9222 | 1.9721 | 0.4939 |

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
| 3 | HyperRL-MLP | 10.0654 | 16.0352 | 0.9150 |
| 4 | OurMethod-LC-DQN-MLP | 10.1961 | 16.6520 | 1.0458 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 12.3259 | 11.6476 | 1.1436 |
| 2 | OurMethod-LC-DQN-MLP | 12.4603 | 11.6078 | 1.2779 |
| 3 | HyperRL-MLP | 12.7420 | 11.9818 | 1.5596 |
| 4 | Random Search | 12.7626 | 11.9065 | 1.5803 |

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
| 1 | Bayesian Optimization | 10.9796 | 11.2581 | 0.1836 |
| 2 | OurMethod-LC-DQN-MLP | 11.5930 | 11.8965 | 0.7970 |
| 3 | Random Search | 12.3379 | 12.6196 | 1.5419 |
| 4 | HyperRL-MLP | 12.6634 | 12.9174 | 1.8674 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 19.2685 | 19.3361 | 0.1481 |
| 2 | OurMethod-LC-DQN-MLP | 19.6000 | 19.7208 | 0.4796 |
| 3 | HyperRL-MLP | 19.7056 | 19.7928 | 0.5852 |
| 4 | Random Search | 19.7593 | 19.8238 | 0.6389 |

## lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 38.5784 | 38.7735 | 0.5241 |
| 2 | OurMethod-LC-DQN-MLP | 39.0763 | 39.1628 | 1.0220 |
| 3 | Random Search | 39.7449 | 39.8446 | 1.6906 |
| 4 | HyperRL-MLP | 39.8222 | 39.8735 | 1.7679 |

## lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 34.5797 | 34.3476 | 0.1785 |
| 2 | Random Search | 35.0003 | 34.7757 | 0.5990 |
| 3 | Bayesian Optimization | 35.0215 | 34.8540 | 0.6203 |
| 4 | HyperRL-MLP | 35.0235 | 34.8096 | 0.6222 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 11.7115 | 11.4471 | 0.0980 |
| 2 | Random Search | 12.0156 | 11.6174 | 0.4021 |
| 3 | HyperRL-MLP | 12.9899 | 12.8387 | 1.3764 |
| 4 | Bayesian Optimization | 15.0185 | 15.3254 | 3.4050 |

## lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 24.6988 | 22.5203 | 1.4458 |
| 2 | HyperRL-MLP | 25.4217 | 22.6016 | 2.1687 |
| 3 | Random Search | 28.3133 | 25.9350 | 5.0602 |
| 4 | Bayesian Optimization | 30.3614 | 29.8374 | 7.1084 |

## lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 9.6084 | 13.7544 | 2.6632 |
| 2 | Random Search | 9.9217 | 13.9298 | 2.9765 |
| 3 | Bayesian Optimization | 10.0261 | 14.4561 | 3.0809 |
| 4 | OurMethod-LC-DQN-MLP | 10.4439 | 14.9825 | 3.4987 |

## lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 26.3773 | 28.1767 | 0.2003 |
| 2 | OurMethod-LC-DQN-MLP | 26.6277 | 28.1320 | 0.4508 |
| 3 | Bayesian Optimization | 26.8280 | 27.9530 | 0.6511 |
| 4 | HyperRL-MLP | 26.8781 | 28.3333 | 0.7012 |

## lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 3.9331 | 5.6742 | 0.2510 |
| 2 | Random Search | 4.0167 | 6.3483 | 0.3347 |
| 3 | Bayesian Optimization | 4.1841 | 5.7303 | 0.5021 |
| 4 | HyperRL-MLP | 4.2678 | 6.4045 | 0.5858 |

## lcbench_connect-4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 30.2865 | 30.0274 | 1.0135 |
| 2 | HyperRL-MLP | 30.9479 | 30.6419 | 1.6749 |
| 3 | Random Search | 31.0269 | 30.7863 | 1.7539 |
| 4 | Bayesian Optimization | 33.5025 | 33.1252 | 4.2295 |

## lcbench_covertype

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 31.6750 | 31.5214 | 2.7916 |
| 2 | OurMethod-LC-DQN-MLP | 32.5727 | 32.3641 | 3.6893 |
| 3 | HyperRL-MLP | 34.1187 | 33.9007 | 5.2353 |
| 4 | Random Search | 34.2039 | 34.0279 | 5.3205 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 27.1171 | 30.3030 | 0.5405 |
| 2 | OurMethod-LC-DQN-MLP | 27.2973 | 29.2727 | 0.7207 |
| 3 | HyperRL-MLP | 27.9279 | 30.2424 | 1.3514 |
| 4 | Bayesian Optimization | 28.1081 | 30.3636 | 1.5315 |

## lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 0.2762 | 0.2636 | 0.0422 |
| 2 | Bayesian Optimization | 0.3354 | 0.3132 | 0.1013 |
| 3 | Random Search | 0.3669 | 0.3473 | 0.1328 |
| 4 | HyperRL-MLP | 0.3686 | 0.3430 | 0.1345 |

## lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.4761 | 35.7117 | 0.0439 |
| 2 | OurMethod-LC-DQN-MLP | 33.9044 | 35.1379 | 0.4723 |
| 3 | HyperRL-MLP | 33.9703 | 35.5057 | 0.5382 |
| 4 | Random Search | 34.1241 | 35.3071 | 0.6919 |

## lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 14.7660 | 14.8748 | 14.6498 |
| 2 | Random Search | 31.6857 | 31.9437 | 31.5695 |
| 3 | Bayesian Optimization | 44.3653 | 64.4584 | 44.2491 |
| 4 | HyperRL-MLP | 47.2276 | 47.5346 | 47.1114 |

## lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 29.9170 | 29.7954 | 1.1937 |
| 2 | Bayesian Optimization | 31.3736 | 31.4365 | 2.6504 |
| 3 | Random Search | 31.4520 | 31.3073 | 2.7288 |
| 4 | HyperRL-MLP | 31.8792 | 31.9119 | 3.1559 |

## lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.6566 | 36.0531 | 1.0014 |
| 2 | OurMethod-LC-DQN-MLP | 37.5943 | 37.0947 | 1.9391 |
| 3 | Random Search | 37.6288 | 37.0433 | 1.9736 |
| 4 | HyperRL-MLP | 39.0310 | 38.5285 | 3.3758 |

## lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.4266 | 24.1260 | 0.0908 |
| 2 | Random Search | 18.4569 | 24.1667 | 0.1210 |
| 3 | HyperRL-MLP | 18.5477 | 24.1260 | 0.2118 |
| 4 | OurMethod-LC-DQN-MLP | 18.7595 | 24.1667 | 0.4236 |

## lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 24.7952 | 23.7417 | 5.3723 |
| 2 | OurMethod-LC-DQN-MLP | 25.2593 | 24.3435 | 5.8365 |
| 3 | Random Search | 25.5076 | 24.5057 | 6.0848 |
| 4 | HyperRL-MLP | 25.8890 | 25.0507 | 6.4662 |

## lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 16.2313 | 17.3813 | 1.6702 |
| 2 | Random Search | 17.0021 | 17.2374 | 2.4411 |
| 3 | Bayesian Optimization | 17.5589 | 17.9856 | 2.9979 |
| 4 | OurMethod-LC-DQN-MLP | 17.9872 | 17.9568 | 3.4261 |

## lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 2.8006 | 2.9981 | 0.4526 |
| 2 | OurMethod-LC-DQN-MLP | 2.8571 | 2.9032 | 0.5092 |
| 3 | Random Search | 3.1117 | 3.2827 | 0.7638 |
| 4 | Bayesian Optimization | 3.1683 | 3.7192 | 0.8204 |

## lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.2506 | 2.0606 | 0.4063 |
| 2 | Random Search | 3.2957 | 2.2121 | 0.4515 |
| 3 | OurMethod-LC-DQN-MLP | 3.2957 | 2.0909 | 0.4515 |
| 4 | HyperRL-MLP | 3.3409 | 2.1818 | 0.4966 |

## lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 4.5243 | 4.7252 | 0.3097 |
| 2 | Bayesian Optimization | 4.7553 | 4.8800 | 0.5406 |
| 3 | Random Search | 5.0282 | 5.0787 | 0.8135 |
| 4 | OurMethod-LC-DQN-MLP | 5.2565 | 5.3583 | 1.0419 |

## lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 48.1260 | 48.0019 | 0.0967 |
| 2 | OurMethod-LC-DQN-MLP | 48.1589 | 47.8383 | 0.1296 |
| 3 | Random Search | 48.1833 | 47.9050 | 0.1540 |
| 4 | HyperRL-MLP | 48.1965 | 47.7615 | 0.1672 |

## lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 21.6736 | 21.0208 | 0.3849 |
| 2 | HyperRL-MLP | 21.9916 | 21.0544 | 0.7029 |
| 3 | OurMethod-LC-DQN-MLP | 22.1423 | 21.6265 | 0.8536 |
| 4 | Bayesian Optimization | 22.2092 | 22.2546 | 0.9205 |

## lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 13.5421 | 13.4121 | 0.6262 |
| 2 | HyperRL-MLP | 14.1292 | 13.9370 | 1.2133 |
| 3 | OurMethod-LC-DQN-MLP | 14.6771 | 14.2257 | 1.7613 |
| 4 | Bayesian Optimization | 15.7339 | 15.2493 | 2.8180 |

## lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 1.7873 | 1.7879 | 0.6956 |
| 2 | OurMethod-LC-DQN-MLP | 1.8247 | 1.8234 | 0.7330 |
| 3 | HyperRL-MLP | 1.8715 | 1.8349 | 0.7798 |
| 4 | Bayesian Optimization | 2.1117 | 2.1285 | 1.0200 |

## lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 5.9259 | 7.6095 | 0.1587 |
| 2 | Bayesian Optimization | 6.1552 | 7.8225 | 0.3880 |
| 3 | HyperRL-MLP | 6.7901 | 8.6864 | 1.0229 |
| 4 | Random Search | 6.9136 | 8.7219 | 1.1464 |

## lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 23.0851 | 25.5914 | 0.9574 |
| 2 | Random Search | 24.4681 | 24.7312 | 2.3404 |
| 3 | OurMethod-LC-DQN-MLP | 25.8511 | 24.4444 | 3.7234 |
| 4 | HyperRL-MLP | 27.4468 | 26.4516 | 5.3192 |

## lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 44.1077 | 44.3819 | 2.4044 |
| 2 | Random Search | 44.4893 | 44.6334 | 2.7860 |
| 3 | OurMethod-LC-DQN-MLP | 45.2245 | 45.3349 | 3.5213 |
| 4 | Bayesian Optimization | 45.8900 | 45.8806 | 4.1868 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 1.6306 | 2.23 | 35 |
| 2 | Random Search | 2.2605 | 2.57 | 35 |
| 3 | Bayesian Optimization | 2.7131 | 2.26 | 35 |
| 4 | HyperRL-MLP | 2.8314 | 2.94 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 16 |
| OurMethod-LC-DQN-MLP | 11 |
| Random Search | 8 |
| HyperRL-MLP | 7 |

Most rank-1 finishes: **Bayesian Optimization** with 16 task(s).

Across the selected tasks, **OurMethod-LC-DQN-MLP** gives the best average simple regret (1.6306). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.
