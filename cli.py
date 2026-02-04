import argparse
import os
from bot.orders import OrderService
from bot.logging_config import setup_logger

# Import real and mock clients
from bot.client import BinanceFuturesClient
from bot.mock_client import MockFuturesClient

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--order-type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--dry-run", action="store_true", help="Run without hitting Binance API")

    args = parser.parse_args()

    try:
        # Use mock client if dry-run
        if args.dry_run:
            client = MockFuturesClient()
        else:
            client = BinanceFuturesClient(
                api_key=os.getenv("BINANCE_API_KEY"),
                api_secret=os.getenv("BINANCE_API_SECRET"),
            )

        service = OrderService(client)

        print("\n📤 Order Request")
        print(vars(args))

        response = service.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\n✅ Order Placed Successfully")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        logger.error(f"Order failed: {e}")
        print("\n❌ Order Failed")
        print(str(e))


if __name__ == "__main__":
    main()
