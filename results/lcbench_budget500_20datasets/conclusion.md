# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.0771 | 1.0726 | 0.0000 |
| 2 | HyperRL-MLP | 1.1378 | 1.1244 | 0.0607 |
| 3 | OurMethod-LC-DQN-MLP | 1.1688 | 1.1635 | 0.0916 |
| 4 | Random Search | 1.1831 | 1.2089 | 0.1059 |

## lcbench_Amazon_employee_access

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 5.9122 | 5.7888 | 0.0055 |
| 2 | Random Search | 5.9150 | 5.7888 | 0.0083 |
| 3 | HyperRL-MLP | 5.9177 | 5.7888 | 0.0110 |
| 4 | Bayesian Optimization | 5.9205 | 5.7888 | 0.0138 |

## lcbench_Australian

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 8.6275 | 16.5639 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 8.8889 | 16.4758 | 0.2614 |
| 3 | Random Search | 8.8889 | 15.8590 | 0.2614 |
| 4 | HyperRL-MLP | 9.0196 | 16.2115 | 0.3922 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.6021 | 9.9481 | 0.0000 |
| 2 | HyperRL-MLP | 10.6461 | 9.9740 | 0.0439 |
| 3 | OurMethod-LC-DQN-MLP | 10.7055 | 9.8511 | 0.1034 |
| 4 | Random Search | 10.9562 | 10.2597 | 0.3541 |

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
| 1 | Bayesian Optimization | 9.6046 | 9.8621 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 9.9475 | 10.0941 | 0.3429 |
| 3 | HyperRL-MLP | 10.1568 | 10.3583 | 0.5522 |
| 4 | Random Search | 10.3168 | 10.5508 | 0.7122 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 17.1093 | 17.2997 | 0.3593 |
| 2 | Bayesian Optimization | 17.4944 | 17.7775 | 0.7444 |
| 3 | HyperRL-MLP | 17.5759 | 17.8309 | 0.8259 |
| 4 | Random Search | 17.7167 | 17.9376 | 0.9667 |

## lcbench_airlines

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 36.5292 | 36.8141 | 0.0000 |
| 2 | HyperRL-MLP | 36.5956 | 36.8168 | 0.0664 |
| 3 | Random Search | 36.6848 | 36.9182 | 0.1556 |
| 4 | OurMethod-LC-DQN-MLP | 36.8621 | 37.0496 | 0.3329 |

## lcbench_albert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.7722 | 33.7485 | 0.0000 |
| 2 | HyperRL-MLP | 33.8310 | 33.7930 | 0.0587 |
| 3 | OurMethod-LC-DQN-MLP | 33.9847 | 33.8234 | 0.2125 |
| 4 | Random Search | 34.0052 | 33.8918 | 0.2329 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 11.2834 | 10.8452 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 11.3554 | 10.9297 | 0.0720 |
| 3 | Random Search | 11.3914 | 10.9552 | 0.1080 |
| 4 | HyperRL-MLP | 11.4114 | 10.9350 | 0.1280 |

## lcbench_blood-transfusion-service-center

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 20.8434 | 18.2927 | 0.0000 |
| 2 | Bayesian Optimization | 20.9639 | 19.3496 | 0.1205 |
| 3 | HyperRL-MLP | 21.0843 | 19.5935 | 0.2410 |
| 4 | OurMethod-LC-DQN-MLP | 21.0843 | 19.0244 | 0.2410 |

## lcbench_car

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 3.1332 | 6.1404 | 0.0000 |
| 2 | HyperRL-MLP | 4.6997 | 7.7895 | 1.5666 |
| 3 | OurMethod-LC-DQN-MLP | 5.2219 | 8.0351 | 2.0888 |
| 4 | Random Search | 5.2219 | 8.2105 | 2.0888 |

## lcbench_christine

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 25.5426 | 27.9642 | 0.0000 |
| 2 | HyperRL-MLP | 25.7763 | 28.0649 | 0.2337 |
| 3 | OurMethod-LC-DQN-MLP | 25.8097 | 27.9195 | 0.2671 |
| 4 | Random Search | 25.8932 | 27.9306 | 0.3506 |

## lcbench_cnae-9

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 2.9289 | 5.7865 | 0.0000 |
| 2 | HyperRL-MLP | 3.0126 | 5.7865 | 0.0837 |
| 3 | OurMethod-LC-DQN-MLP | 3.0126 | 6.1236 | 0.0837 |
| 4 | Random Search | 3.0962 | 5.6180 | 0.1674 |

## lcbench_connect-4

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 25.7933 | 25.5327 | 0.0000 |
| 2 | HyperRL-MLP | 26.2726 | 25.9777 | 0.4793 |
| 3 | OurMethod-LC-DQN-MLP | 26.6261 | 26.2665 | 0.8328 |
| 4 | Random Search | 27.8940 | 27.5414 | 2.1007 |

## lcbench_covertype

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 22.7336 | 22.5375 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 24.5372 | 24.4289 | 1.8036 |
| 3 | HyperRL-MLP | 24.6912 | 24.5772 | 1.9576 |
| 4 | Random Search | 24.7131 | 24.5674 | 1.9796 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 25.2252 | 29.6970 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 25.3153 | 28.5455 | 0.0901 |
| 3 | HyperRL-MLP | 25.4054 | 26.7273 | 0.1802 |
| 4 | Random Search | 25.4955 | 28.3636 | 0.2703 |

## lcbench_dionis

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.0233 | 39.6214 | 0.0057 |
| 2 | HyperRL-MLP | 0.0317 | 59.4128 | 0.0141 |
| 3 | OurMethod-LC-DQN-MLP | 0.0365 | 59.4165 | 0.0189 |
| 4 | Random Search | 0.0585 | 39.6360 | 0.0409 |

## lcbench_fabert

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 33.0807 | 35.0497 | 0.0000 |
| 2 | Random Search | 33.2455 | 35.5940 | 0.1647 |
| 3 | OurMethod-LC-DQN-MLP | 33.3882 | 35.2335 | 0.3075 |
| 4 | HyperRL-MLP | 33.3992 | 35.5278 | 0.3185 |

## lcbench_helena

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.0052 | 19.8713 | 0.0000 |
| 2 | Random Search | 0.0163 | 19.8602 | 0.0111 |
| 3 | OurMethod-LC-DQN-MLP | 0.0288 | 39.6360 | 0.0236 |
| 4 | HyperRL-MLP | 0.0316 | 19.8639 | 0.0264 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.0442 | 1.25 | 20 |
| 2 | HyperRL-MLP | 0.3620 | 2.70 | 20 |
| 3 | OurMethod-LC-DQN-MLP | 0.3769 | 2.65 | 20 |
| 4 | Random Search | 0.5040 | 3.40 | 20 |

Across the selected tasks, **Bayesian Optimization** gives the best average simple regret (0.0442). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.

The DQN implementation intentionally replaces the original Hyp-RL LSTM encoder with an MLP, as requested. The LCBench adapter can be pointed at the official downloaded JSON file for full-scale evaluation.
