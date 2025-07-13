import time
import threading
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API keys from .env
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

# Binance API URL
url = "https://api.binance.com/api/v3/ticker/price"
log_file = "price_log.txt"

# Store last known prices
last_prices = {
    "BTCUSDT": None,
    "ETHUSDT": None
}

def get_price(symbol):
    try:
        response = requests.get(url, params={"symbol": symbol})
        response.raise_for_status()
        return float(response.json()["price"])
    except:
        return None

# Get last N daily closing prices (default 30 days)
def get_last_closes(symbol, limit=30):
    try:
        response = requests.get(
            url="https://api.binance.com/api/v3/klines",
            params={
                "symbol": symbol,
                "interval": "1d",  # daily candles
                "limit": limit     # number of days
            }
        )
        response.raise_for_status()
        data = response.json()
        closes = [float(candle[4]) for candle in data]  # candle[4] = close price
        return closes
    except Exception as e:
        print(f"❌ Error fetching candle data for {symbol}:", e)
        return None



def log_price(symbol, price):
    with open(log_file, "a") as file:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"[{timestamp}] {symbol}: {price:.2f} USD\n")

def update_prices_loop():
    while True:
        btc_price = get_price("BTCUSDT")
        eth_price = get_price("ETHUSDT")

        if btc_price:
            last_prices["BTCUSDT"] = btc_price
            log_price("BTCUSDT", btc_price)
        if eth_price:
            last_prices["ETHUSDT"] = eth_price
            log_price("ETHUSDT", eth_price)

        print(f"🕒 Last update: BTC ${btc_price:,.2f}, ETH ${eth_price:,.2f}")
        time.sleep(180)

def interpret_crypto_question(question):
    question = question.lower()
    mapping = {
        "btc": "BTCUSDT", "bitcoin": "BTCUSDT",
        "eth": "ETHUSDT", "ethereum": "ETHUSDT",
        "bnb": "BNBUSDT", "xrp": "XRPUSDT",
        "doge": "DOGEUSDT", "sol": "SOLUSDT"
    }
    for k in mapping:
        if k in question:
            return mapping[k]
    return None

def ask_openai(prompt, symbol=None):
    price = last_prices.get(symbol) if symbol else None
    context = "You're a helpful crypto assistant. Answer clearly in casual tone."

    # Si pregunta por velas
    if any(word in prompt.lower() for word in ["vela", "velas", "candlestick", "candlesticks", "cerró la vela"]):
        if symbol:
            closes = get_last_3_closes(symbol)
            if closes:
                context += (
                    f"\nThe last 3 daily closing prices for {symbol} are:\n"
                    f"- 3 days ago: ${closes[0]:,.2f}\n"
                    f"- 2 days ago: ${closes[1]:,.2f}\n"
                    f"- Yesterday: ${closes[2]:,.2f}"
                )
            else:
                context += f"\nSorry, I couldn't retrieve candle data for {symbol}."

    elif price and symbol:
        context += f"\nCurrent price of {symbol} is {price:.2f} USD."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()


# Start background thread for updating prices
threading.Thread(target=update_prices_loop, daemon=True).start()

print("💬 Ask about crypto (type 'exit' to quit)\n")

while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        print("👋 Exiting crypto assistant.")
        break

    symbol = interpret_crypto_question(question)
    response = ask_openai(question, symbol)
    print(f"🤖 Jarvis: {response}\n")