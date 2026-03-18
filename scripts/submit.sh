
set -e

echo "=============================="
echo "Preparing submission"
echo "=============================="
mkdir -p submissions
rm -f submission.py

TIMESTAMP=$(date +%s)
cp strategy/trader.py submissions/submission_$TIMESTAMP.py
cp strategy/mock_strategy.py submission.py
echo "Created submission.py"
echo "Opening directory..."
open .

echo "Upload submission.py on IMC portal"