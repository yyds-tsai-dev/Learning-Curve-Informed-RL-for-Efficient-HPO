# LCBench Official Data Run

- Data: `data/lcbench/data_2k_lw.json`
- Datasets: `credit-g`, `Fashion-MNIST`, `Australian`, `adult`, `bank-marketing`, `MiniBooNE`, `APSFailure`
- Budget: 50 evaluations per method/seed/dataset
- Seeds: 5

```bash
python3 scripts/run_lcbench_baselines.py \
  --data-path data/lcbench/data_2k_lw.json \
  --datasets credit-g,Fashion-MNIST,Australian,adult,bank-marketing,MiniBooNE,APSFailure \
  --budget 50 \
  --seeds 5 \
  --output-dir results/lcbench_budget50
```
