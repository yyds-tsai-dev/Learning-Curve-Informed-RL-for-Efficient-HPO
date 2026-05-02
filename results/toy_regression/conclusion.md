# Baseline Evaluation Conclusion

Lower validation score and lower simple regret are better. The oracle for simple regret is the best validation score observed by any compared method under the same task and seed.

| Rank | Method | Val score mean | Test score mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | Bayesian Optimization | 0.1754 | 0.2015 | 0.0000 |
| 2 | Random Search | 0.1754 | 0.2015 | 0.0000 |
| 3 | HyperRL-MLP | 0.1762 | 0.2005 | 0.0008 |

**Bayesian Optimization** gives the strongest average validation score (0.1754) for this run. On tiny fixtures or short budgets, treat the result as a smoke test for the protocol rather than decisive evidence. Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, HyperRL-MLP tests the paper-style DQN setup with an MLP encoder, and OurMethod-LC-DQN-MLP adds learning-curve and derivative state features.

The DQN implementation intentionally replaces the original Hyp-RL LSTM encoder with an MLP, as requested. The LCBench adapter can be pointed at the official downloaded JSON file for full-scale evaluation.
