#!/usr/bin/env bash
# LCBench cross-dataset run: training budget = 100 (evaluation budget fixed at 20).
# All 35 datasets, 5 seeds, 150 meta-training episodes.
# Live progress (tqdm + ETA) is teed to the log; result CSVs/PNGs are written to
# OUTDIR when this setting finishes.
set -uo pipefail

BUDGET=100
TOTAL_EPISODES=150
SEEDS=5
DATA=data/lcbench/data_2k_lw.json
OUTDIR=results/lcbench_budget${BUDGET}_all_datasets

cd "$(dirname "$0")/../.."          # -> repo root
mkdir -p logs
LOG=logs/lcbench_budget${BUDGET}_$(date +%Y%m%d_%H%M%S).log

echo "[$(date)] START budget=$BUDGET seeds=$SEEDS episodes=$TOTAL_EPISODES -> $OUTDIR" | tee -a "$LOG"
uv run python -u scripts/run_lcbench_baselines.py \
  --data-path "$DATA" \
  --datasets all \
  --cross-dataset \
  --budget "$BUDGET" \
  --total-episodes "$TOTAL_EPISODES" \
  --seeds "$SEEDS" \
  --output-dir "$OUTDIR" 2>&1 | tee -a "$LOG"
echo "[$(date)] DONE budget=$BUDGET -> $OUTDIR" | tee -a "$LOG"
