# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.1402 | 1.1467 | 0.0226 |
| 2 | OurMethod-LC-DQN-MLP | 1.2580 | 1.2998 | 0.1404 |
| 3 | HyperRL-MLP | 1.3378 | 1.3796 | 0.2202 |
| 4 | Random Search | 1.3413 | 1.3860 | 0.2238 |

## lcbench_Amazon_employee_access

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 5.9177 | 5.7888 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 5.9177 | 5.7888 | 0.0000 |
| 3 | Bayesian Optimization | 5.9205 | 5.7888 | 0.0028 |
| 4 | Random Search | 5.9205 | 5.7888 | 0.0028 |

## lcbench_Australian

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 9.0196 | 15.9471 | 0.0000 |
| 2 | Bayesian Optimization | 9.1503 | 16.1233 | 0.1307 |
| 3 | HyperRL-MLP | 9.1503 | 16.2996 | 0.1307 |
| 4 | OurMethod-LC-DQN-MLP | 9.1503 | 16.2115 | 0.1307 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.6435 | 9.9887 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 11.0945 | 10.3316 | 0.4510 |
| 3 | HyperRL-MLP | 11.2301 | 10.4381 | 0.5866 |
| 4 | Random Search | 11.2922 | 10.4918 | 0.6487 |

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
| 2 | HyperRL-MLP | 10.4774 | 10.6957 | 0.7810 |
| 3 | Random Search | 10.7104 | 10.9301 | 1.0140 |
| 4 | OurMethod-LC-DQN-MLP | 11.0950 | 11.3089 | 1.3986 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 18.0093 | 18.2912 | 0.5611 |
| 2 | Bayesian Optimization | 18.4093 | 18.5568 | 0.9611 |
| 3 | OurMethod-LC-DQN-MLP | 18.4204 | 18.7975 | 0.9722 |
| 4 | Random Search | 19.4352 | 19.4577 | 1.9870 |

## lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.5939 | 36.8202 | 0.0000 |
| 2 | HyperRL-MLP | 37.5032 | 37.7234 | 0.9093 |
| 3 | OurMethod-LC-DQN-MLP | 37.9938 | 38.1591 | 1.3998 |
| 4 | Random Search | 38.0984 | 38.2811 | 1.5045 |

## lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.7722 | 33.7485 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 34.0766 | 33.7691 | 0.3044 |
| 3 | Random Search | 34.2134 | 33.9370 | 0.4412 |
| 4 | HyperRL-MLP | 34.3883 | 34.2055 | 0.6160 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 11.5415 | 11.2032 | 0.1841 |
| 2 | OurMethod-LC-DQN-MLP | 11.5475 | 11.1361 | 0.1901 |
| 3 | HyperRL-MLP | 11.6435 | 11.1388 | 0.2861 |
| 4 | Bayesian Optimization | 11.7275 | 11.5718 | 0.3701 |

## lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 21.2048 | 19.2683 | 0.2410 |
| 2 | Random Search | 21.5663 | 18.8618 | 0.6024 |
| 3 | HyperRL-MLP | 21.6867 | 19.1870 | 0.7229 |
| 4 | OurMethod-LC-DQN-MLP | 21.9277 | 19.7561 | 0.9639 |

## lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.1332 | 6.1404 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 7.4674 | 11.0877 | 4.3342 |
| 3 | Random Search | 7.7807 | 11.2281 | 4.6475 |
| 4 | HyperRL-MLP | 7.9373 | 12.2456 | 4.8042 |

## lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 25.7095 | 27.9642 | 0.0835 |
| 2 | OurMethod-LC-DQN-MLP | 26.1603 | 27.7181 | 0.5342 |
| 3 | Random Search | 26.2104 | 27.9866 | 0.5843 |
| 4 | HyperRL-MLP | 26.2938 | 27.8971 | 0.6678 |

## lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 3.1799 | 5.9551 | 0.1674 |
| 2 | HyperRL-MLP | 3.5983 | 6.0112 | 0.5858 |
| 3 | OurMethod-LC-DQN-MLP | 3.5983 | 5.7865 | 0.5858 |
| 4 | Bayesian Optimization | 3.5983 | 6.1236 | 0.5858 |

