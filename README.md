# Trading Bot - Binance Futures Testnet

##  Overview
This is a simplified Python trading bot that places Market and Limit orders on Binance Futures Testnet (USDT-M).  
It uses CLI input and supports BUY/SELL orders with proper logging and error handling.

---

##  Features

- Market Order Execution
- Limit Order Execution
- BUY / SELL Support
- CLI-based input (argparse)
- Structured code (client + orders layer)
- Logging of requests, responses, and errors
- Error handling for API and input issues

---

##  Project Structure
trading_bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│
├── logs/
├── cli.py
├── requirements.txt
├── README.md
├── .env



---

##  Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt


#  Create .env file

API_KEY=your_api_key
API_SECRET=your_api_secret

# Run market order 
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001


#Run limit order 
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000



# Logs
logs/trading.log


# Example Output 

Order placed successfully

Order ID: 123456
Status: NEW
Executed Qty: 0.001
Avg Price: 50000


# Author

Python Developer Trading Bot Assignment

# logging_config.py (PRO LEVEL)

```python id="log1"
import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/trading.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger(name):
    logger = logging.getLogger(name)
    return logger




## Disclaimer
This bot works only on Binance Futures Testnet and is for educational purposes only. Not financial advice.s