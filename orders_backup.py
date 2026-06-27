class OrderManager:

    def __init__(self, client):
        self.client = client


    def create_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        return self.client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )


    def market_buy(self, symbol, quantity):

        return self.create_order(
            symbol,
            "BUY",
            "MARKET",
            quantity
        )


    def market_sell(self, symbol, quantity):

        return self.create_order(
            symbol,
            "SELL",
            "MARKET",
            quantity
        )