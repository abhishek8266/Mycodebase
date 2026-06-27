import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://testnet.binancefuture.com"

params = {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "MARKET",
    "quantity": 0.001,
    "timestamp": int(time.time() * 1000)
}

query_string = "&".join([f"{k}={v}" for k, v in params.items()])

signature = hmac.new(
    API_SECRET.encode(),
    query_string.encode(),
    hashlib.sha256
).hexdigest()

params["signature"] = signature

headers = {
    "X-MBX-APIKEY": API_KEY
}

url = BASE_URL + "/fapi/v1/order"

res = requests.post(url, params=params, headers=headers)

print(res.json())