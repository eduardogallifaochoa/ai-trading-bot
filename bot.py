# bot.py

from services.price_fetcher import get_price, get_last_closes
from services.news_fetcher import get_crypto_news
from services.gpt_analyzer import generate_analysis as ask_openai

from utils.formatters import print_suggestions
from database.db_utils import init_db
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Quick-access questions
suggestions = {
    "1": "What's the market summary for BTC?",
    "2": "Give me an ETH trend analysis based on recent news and prices.",
    "3": "What’s going on with Bitcoin this week?",
    "4": "Tell me the recent news for Ethereum.",
    "5": "Show me the last 3 daily closes for BTC.",
    "6": "What do you do and how does this work?"
}

# Detect coin from user input
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

def main():
    init_db()
    print("💬 Ask me anything about crypto (type 'exit' to quit)\n")
    print_suggestions(suggestions)

    while True:
        question = input("You: ").strip()
        if question.lower() in ["exit", "quit"]:
            print("👋 Exiting crypto assistant.")
            break

        if question in suggestions:
            question = suggestions[question]

        if question.lower() in [
            "what do you do", "how do you work",
            "what do you do and how does this work?",
            "what can you do", "how does this bot work"
        ]:
            print("🤖 Jarvis: I was programmed by Eduardo Gallifa 🧠🔥")
            print("- Real-time prices from Binance 📊")
            print("- Last 3 daily closes (candles) 🕯️")
            print("- Breaking crypto news 📰")
            print("- Smart GPT analysis 🤖💬\n")
            continue

        # Check if user just wants news
        if "news" in question.lower():
            symbol = interpret_crypto_question(question)
            if symbol:
                news = get_crypto_news(currencies=symbol.replace("USDT", ""))
                print(f"📰 Latest {symbol.replace('USDT','')} news:\n{news}\n")
            else:
                print("📰 Sorry, please mention BTC or ETH to fetch news.\n")
            continue

        # Full analysis for BTC or ETH
        symbol = interpret_crypto_question(question)
        if symbol in ["BTCUSDT", "ETHUSDT"]:
            btc_price = get_price("BTCUSDT")
            eth_price = get_price("ETHUSDT")
            btc_closes = get_last_closes("BTCUSDT", limit=3)
            eth_closes = get_last_closes("ETHUSDT", limit=3)
            news = get_crypto_news(currencies=symbol.replace("USDT", ""))

            response = ask_openai(
                btc_price=btc_price,
                eth_price=eth_price,
                btc_closes=btc_closes,
                eth_closes=eth_closes,
                news_text=news
            )
        else:
            response = f"🤖 Jarvis: Sorry, I can only analyze BTC or ETH for now."

        print(f"🤖 Jarvis: {response}\n")
        
if __name__ == "__main__":
    main()
