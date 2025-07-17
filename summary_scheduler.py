# summary_scheduler.py

import time
from datetime import datetime
import os
from openai import OpenAI
from dotenv import load_dotenv

from news_fetcher import get_crypto_news
from bot import get_last_closes, get_price  # Reuse functions from bot.py
from db_utils import init_db, save_summary_to_db  # DB helper functions

# Load OpenAI API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize the database (only once)
init_db()

# Function to generate and save the summary
def generate_summary():
    try:
        # 1. Get current prices
        btc_price = get_price("BTCUSDT")
        eth_price = get_price("ETHUSDT")

        # 2. Get last 3 daily closes
        btc_closes = get_last_closes("BTCUSDT", limit=3)
        eth_closes = get_last_closes("ETHUSDT", limit=3)

        # 3. Get top crypto news
        news = get_crypto_news(limit=5, currencies="BTC,ETH")

        # 4. Build prompt for OpenAI
        prompt = f"""
You're a crypto market analyst bot. Generate a professional but casual summary of the current situation for BTC and ETH.

Current prices:
- BTC: ${btc_price:,.2f}
- ETH: ${eth_price:,.2f}

Last 3 daily closes:
BTC:
- 3 days ago: ${btc_closes[0]:,.2f}
- 2 days ago: ${btc_closes[1]:,.2f}
- Yesterday: ${btc_closes[2]:,.2f}
ETH:
- 3 days ago: ${eth_closes[0]:,.2f}
- 2 days ago: ${eth_closes[1]:,.2f}
- Yesterday: ${eth_closes[2]:,.2f}

Recent news:
{news}

Please analyze current trends, risks, and possible moves based on this info.
"""

        # 5. Send prompt to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600
        )

        analysis = response.choices[0].message.content.strip()

        # 6. Print the summary
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n🕒 Crypto Summary - {now}\n")
        print(analysis)
        print("\n" + "=" * 60 + "\n")

        # 7. Save all to SQLite database
        save_summary_to_db(
            btc_price, eth_price,
            btc_closes, eth_closes,
            news, analysis
        )

    except Exception as e:
        print(f"❌ Error while generating summary:\n{e}")

# Main loop: runs every 3 hours
if __name__ == "__main__":
    print("🚀 Starting scheduled crypto summaries every 3 hours...\n")
    while True:
        generate_summary()
        time.sleep(3 * 60 * 60)  # 3 hours