## lcbench_connect-4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.5243 | 26.1203 | 0.0000 |
| 2 | Random Search | 29.3266 | 28.9965 | 2.8022 |
| 3 | HyperRL-MLP | 29.4899 | 29.0890 | 2.9656 |
| 4 | OurMethod-LC-DQN-MLP | 30.3441 | 29.9520 | 3.8198 |

## lcbench_covertype

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 22.9561 | 22.8193 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 29.3710 | 29.1634 | 6.4150 |
| 3 | HyperRL-MLP | 30.6723 | 30.4535 | 7.7162 |
| 4 | Random Search | 30.9495 | 30.7191 | 7.9935 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 25.6757 | 30.9697 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 26.3964 | 29.2727 | 0.7207 |
| 3 | Random Search | 26.6667 | 29.4545 | 0.9910 |
| 4 | HyperRL-MLP | 26.8468 | 31.2121 | 1.1712 |

## lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 0.1600 | 19.9679 | 0.0898 |
| 2 | OurMethod-LC-DQN-MLP | 0.1850 | 19.9641 | 0.1148 |
| 3 | HyperRL-MLP | 0.1963 | 0.1914 | 0.1261 |
| 4 | Bayesian Optimization | 0.2180 | 0.2168 | 0.1478 |

## lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.2345 | 35.4395 | 0.0439 |
| 2 | OurMethod-LC-DQN-MLP | 33.4102 | 35.2483 | 0.2197 |
| 3 | Random Search | 33.5310 | 35.2777 | 0.3405 |
| 4 | HyperRL-MLP | 33.6189 | 35.5057 | 0.4283 |

## lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.0524 | 19.9020 | 0.0264 |
| 2 | OurMethod-LC-DQN-MLP | 0.0760 | 0.1327 | 0.0499 |
| 3 | HyperRL-MLP | 0.1134 | 0.1717 | 0.0874 |
| 4 | Random Search | 0.1439 | 0.2164 | 0.1179 |

## lcbench_higgs

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 28.2094 | 28.1654 | 0.0000 |
| 2 | Random Search | 29.3423 | 29.2385 | 1.1328 |
| 3 | OurMethod-LC-DQN-MLP | 29.4991 | 29.4511 | 1.2897 |
| 4 | HyperRL-MLP | 29.7546 | 29.6032 | 1.5452 |

## lcbench_jannis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.8403 | 33.4858 | 0.0000 |
| 2 | Random Search | 35.6066 | 34.9920 | 1.7662 |
| 3 | OurMethod-LC-DQN-MLP | 35.9501 | 35.3518 | 2.1098 |
| 4 | HyperRL-MLP | 36.4286 | 35.9279 | 2.5883 |

## lcbench_jasmine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.0938 | 24.2886 | 0.0908 |
| 2 | Random Search | 18.1543 | 24.2480 | 0.1513 |
| 3 | OurMethod-LC-DQN-MLP | 18.2753 | 24.2480 | 0.2723 |
| 4 | HyperRL-MLP | 18.3056 | 24.2886 | 0.3026 |

## lcbench_jungle_chess_2pcs_raw_endgame_complete

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 16.1958 | 14.9561 | 0.0000 |
| 2 | Random Search | 19.8607 | 18.6058 | 3.6650 |
| 3 | OurMethod-LC-DQN-MLP | 20.1715 | 18.9588 | 3.9758 |
| 4 | HyperRL-MLP | 22.4904 | 21.3252 | 6.2947 |

## lcbench_kc1

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 13.7902 | 14.0432 | 0.0428 |
| 2 | HyperRL-MLP | 14.5610 | 15.6259 | 0.8137 |
| 3 | Random Search | 14.7752 | 14.9353 | 1.0278 |
| 4 | Bayesian Optimization | 15.2463 | 15.9712 | 1.4989 |

