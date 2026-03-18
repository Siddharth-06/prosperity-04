#!/bin/bash
set -e

echo "Starting parameter sweep..."

for spread in 1 2 3
do
  for penalty in 0.05 0.1 0.2
  do
    echo "------------------------"
    echo "spread=$spread penalty=$penalty"
    python - <<EOF
import json

params = {
    "spread": $spread,
    "inventory_penalty": $penalty
}

with open("configs/params.json", "w") as f:
    json.dump(params, f, indent=2)
EOF

    ./scripts/run.sh

  done
done

echo "Sweep complete"