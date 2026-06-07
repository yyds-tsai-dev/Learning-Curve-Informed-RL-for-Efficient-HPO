#!/usr/bin/env bash
# Launch the full sweep inside a detached tmux session, wrapped in `caffeinate -i`
# so the Mac will not idle-sleep while it runs. You can detach and close the
# terminal; the run keeps going.
#
#   ./start_tmux.sh            # start the sweep in the background
#   tmux attach -t lcbench     # watch it live
#   (inside tmux) Ctrl-b d     # detach again, leaving it running
#   tail -f ../../logs/lcbench_budget*.log   # or follow the logs from anywhere
#
# NOTE: `caffeinate -i` prevents idle sleep with the display off, but closing the
# laptop lid still sleeps the Mac unless it is on AC power with clamshell mode
# (external display/keyboard) or an app like Amphetamine. Keep the lid open, or
# stay plugged in, if you want it to survive overnight.
set -euo pipefail
SESSION=lcbench
cd "$(dirname "$0")"

if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "tmux session '$SESSION' already exists. Attach with: tmux attach -t $SESSION"
  exit 1
fi

tmux new-session -d -s "$SESSION" "caffeinate -i bash run_all.sh; echo; echo '[sweep done — press any key to close]'; read -n 1"
echo "Started sweep in tmux session '$SESSION'."
echo "  watch live:  tmux attach -t $SESSION   (detach: Ctrl-b then d)"
echo "  follow logs: tail -f $(cd ../.. && pwd)/logs/lcbench_budget*.log"
