# Binance Futures Testnet Trading Bot

A clean, production-ready Python CLI trading bot for **Binance Futures Testnet (USDT-M)**.  
Supports MARKET and LIMIT orders, BUY and SELL, with structured logging, input validation, and dry-run testing.

---

## Features

- Execute MARKET and LIMIT orders  
- BUY and SELL support  
- CLI-based interface  
- Input validation for all parameters  
- Structured logging of API requests, responses, and errors  
- Dry-run mode for safe simulation without real funds  
- Modular architecture for maintainability  

---

## Setup

1. Clone the repository:

```bash
git clone <repo-url>
cd trading_bot
```

2. Create and activate a Python virtual environment:

Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3.Install dependencies:

```bash
pip install -r requirements.txt
```

4.(Optional for real Testnet use) Set Binance API keys as environment variables:

Windows (PowerShell):
```
setx BINANCE_API_KEY "your_api_key"
setx BINANCE_API_SECRET "your_api_secret"
```

macOS / Linux:
```
export BINANCE_API_KEY="your_api_key"
export BINANCE_API_SECRET="your_api_secret"
```
Dry-run mode does not require API keys.

---

CLI Usage

Run the bot using python cli.py with the following arguments:
```SQL
--symbol SYMBOL             : Trading pair, e.g., BTCUSDT
--side {BUY,SELL}           : Order side
--order-type {MARKET,LIMIT} : Order type
--quantity QUANTITY         : Order quantity
--price PRICE               : Required for LIMIT orders
--dry-run                   : Optional, simulate order without real API
```

MARKET Order Example
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```
LIMIT Order Example
```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 50000
```
🧪 Dry-Run Testing (Safe Simulation)

Dry-run mode simulates order execution without hitting Binance Testnet or using real funds.

MARKET Order Dry-Run Example


