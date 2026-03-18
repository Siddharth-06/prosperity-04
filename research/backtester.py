import pandas as pd
import json
from strategy.mock_strategy import MockStrategy

class Backtester:

    def __init__(self, price_file, params_file):

        # load data
        self.prices = pd.read_csv(price_file, sep = ';')

        # load params
        with open(params_file) as f:
            self.params = json.load(f)

        # initialize strategy
        self.strategy = MockStrategy(self.params)

        # state
        self.position = {}
        self.pnl = {}
        print(self.prices.columns)
    def run(self):
        print("Rows in dataset:", len(self.prices))
        print("timestamp,product,mid,position,pnl")

        for _, row in self.prices.iterrows():

            product = row["product"]

            if product not in self.position:
                self.position[product] = 0
                self.pnl[product] = 0

            if pd.isna(row["bid_price_1"]) or pd.isna(row["ask_price_1"]):
                continue

            best_bid = row["bid_price_1"]
            best_ask = row["ask_price_1"]

            mid = (best_bid + best_ask) / 2

            pos = self.position[product]

            # call strategy
            buy_price, sell_price = self.strategy.run(
                product,
                best_bid,
                best_ask,
                pos
            )

            # execution logic (simple)
            if buy_price >= best_ask:
                self.position[product] += 1
                self.pnl[product] -= best_ask

            if sell_price <= best_bid:
                self.position[product] -= 1
                self.pnl[product] += best_bid

            print(f"{row['timestamp']},{product},{mid},{self.position[product]},{self.pnl[product]}")