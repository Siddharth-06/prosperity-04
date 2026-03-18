import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from research.backtester import Backtester

bt = Backtester(
    price_file="data/prices_round_0_day_-1.csv",
    params_file="configs/params.json"
)

bt.run()