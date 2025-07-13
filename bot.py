import time
import requests
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

# URL to fetch crypto prices
url = "https://api.binance.com/api/v3/ticker/price"

# Log file to save prices
log_file = "price_log.txt"

def get_price(symbol):
    try:
        response = requests.get(url, params={"symbol": symbol})
        response.raise_for_status()
        return float(response.json()["price"])
    except Exception as e:
        print(f"❌ Error fetching {symbol} price:", e)
        return None

def log_price(symbol, price):
    with open(log_file, "a") as file:
        file.write(f"{symbol}: {price:.2f} USD\n")

print("✅ Bot started. Press Ctrl+C to stop.\n")

try:
    while True:
        btc_price = get_price("BTCUSDT")
        eth_price = get_price("ETHUSDT")

        if btc_price is not None:
            print(f"🟩 BTCUSDT: ${btc_price:,.2f}")
            log_price("BTCUSDT", btc_price)

        if eth_price is not None:
            print(f"🟩 ETHUSDT: ${eth_price:,.2f}")
            log_price("ETHUSDT", eth_price)

        print("⏳ Waiting 3 minutes...\n")
        time.sleep(180)

except KeyboardInterrupt:
    print("🛑 Bot stopped by user (Ctrl+C). Goodbye!\n")
