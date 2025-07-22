import requests

BASE_URL = "https://api.binance.com/api/v3"

def test_btc_price():
    response = requests.get(f"{BASE_URL}/ticker/price?symbol=BTCUSDT")
    assert response.status_code == 200
    data = response.json()
    assert "price" in data
    assert float(data["price"]) > 0

def test_eth_price():
    response = requests.get(f"{BASE_URL}/ticker/price?symbol=ETHUSDT")
    assert response.status_code == 200
    data = response.json()
    assert "price" in data
    assert float(data["price"]) > 0
