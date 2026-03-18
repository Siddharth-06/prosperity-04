#!/bin/bash
echo "running"

mkdir -p logs

TIMESTAMP=$(date +%s)

LOG_FILE="logs/run_$TIMESTAMP.csv"

echo "Log file: $LOG_FILE"

python3 research/run.py | tee $LOG_FILE

echo "Run complete"