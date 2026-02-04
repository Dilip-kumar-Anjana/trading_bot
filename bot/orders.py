from bot.client import BinanceFuturesClient
from bot.validators import validate_inputs

class OrderService:
    def __init__(self, client: BinanceFuturesClient):
        self.client = client

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float | None = None,
    ):
        validate_inputs(symbol, side, order_type, quantity, price)

        order_payload = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            order_payload["price"] = price
            order_payload["timeInForce"] = "GTC"

        return self.client.create_order(**order_payload)
