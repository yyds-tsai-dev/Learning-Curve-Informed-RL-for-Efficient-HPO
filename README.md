# Learning Curve-Informed RL for Efficient HPO

This repository contains a lightweight HPO evaluation scaffold for the project proposal.

## LCBench Baselines

LCBench is the primary tabular benchmark interface. Pass the official downloaded LCBench JSON
from figshare, or run the tiny fixture for a smoke test:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_lcbench_baselines.py --data-path data/tiny_lcbench.json
```

For the full LCBench file, use a larger budget, for example `--budget 20`, and optionally
`--dataset <LCBench dataset name>`.

The current official-data result was generated with:

```bash
python3 scripts/run_lcbench_baselines.py \
  --data-path data/lcbench/data_2k_lw.json \
  --datasets credit-g,Fashion-MNIST,Australian,adult,bank-marketing,MiniBooNE,APSFailure \
  --budget 20 \
  --seeds 5 \
  --output-dir results/lcbench
```

Implemented methods:

- `Random Search`
- `Bayesian Optimization`
- `HyperRL-MLP`: DQN with replay buffer and target network, matching the Hyp-RL setup but replacing
  the LSTM encoder with a padded-history MLP
- `OurMethod-LC-DQN-MLP`: the same DQN-MLP controller with learning-curve and derivative features
  appended to the state

Outputs are written to `results/lcbench/`:

- `summary.csv`
- `pairwise_comparisons.csv`
- `traces.json`
- `conclusion.md`

Budget sweep outputs are also available:

- `results/lcbench_budget50/`
- `results/lcbench_budget100/`
- `results/lcbench_budget_sweep.md`

## Toy Regression Baseline

The earlier synthetic regression smoke test is still available:

```bash
python3 scripts/run_toy_regression.py --budget 20 --seeds 5
```
