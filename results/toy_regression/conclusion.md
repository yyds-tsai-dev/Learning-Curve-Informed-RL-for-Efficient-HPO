# Baseline Evaluation Conclusion

Lower RMSE and lower simple regret are better. The oracle for simple regret is the best validation RMSE observed by any compared method under the same task and seed.

| Rank | Method | Val RMSE mean | Test RMSE mean | Simple regret mean |
| --- | --- | ---: | ---: | ---: |
| 1 | HyperRL | 0.1752 | 0.2020 | 0.0001 |
| 2 | Bayesian Optimization | 0.1753 | 0.2014 | 0.0002 |
| 3 | Random Search | 0.1753 | 0.2018 | 0.0002 |

On this toy regression task, **HyperRL** gives the strongest average validation RMSE (0.1752). The gap between methods is small in this deliberately simple task, so the result should be treated as a smoke test for the protocol rather than decisive evidence. Random Search is the sanity-check lower bound, Bayesian Optimization tests sample-efficient surrogate modeling, and HyperRL tests a sequential RL-style policy that can consume learning curve trend features.

This is a lightweight baseline scaffold, not yet a full reproduction of Hyp-RL's LSTM policy. It is intended to make the evaluation protocol concrete before plugging in HPOBench/NAS-Bench-360 or a learned cross-dataset policy.
