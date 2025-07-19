# services/binance_service.py
import requests

BASE_URL = "https://api.binance.com/api/v3"

def get_candles(symbol="BTCUSDT", interval="1h", limit=50):
    """
    Fetch candlestick (kline) data from Binance API.
    Returns: List of candles [ [open_time, open, high, low, close, volume, ...], ... ]
    """
    url = f"{BASE_URL}/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error fetching candles for {symbol}: {e}")

def get_price(symbol="BTCUSDT"):
    """
    Fetch the current price for a symbol.
    Returns: float (price)
    """
    url = f"{BASE_URL}/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data["price"])
    except requests.RequestException as e:
        raise Exception(f"Error fetching price for {symbol}: {e}")

def get_popular_prices(symbols=None):
    """
    Fetch prices for a list of popular symbols.
    Default: BTC, ETH, BNB, SOL, XRP.
    Returns: dict {symbol: price}
    """
    if symbols is None:
        symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]
    
    prices = {}
    for symbol in symbols:
        try:
            prices[symbol] = get_price(symbol)
        except Exception as e:
            prices[symbol] = f"Error: {e}"
    return prices
