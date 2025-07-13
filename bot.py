from binance.client import Client
from dotenv import load_dotenv
from datetime import datetime
import time
import os

# Load environment variables from .env file
load_dotenv()

# Read Binance API credentials
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# Initialize Binance client
client = Client(api_key, api_secret)

# Function to get the current price of a symbol
def get_price(symbol):
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        return float(ticker["price"])
    except Exception as e:
        print(f"❌ Error getting {symbol}: {e}")
        return None

# Function to log price to a text file with timestamp
def log_price(symbol, price):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("price_log.txt", "a") as f:
        f.write(f"[{now}] {symbol}: ${price:,.2f}\n")

# Main loop
if __name__ == "__main__":
    while True:
        btc_price = get_price("BTCUSDT")
        eth_price = get_price("ETHUSDT")

        if btc_price is not None:
            print(f"💹 BTCUSDT: ${btc_price:,.2f}")
            log_price("BTCUSDT", btc_price)

        if eth_price is not None:
            print(f"💹 ETHUSDT: ${eth_price:,.2f}")
            log_price("ETHUSDT", eth_price)

        # Wait for 3 minutes before next check
        print("⏳ Waiting 3 minutes...\n")
        time.sleep(180)  # 180 seconds = 3 minutes