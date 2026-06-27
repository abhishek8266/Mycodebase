# Trading Bot - Binance Futures Testnet

## Overview

A Python based CLI trading bot for Binance Futures Testnet (USDT-M).

The bot supports Market and Limit order execution with validation, logging and error handling.

---

## Features

- Market Order Execution
- Limit Order Execution
- BUY / SELL Support
- Command Line Interface (CLI)
- Input Validation
- API Error Handling
- Request/Response Logging

---

## Project Structure

trading_bot/




---

## Installation

Clone repository:

```bash
git clone https://github.com/abhishek8266/Trading_bot.git

Run Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Run Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
