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

## CLI Usage

Run the bot using python cli.py with the following arguments:
```SQL
--symbol SYMBOL             : Trading pair, e.g., BTCUSDT
--side {BUY,SELL}           : Order side
--order-type {MARKET,LIMIT} : Order type
--quantity QUANTITY         : Order quantity
--price PRICE               : Required for LIMIT orders
--dry-run                   : Optional, simulate order without real API
```
---

MARKET Order Example
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```
---

LIMIT Order Example
```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 50000
```
---

## 🧪 Dry-Run Testing (Safe Simulation)

Dry-run mode simulates order execution without hitting Binance Testnet or using real funds.

MARKET Order Dry-Run Example

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001 --dry-run
```

Sample Output:
```text
✅ Order Placed Successfully
Order ID     : 4147744
Status       : FILLED
Executed Qty : 0.001
Avg Price    : 47829.15
```
LIMIT Order Dry-Run Example

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 50000 --dry-run
```
Sample Output:
```text
✅ Order Placed Successfully
Order ID     : 7351140
Status       : NEW
Executed Qty : 0.001
Avg Price    : 50000
```

---

## Logs

All API activity (requests, responses, errors) is stored in:

```yaml
logs/trading_bot.log
```

Sample Log Entries:
```text
2026-02-04 21:40:43,991 | INFO | trading_bot | [DRY-RUN] API Request: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}
2026-02-04 21:40:43,993 | INFO | trading_bot | [DRY-RUN] API Response: {'orderId': 4147744, 'symbol': 'BTCUSDT', 'status': 'FILLED', 'executedQty': 0.001, 'avgPrice': 47829.15}
2026-02-04 21:40:44,732 | INFO | trading_bot | [DRY-RUN] API Request: {'symbol': 'BTCUSDT', 'side': 'SELL', 'type': 'LIMIT', 'quantity': 0.001, 'price': 50000.0, 'timeInForce': 'GTC'}
2026-02-04 21:40:44,733 | INFO | trading_bot | [DRY-RUN] API Response: {'orderId': 7351140, 'symbol': 'BTCUSDT', 'status': 'NEW', 'executedQty': 0.001, 'avgPrice': 50000.0}
```
Logs are automatically created the first time you run the bot.

---

## Assumptions

- Only USDT-M Futures are supported

- Binance Testnet is used by default for safety

- LIMIT orders require --price argument

- Dry-run mode allows safe testing without funds or API keys

- Logging is structured for easy review and submission


