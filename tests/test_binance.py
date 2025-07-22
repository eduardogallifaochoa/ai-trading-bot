import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
import unittest

BASE_URL = "https://api.binance.com/api/v3"

class TestBinanceAPI(unittest.TestCase):
    def test_btc_price(self):
        response = requests.get(f"{BASE_URL}/ticker/price?symbol=BTCUSDT")
        assert response.status_code == 200
        data = response.json()
        assert "price" in data
        assert float(data["price"]) > 0

    def test_eth_price(self):
        response = requests.get(f"{BASE_URL}/ticker/price?symbol=ETHUSDT")
        assert response.status_code == 200
        data = response.json()
        assert "price" in data
        assert float(data["price"]) > 0
