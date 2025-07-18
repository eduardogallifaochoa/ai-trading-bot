import requests

# Binance API URL for price and candlestick data
BASE_URL = "https://api.binance.com/api/v3"

# Fetch current price of a given crypto symbol
def get_price(symbol):
    try:
        response = requests.get(f"{BASE_URL}/ticker/price", params={"symbol": symbol})
        response.raise_for_status()
        return float(response.json()["price"])
    except Exception as e:
        print(f"❌ Error fetching price for {symbol}: {e}")
        return None

# Fetch the last N daily closing prices (candles) for a crypto symbol
def get_last_closes(symbol, limit=3):
    try:
        response = requests.get(
            f"{BASE_URL}/klines",
            params={
                "symbol": symbol,
                "interval": "1d",  # Daily candles
                "limit": limit
            }
        )
        response.raise_for_status()
        data = response.json()
        closes = [float(candle[4]) for candle in data]  # Close price is at index 4
        return closes
    except Exception as e:
        print(f"❌ Error fetching candlestick data for {symbol}: {e}")
        return []

def get_last_30_candles(symbol="BTCUSDT", interval="1d"):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit=30"
    response = requests.get(url)
    data = response.json()

    closes = [float(entry[4]) for entry in data]  # closing prices
    return closes

import requests

def get_historical_closes(symbol, interval="1d", limit=30):
    """
    Fetches the last N daily close prices for the given symbol using Binance API.
    """
    url = f"https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Each entry = [open time, open, high, low, close, volume, ...]
        closes = [float(entry[4]) for entry in data]
        return closes

    except Exception as e:
        print(f"⚠️ Error fetching historical closes for {symbol}: {e}")
        return []
