import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()


class BinanceClient:

    def __init__(self):

        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

        self.base_url = "https://testnet.binancefuture.com"


    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": int(time.time() * 1000)
        }


        query_string = "&".join(
            [f"{k}={v}" for k, v in params.items()]
        )


        signature = hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()


        params["signature"] = signature


        headers = {
            "X-MBX-APIKEY": self.api_key
        }


        response = requests.post(
            self.base_url + "/fapi/v1/order",
            params=params,
            headers=headers
        )


        return response.json()