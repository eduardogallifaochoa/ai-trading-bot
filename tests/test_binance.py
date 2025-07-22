import sys, os
import requests
import unittest
from dotenv import load_dotenv

# Ensure the root project path is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load environment variables
load_dotenv()

BASE_URL = "https://api.binance.com/api/v3"
HEADERS = {"X-MBX-APIKEY": os.getenv("BINANCE_API_KEY")}


class TestBinanceAPI(unittest.TestCase):
    def test_btc_price(self):
        response = requests.get(f"{BASE_URL}/ticker/price?symbol=BTCUSDT", headers=HEADERS)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        data = response.json()
        assert "price" in data, "Price field not found in response"
        assert float(data["price"]) > 0, "Price must be greater than 0"

    def test_eth_price(self):
        response = requests.get(f"{BASE_URL}/ticker/price?symbol=ETHUSDT", headers=HEADERS)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        data = response.json()
        assert "price" in data, "Price field not found in response"
        assert float(data["price"]) > 0, "Price must be greater than 0"


if __name__ == "__main__":
    unittest.main()
