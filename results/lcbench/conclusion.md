# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

## lcbench_APSFailure

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 1.6567 | 1.6962 | 0.2249 |
| 2 | Random Search | 1.7377 | 1.8022 | 0.3059 |
| 3 | HyperRL-MLP | 1.7781 | 1.8102 | 0.3463 |
| 4 | OurMethod-LC-DQN-MLP | 1.8043 | 1.8166 | 0.3725 |

## lcbench_Australian

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 9.4118 | 16.2996 | 0.2614 |
| 2 | OurMethod-LC-DQN-MLP | 9.4118 | 16.2115 | 0.2614 |
| 3 | Bayesian Optimization | 9.5425 | 16.5639 | 0.3922 |
| 4 | HyperRL-MLP | 9.8039 | 16.2996 | 0.6536 |

## lcbench_Fashion-MNIST

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 11.9589 | 11.2199 | 0.8696 |
| 2 | HyperRL-MLP | 12.6024 | 11.8407 | 1.5131 |
| 3 | Random Search | 12.7626 | 11.9065 | 1.6733 |
| 4 | OurMethod-LC-DQN-MLP | 13.3131 | 12.3827 | 2.2238 |

## lcbench_MiniBooNE

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 10.8092 | 11.0251 | 0.4235 |
| 2 | OurMethod-LC-DQN-MLP | 11.3127 | 11.5116 | 0.9271 |
| 3 | HyperRL-MLP | 11.9171 | 12.2585 | 1.5315 |
| 4 | Random Search | 12.3379 | 12.6196 | 1.9522 |

## lcbench_adult

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | OurMethod-LC-DQN-MLP | 19.6407 | 19.6836 | 0.2278 |
| 2 | Random Search | 19.7593 | 19.8238 | 0.3463 |
| 3 | HyperRL-MLP | 19.7722 | 19.8163 | 0.3593 |
| 4 | Bayesian Optimization | 20.0130 | 20.0074 | 0.6000 |

## lcbench_bank-marketing

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 12.0156 | 11.6174 | 0.4081 |
| 2 | Bayesian Optimization | 12.4977 | 12.4298 | 0.8903 |
| 3 | HyperRL-MLP | 13.3660 | 13.3829 | 1.7585 |
| 4 | OurMethod-LC-DQN-MLP | 13.5821 | 13.5947 | 1.9746 |

## lcbench_credit-g

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Random Search | 27.1171 | 30.3030 | 0.5405 |
| 2 | OurMethod-LC-DQN-MLP | 27.2973 | 29.6364 | 0.7207 |
| 3 | HyperRL-MLP | 27.4775 | 29.8788 | 0.9009 |
| 4 | Bayesian Optimization | 27.7477 | 29.6364 | 1.1712 |

## Overall

| Rank | Method | Avg simple regret | Avg per-task rank | Tasks |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.6531 | 2.29 | 7 |
| 2 | Random Search | 0.7840 | 2.00 | 7 |
| 3 | OurMethod-LC-DQN-MLP | 0.9583 | 2.71 | 7 |
| 4 | HyperRL-MLP | 1.0090 | 3.00 | 7 |

Across the selected tasks, **Bayesian Optimization** gives the best average simple regret (0.6531). Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.

The DQN implementation intentionally replaces the original Hyp-RL LSTM encoder with an MLP, as requested. The LCBench adapter can be pointed at the official downloaded JSON file for full-scale evaluation.
