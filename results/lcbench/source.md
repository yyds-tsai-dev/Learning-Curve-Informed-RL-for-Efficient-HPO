# LCBench Official Data Run

Data source: official LCBench lightweight archive from figshare.

- Download URL: https://ndownloader.figshare.com/files/21188598
- Local archive: `data/lcbench/data_2k_lw.zip`
- Local JSON: `data/lcbench/data_2k_lw.json`
- Selected datasets: `credit-g`, `Fashion-MNIST`, `Australian`, `adult`, `bank-marketing`, `MiniBooNE`, `APSFailure`
- Budget: 20 evaluations per method/seed/dataset
- Seeds: 5

Command:

```bash
python3 scripts/run_lcbench_baselines.py \
  --data-path data/lcbench/data_2k_lw.json \
  --datasets credit-g,Fashion-MNIST,Australian,adult,bank-marketing,MiniBooNE,APSFailure \
  --budget 20 \
  --seeds 5 \
  --output-dir results/lcbench
```
