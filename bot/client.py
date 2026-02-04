from binance.client import Client
from bot.logging_config import setup_logger
import os

logger = setup_logger()

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def create_order(self, **kwargs):
        try:
            logger.info(f"API Request: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"API Response: {response}")
            return response
        except Exception as e:
            logger.exception("Binance API Error")
            raise
