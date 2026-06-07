#!/usr/bin/env bash
# Run the full training-budget sweep {20,50,100,150} sequentially.
# Each setting writes its own result dir + log as soon as it finishes, so you can
# inspect partial results while later settings are still running. A failure in one
# setting does not stop the rest.
set -uo pipefail
cd "$(dirname "$0")"

for B in 20 50 100 150; do
  echo "================ training budget $B ================"
  bash "run_b${B}.sh" || echo "!! budget $B failed, continuing with the next setting"
done
echo "================ sweep finished ================"
