# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.1402 | 1.1467 | 0.0226 |
| 2 | Random Search | 1.3413 | 1.3860 | 0.2238 |
| 3 | OurMethod-LC-DQN-MLP | 1.3652 | 1.4474 | 0.2476 |
| 4 | HyperRL-MLP | 1.4163 | 1.4609 | 0.2987 |

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
| 1 | Random Search | 9.0196 | 15.9471 | 0.0000 |
| 2 | Bayesian Optimization | 9.1503 | 16.1233 | 0.1307 |
| 3 | HyperRL-MLP | 9.1503 | 16.2115 | 0.1307 |
| 4 | OurMethod-LC-DQN-MLP | 9.1503 | 16.4758 | 0.1307 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.6435 | 9.9887 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 10.9174 | 10.1186 | 0.2739 |
| 3 | Random Search | 11.2922 | 10.4918 | 0.6487 |
| 4 | HyperRL-MLP | 11.3904 | 10.6511 | 0.7469 |

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
| 1 | Bayesian Optimization | 9.6964 | 9.8099 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 10.6165 | 10.8499 | 0.9201 |
| 3 | Random Search | 10.7104 | 10.9301 | 1.0140 |
| 4 | HyperRL-MLP | 10.8544 | 11.1192 | 1.1580 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.4093 | 18.5568 | 0.7648 |
| 2 | OurMethod-LC-DQN-MLP | 18.4389 | 18.7578 | 0.7944 |
| 3 | HyperRL-MLP | 18.5593 | 18.7913 | 0.9148 |
| 4 | Random Search | 19.4352 | 19.4577 | 1.7907 |

## lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.5939 | 36.8202 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 38.0947 | 38.2736 | 1.5008 |
| 3 | Random Search | 38.0984 | 38.2811 | 1.5045 |
| 4 | HyperRL-MLP | 38.2378 | 38.3932 | 1.6438 |

## lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.7722 | 33.7485 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 34.0641 | 33.7991 | 0.2919 |
| 3 | Random Search | 34.2134 | 33.9370 | 0.4412 |
| 4 | HyperRL-MLP | 34.4863 | 34.2787 | 0.7141 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 11.5415 | 11.2032 | 0.0740 |
| 2 | OurMethod-LC-DQN-MLP | 11.6715 | 11.3694 | 0.2041 |
| 3 | HyperRL-MLP | 11.7095 | 11.3493 | 0.2421 |
| 4 | Bayesian Optimization | 11.7275 | 11.5718 | 0.2601 |

## lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 21.2048 | 19.2683 | 0.2410 |
| 2 | OurMethod-LC-DQN-MLP | 21.5663 | 19.6748 | 0.6024 |
| 3 | Random Search | 21.5663 | 18.8618 | 0.6024 |
| 4 | HyperRL-MLP | 21.6867 | 19.5122 | 0.7229 |

## lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.1332 | 6.1404 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 7.1018 | 10.4561 | 3.9687 |
| 3 | Random Search | 7.7807 | 11.2281 | 4.6475 |
| 4 | HyperRL-MLP | 7.8329 | 12.0702 | 4.6997 |

## lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 25.7095 | 27.9642 | 0.0835 |
| 2 | OurMethod-LC-DQN-MLP | 26.0267 | 27.7852 | 0.4007 |
| 3 | HyperRL-MLP | 26.0601 | 28.0313 | 0.4341 |
| 4 | Random Search | 26.2104 | 27.9866 | 0.5843 |

## lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 3.1799 | 5.9551 | 0.1674 |
| 2 | OurMethod-LC-DQN-MLP | 3.3473 | 6.3483 | 0.3347 |
| 3 | HyperRL-MLP | 3.5983 | 6.4607 | 0.5858 |
| 4 | Bayesian Optimization | 3.5983 | 6.1236 | 0.5858 |

## lcbench_connect-4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.5243 | 26.1203 | 0.0000 |
| 2 | HyperRL-MLP | 28.8794 | 28.4251 | 2.3551 |
| 3 | Random Search | 29.3266 | 28.9965 | 2.8022 |
| 4 | OurMethod-LC-DQN-MLP | 30.4244 | 30.0964 | 3.9001 |

## lcbench_covertype

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 22.9561 | 22.8193 | 0.0000 |
| 2 | HyperRL-MLP | 29.8971 | 29.7583 | 6.9410 |
| 3 | OurMethod-LC-DQN-MLP | 30.7345 | 30.5004 | 7.7785 |
| 4 | Random Search | 30.9495 | 30.7191 | 7.9935 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 25.6757 | 30.9697 | 0.3604 |
| 2 | OurMethod-LC-DQN-MLP | 26.0360 | 26.9697 | 0.7207 |
| 3 | Random Search | 26.6667 | 29.4545 | 1.3513 |
| 4 | HyperRL-MLP | 26.6667 | 28.9091 | 1.3513 |

## lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 0.1582 | 59.5207 | 0.1239 |
| 2 | Random Search | 0.1600 | 19.9679 | 0.1256 |
| 3 | Bayesian Optimization | 0.2180 | 0.2168 | 0.1837 |
| 4 | HyperRL-MLP | 0.2304 | 0.2547 | 0.1960 |

## lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.2345 | 35.4395 | 0.0329 |
| 2 | Random Search | 33.5310 | 35.2777 | 0.3295 |
| 3 | OurMethod-LC-DQN-MLP | 33.5969 | 35.2850 | 0.3954 |
| 4 | HyperRL-MLP | 33.6518 | 35.0938 | 0.4503 |

## lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.0524 | 19.9020 | 0.0194 |
| 2 | OurMethod-LC-DQN-MLP | 0.0843 | 19.9076 | 0.0513 |
| 3 | HyperRL-MLP | 0.0940 | 0.1755 | 0.0610 |
| 4 | Random Search | 0.1439 | 0.2164 | 0.1110 |

## lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 28.2094 | 28.1654 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 28.9299 | 28.9449 | 0.7205 |
| 3 | Random Search | 29.3423 | 29.2385 | 1.1328 |
| 4 | HyperRL-MLP | 29.5332 | 29.3584 | 1.3238 |

## lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.8403 | 33.4858 | 0.0000 |
| 2 | HyperRL-MLP | 35.4164 | 34.7250 | 1.5761 |
| 3 | Random Search | 35.6066 | 34.9920 | 1.7662 |
| 4 | OurMethod-LC-DQN-MLP | 36.1316 | 35.4241 | 2.2912 |

## lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.0938 | 24.2886 | 0.1513 |
| 2 | Random Search | 18.1543 | 24.2480 | 0.2118 |
| 3 | HyperRL-MLP | 18.1543 | 24.0244 | 0.2118 |
| 4 | OurMethod-LC-DQN-MLP | 18.3056 | 24.4309 | 0.3631 |

## lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 16.1958 | 14.9561 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 19.2674 | 18.0365 | 3.0716 |
| 3 | Random Search | 19.8607 | 18.6058 | 3.6650 |
| 4 | HyperRL-MLP | 21.6327 | 20.4787 | 5.4369 |

## lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 14.1328 | 14.5036 | 0.4711 |
| 2 | OurMethod-LC-DQN-MLP | 14.1328 | 14.4460 | 0.4711 |
| 3 | Random Search | 14.7752 | 14.9353 | 1.1135 |
| 4 | Bayesian Optimization | 15.2463 | 15.9712 | 1.5846 |

## lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.4144 | 2.2770 | 0.0000 |
| 2 | HyperRL-MLP | 2.2348 | 2.5047 | 0.8204 |
| 3 | Random Search | 2.3479 | 2.5806 | 0.9335 |
| 4 | OurMethod-LC-DQN-MLP | 2.4045 | 2.4858 | 0.9901 |

## lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 2.5282 | 1.5455 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 2.7540 | 1.6970 | 0.2257 |
| 3 | Random Search | 2.9345 | 1.9697 | 0.4063 |
| 4 | HyperRL-MLP | 2.9797 | 1.7273 | 0.4515 |

## lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.8446 | 4.0886 | 0.0000 |
| 2 | HyperRL-MLP | 4.0782 | 4.3348 | 0.2336 |
| 3 | Random Search | 4.2094 | 4.4034 | 0.3648 |
| 4 | OurMethod-LC-DQN-MLP | 4.3013 | 4.4456 | 0.4566 |

## lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 47.8039 | 47.5979 | 0.0000 |
| 2 | Random Search | 48.0321 | 47.7414 | 0.2282 |
| 3 | HyperRL-MLP | 48.0368 | 47.9792 | 0.2329 |
| 4 | OurMethod-LC-DQN-MLP | 48.0969 | 47.7106 | 0.2930 |

## lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 20.1172 | 19.0690 | 0.0000 |
| 2 | HyperRL-MLP | 20.5858 | 19.5850 | 0.4686 |
| 3 | OurMethod-LC-DQN-MLP | 20.8201 | 20.1458 | 0.7029 |
| 4 | Random Search | 20.8536 | 19.7420 | 0.7364 |

## lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.8023 | 10.7612 | 0.8611 |
| 2 | HyperRL-MLP | 12.7202 | 12.4409 | 2.7789 |
| 3 | OurMethod-LC-DQN-MLP | 12.7593 | 12.2572 | 2.8180 |
| 4 | Random Search | 12.9159 | 13.0709 | 2.9746 |

## lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.4570 | 0.4472 | 0.0000 |
| 2 | HyperRL-MLP | 0.7689 | 0.7565 | 0.3119 |
| 3 | Random Search | 0.8581 | 0.8614 | 0.4012 |
| 4 | OurMethod-LC-DQN-MLP | 0.9935 | 0.9770 | 0.5365 |

## lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.2028 | 7.1953 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 5.6790 | 7.7278 | 0.4762 |
| 3 | HyperRL-MLP | 5.9436 | 7.8698 | 0.7407 |
| 4 | Random Search | 6.0670 | 7.9645 | 0.8642 |

## lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.6170 | 30.3226 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 20.7447 | 27.1685 | 2.1277 |
| 3 | Random Search | 21.2766 | 26.8100 | 2.6596 |
| 4 | HyperRL-MLP | 23.6170 | 25.5914 | 5.0000 |

## lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.2367 | 37.2343 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 40.0248 | 40.1164 | 3.7881 |
| 3 | HyperRL-MLP | 40.5212 | 40.7348 | 4.2845 |
| 4 | Random Search | 41.2968 | 41.4177 | 5.0601 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.1509 | 1.34 | 35 |
| 2 | OurMethod-LC-DQN-MLP | 1.1992 | 2.63 | 35 |
| 3 | Random Search | 1.3409 | 2.97 | 35 |
| 4 | HyperRL-MLP | 1.3711 | 3.06 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 30 |
| Random Search | 5 |
| OurMethod-LC-DQN-MLP | 4 |
| HyperRL-MLP | 3 |

Most rank-1 finishes: **Bayesian Optimization** with 30 task(s).

Across the selected tasks, **Bayesian Optimization** gives the best average simple regret (0.1509). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.
