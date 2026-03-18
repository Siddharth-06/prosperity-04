class MockStrategy:

    def __init__(self, params):
        self.spread = params["spread"]
        self.inventory_penalty = params["inventory_penalty"]

    def run(self, product, best_bid, best_ask, position):

        mid = (best_bid + best_ask) / 2

        fair_price = mid - self.inventory_penalty * position

        buy_price = fair_price - self.spread
        sell_price = fair_price + self.spread

        return buy_price, sell_price