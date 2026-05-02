# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.3425 | 1.3589 | 0.0952 |
| 2 | HyperRL-MLP | 1.3628 | 1.3740 | 0.1154 |
| 3 | Random Search | 1.4699 | 1.5152 | 0.2226 |
| 4 | OurMethod-LC-DQN-MLP | 1.5794 | 1.6372 | 0.3321 |

## lcbench_Australian

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 9.1503 | 16.2115 | 0.1307 |
| 2 | Bayesian Optimization | 9.2810 | 16.0352 | 0.2614 |
| 3 | HyperRL-MLP | 9.4118 | 16.2996 | 0.3922 |
| 4 | OurMethod-LC-DQN-MLP | 9.4118 | 16.3877 | 0.3922 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.6435 | 9.9887 | 0.0000 |
| 2 | Random Search | 11.2922 | 10.4918 | 0.6487 |
| 3 | HyperRL-MLP | 11.4666 | 10.7576 | 0.8231 |
| 4 | OurMethod-LC-DQN-MLP | 11.9899 | 11.1991 | 1.3464 |

## lcbench_MiniBooNE

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 9.6505 | 9.8360 | 0.0000 |
| 2 | Random Search | 10.7104 | 10.9301 | 1.0599 |
| 3 | OurMethod-LC-DQN-MLP | 11.1423 | 11.3970 | 1.4918 |
| 4 | HyperRL-MLP | 11.7015 | 11.9752 | 2.0510 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 18.4889 | 18.6462 | 0.0667 |
| 2 | Bayesian Optimization | 19.3148 | 19.4528 | 0.8926 |
| 3 | HyperRL-MLP | 19.4426 | 19.5620 | 1.0204 |
| 4 | Random Search | 19.4963 | 19.5284 | 1.0741 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 11.5655 | 11.1871 | 0.1220 |
| 2 | Random Search | 11.6495 | 11.3600 | 0.2061 |
| 3 | OurMethod-LC-DQN-MLP | 11.6955 | 11.4136 | 0.2521 |
| 4 | HyperRL-MLP | 11.7375 | 11.3895 | 0.2941 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.1261 | 30.4242 | 0.0000 |
| 2 | Random Search | 26.8468 | 29.6364 | 0.7207 |
| 3 | OurMethod-LC-DQN-MLP | 26.9369 | 28.5455 | 0.8108 |
| 4 | HyperRL-MLP | 27.4775 | 29.4545 | 1.3514 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.1959 | 1.29 | 7 |
| 2 | Random Search | 0.5804 | 2.29 | 7 |
| 3 | OurMethod-LC-DQN-MLP | 0.6703 | 3.14 | 7 |
| 4 | HyperRL-MLP | 0.8639 | 3.29 | 7 |

Across the selected tasks, **Bayesian Optimization** gives the best average simple regret (0.1959). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.

The DQN implementation intentionally replaces the original Hyp-RL LSTM encoder with an MLP, as requested. The LCBench adapter can be pointed at the official downloaded JSON file for full-scale evaluation.
