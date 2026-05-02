# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.1473 | 1.1324 | 0.0190 |
| 2 | OurMethod-LC-DQN-MLP | 1.2580 | 1.2998 | 0.1297 |
| 3 | HyperRL-MLP | 1.3378 | 1.3796 | 0.2095 |
| 4 | Random Search | 1.3413 | 1.3860 | 0.2130 |

## lcbench_Australian

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 9.0196 | 15.6828 | 0.1307 |
| 2 | Random Search | 9.0196 | 15.9471 | 0.1307 |
| 3 | HyperRL-MLP | 9.1503 | 16.2996 | 0.2614 |
| 4 | OurMethod-LC-DQN-MLP | 9.1503 | 16.2115 | 0.2614 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.6021 | 9.9481 | 0.0000 |
| 2 | OurMethod-LC-DQN-MLP | 11.0945 | 10.3316 | 0.4923 |
| 3 | HyperRL-MLP | 11.2301 | 10.4381 | 0.6280 |
| 4 | Random Search | 11.2922 | 10.4918 | 0.6900 |

## lcbench_MiniBooNE

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 9.6505 | 9.8360 | 0.0000 |
| 2 | HyperRL-MLP | 10.4774 | 10.6957 | 0.8269 |
| 3 | Random Search | 10.7104 | 10.9301 | 1.0599 |
| 4 | OurMethod-LC-DQN-MLP | 11.0950 | 11.3089 | 1.4445 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL-MLP | 18.0093 | 18.2912 | 0.3815 |
| 2 | OurMethod-LC-DQN-MLP | 18.4204 | 18.7975 | 0.7926 |
| 3 | Bayesian Optimization | 19.1907 | 19.2530 | 1.5630 |
| 4 | Random Search | 19.4352 | 19.4577 | 1.8074 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 11.5055 | 11.1348 | 0.1620 |
| 2 | Random Search | 11.5415 | 11.2032 | 0.1981 |
| 3 | OurMethod-LC-DQN-MLP | 11.5475 | 11.1361 | 0.2041 |
| 4 | HyperRL-MLP | 11.6435 | 11.1388 | 0.3001 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 26.0360 | 29.7576 | 0.3604 |
| 2 | OurMethod-LC-DQN-MLP | 26.3964 | 29.2727 | 0.7207 |
| 3 | Random Search | 26.6667 | 29.4545 | 0.9910 |
| 4 | HyperRL-MLP | 26.8468 | 31.2121 | 1.1712 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.3193 | 1.29 | 7 |
| 2 | HyperRL-MLP | 0.5398 | 2.86 | 7 |
| 3 | OurMethod-LC-DQN-MLP | 0.5779 | 2.71 | 7 |
| 4 | Random Search | 0.7272 | 3.14 | 7 |

Across the selected tasks, **Bayesian Optimization** gives the best average simple regret (0.3193). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.

The DQN implementation intentionally replaces the original Hyp-RL LSTM encoder with an MLP, as requested. The LCBench adapter can be pointed at the official downloaded JSON file for full-scale evaluation.