## lcbench_kr-vs-kp

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.4144 | 2.2770 | 0.0000 |
| 2 | HyperRL-MLP | 2.1499 | 2.4099 | 0.7355 |
| 3 | OurMethod-LC-DQN-MLP | 2.1782 | 2.4858 | 0.7638 |
| 4 | Random Search | 2.3479 | 2.5806 | 0.9335 |

## lcbench_mfeat-factors

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 2.5282 | 1.5455 | 0.0000 |
| 2 | HyperRL-MLP | 2.8442 | 1.7273 | 0.3160 |
| 3 | OurMethod-LC-DQN-MLP | 2.8894 | 1.7576 | 0.3612 |
| 4 | Random Search | 2.9345 | 1.9697 | 0.4063 |

## lcbench_nomao

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.8446 | 4.0886 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 4.1097 | 4.3084 | 0.2651 |
| 3 | Random Search | 4.2094 | 4.4034 | 0.3648 |
| 4 | HyperRL-MLP | 4.4824 | 4.6338 | 0.6377 |

## lcbench_numerai28.6

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 47.8039 | 47.5979 | 0.0150 |
| 2 | OurMethod-LC-DQN-MLP | 48.0115 | 47.7924 | 0.2226 |
| 3 | Random Search | 48.0321 | 47.7414 | 0.2432 |
| 4 | HyperRL-MLP | 48.0781 | 47.8188 | 0.2892 |

## lcbench_phoneme

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 20.1172 | 19.0690 | 0.0000 |
| 2 | HyperRL-MLP | 20.4184 | 19.5850 | 0.3013 |
| 3 | OurMethod-LC-DQN-MLP | 20.5690 | 19.9439 | 0.4519 |
| 4 | Random Search | 20.8536 | 19.7420 | 0.7364 |

## lcbench_segment

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.8023 | 10.7612 | 0.8611 |
| 2 | OurMethod-LC-DQN-MLP | 12.8767 | 12.4934 | 2.9354 |
| 3 | Random Search | 12.9159 | 13.0709 | 2.9746 |
| 4 | HyperRL-MLP | 13.2681 | 13.2283 | 3.3268 |

## lcbench_shuttle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.4570 | 0.4472 | 0.0000 |
| 2 | Random Search | 0.8581 | 0.8614 | 0.4012 |
| 3 | OurMethod-LC-DQN-MLP | 0.9018 | 0.8876 | 0.4449 |
| 4 | HyperRL-MLP | 1.0527 | 1.0240 | 0.5958 |

## lcbench_sylvine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 5.2028 | 7.1953 | 0.0176 |
| 2 | HyperRL-MLP | 5.4497 | 7.4675 | 0.2646 |
| 3 | OurMethod-LC-DQN-MLP | 5.5379 | 7.5503 | 0.3527 |
| 4 | Random Search | 6.0670 | 7.9645 | 0.8818 |

## lcbench_vehicle

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 18.6170 | 30.3226 | 0.0000 |
| 2 | Random Search | 21.2766 | 26.8100 | 2.6596 |
| 3 | OurMethod-LC-DQN-MLP | 21.9149 | 24.3011 | 3.2979 |
| 4 | HyperRL-MLP | 22.2340 | 27.5269 | 3.6170 |

## lcbench_volkert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.2367 | 37.2343 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 40.8609 | 40.9749 | 4.6242 |
| 3 | Random Search | 41.2968 | 41.4177 | 5.0601 |
| 4 | HyperRL-MLP | 41.9514 | 41.9914 | 5.7147 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.1457 | 1.46 | 35 |
| 2 | OurMethod-LC-DQN-MLP | 1.2616 | 2.60 | 35 |
| 3 | Random Search | 1.3356 | 2.89 | 35 |
| 4 | HyperRL-MLP | 1.4488 | 3.06 | 35 |

## Rank-1 Counts

| Method | Rank-1 task count |
| --- | ---: |
| Bayesian Optimization | 28 |
| Random Search | 5 |
| HyperRL-MLP | 3 |
| OurMethod-LC-DQN-MLP | 3 |

Most rank-1 finishes: **Bayesian Optimization** with 28 task(s).

Across the selected tasks, **Bayesian Optimization** gives the best average simple regret (0.1457). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.
