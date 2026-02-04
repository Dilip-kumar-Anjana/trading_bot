import random
from bot.logging_config import setup_logger

logger = setup_logger()

class MockFuturesClient:
    """
    Mock Binance Futures Client for dry-run testing.
    Simulates API responses for MARKET and LIMIT orders.
    """
    def create_order(self, **kwargs):
        logger.info(f"[DRY-RUN] API Request: {kwargs}")

        # Simulate orderId
        order_id = random.randint(1000000, 9999999)

        # Simulate executed quantity and average price
        executed_qty = kwargs.get("quantity")
        avg_price = kwargs.get("price") or round(random.uniform(30000, 70000), 2)

        # Simulate status
        status = "FILLED" if kwargs["type"] == "MARKET" else "NEW"

        response = {
            "orderId": order_id,
            "symbol": kwargs.get("symbol"),
            "status": status,
            "executedQty": executed_qty,
            "avgPrice": avg_price,
        }

        logger.info(f"[DRY-RUN] API Response: {response}")
        return response
