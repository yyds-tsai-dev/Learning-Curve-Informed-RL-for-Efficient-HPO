# LCBench Official Data Run

- Data source: official LCBench lightweight archive from figshare
- Download URL: https://ndownloader.figshare.com/files/21188598
- Local JSON: `data/lcbench/data_2k_lw.json`
- Datasets: `APSFailure`, `Amazon_employee_access`, `Australian`, `Fashion-MNIST`, `KDDCup09_appetency`, `MiniBooNE`, `adult`, `airlines`, `albert`, `bank-marketing`, `blood-transfusion-service-center`, `car`, `christine`, `cnae-9`, `connect-4`, `covertype`, `credit-g`, `dionis`, `fabert`, `helena`
- Budget: 500 evaluations per method/seed/dataset
- Seeds: 5
- Metric: validation score, computed as `100 - accuracy`; lower is better

Command:

```bash
python3 scripts/run_lcbench_baselines.py \
  --data-path data/lcbench/data_2k_lw.json \
  --datasets APSFailure,Amazon_employee_access,Australian,Fashion-MNIST,KDDCup09_appetency,MiniBooNE,adult,airlines,albert,bank-marketing,blood-transfusion-service-center,car,christine,cnae-9,connect-4,covertype,credit-g,dionis,fabert,helena \
  --budget 500 \
  --seeds 5 \
  --output-dir results/lcbench_budget500_20datasets
```

Overall ranking:

| Rank | Method | Avg simple regret | Avg per-task rank |
| ---: | --- | ---: | ---: |
| 1 | Bayesian Optimization | 0.0442 | 1.25 |
| 2 | HyperRL-MLP | 0.3620 | 2.70 |
| 3 | OurMethod-LC-DQN-MLP | 0.3769 | 2.65 |
| 4 | Random Search | 0.5040 | 3.40 |
