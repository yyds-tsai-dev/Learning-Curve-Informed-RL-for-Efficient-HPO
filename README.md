# Learning Curve-Informed RL for Efficient HPO

This repository contains a lightweight HPO evaluation scaffold for the project proposal.

## LCBench Baselines

Python 3.12 is used for this project. Create the local uv environment and install dependencies with:

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
```

LCBench is the primary tabular benchmark interface. Pass the official downloaded LCBench JSON
from figshare, or run the tiny fixture for a smoke test:

```bash
uv run python scripts/run_lcbench_baselines.py --data-path data/tiny_lcbench.json
```

For the full LCBench file, use a larger budget, for example `--budget 20`, and optionally
`--dataset <LCBench dataset name>`.

The current official-data result was generated with:

```bash
uv run python scripts/run_lcbench_baselines.py \
  --data-path data/lcbench/data_2k_lw.json \
  --datasets credit-g,Fashion-MNIST,Australian,adult,bank-marketing,MiniBooNE,APSFailure \
  --budget 20 \
  --seeds 5 \
  --output-dir results/lcbench
```

Implemented methods:

- `Random Search`
- `Bayesian Optimization`
- `HyperRL-DQN`: DQN with replay buffer and target network, matching the Hyp-RL setup with a
  configurable sequence encoder (`lstm` or `mlp`, default `lstm`)
- `OurMethod-LC-DQN`: the same DQN controller with learning-curve and derivative features appended
  to the state

Outputs are written to `results/lcbench/`:

- `summary.csv`
- `pairwise_comparisons.csv`
- `traces.json`
- `conclusion.md`

Budget sweep outputs are also available:

- `results/lcbench_budget50/`
- `results/lcbench_budget100/`
- `results/lcbench_budget_sweep.md`
- `results/lcbench_budget500_20datasets/`

## Toy Regression Baseline

The earlier synthetic regression smoke test is still available:

```bash
uv run python scripts/run_toy_regression.py --budget 20 --seeds 5
```
