# generate_now.py

import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

from services.news_fetcher import get_crypto_news
from services.price_fetcher import get_price, get_last_closes, get_historical_closes
from database.db_utils import init_db, save_summary_to_db

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize DB once
init_db()

def generate_summary():
    try:
        print("\n🟢 Manual summary generation started...\n")

        # 1. Current prices
        btc_price = get_price("BTCUSDT")
        eth_price = get_price("ETHUSDT")

        # 2. Last 3 daily closes
        btc_closes = get_last_closes("BTCUSDT", limit=3)
        eth_closes = get_last_closes("ETHUSDT", limit=3)

        # 3. Last 30 daily closes (historical trend)
        btc_history = get_historical_closes("BTCUSDT", days=30)
        eth_history = get_historical_closes("ETHUSDT", days=30)

        # 4. News from last 30 days
        news = get_crypto_news(limit=10, currencies="BTC,ETH")

        # 5. Build GPT prompt
        prompt = f"""
You're a crypto market analyst bot. Generate a summary of the current state of BTC and ETH based on prices, trends and recent news. Provide recommendations: buy/sell/hold.

Current prices:
- BTC: ${btc_price:,.2f}
- ETH: ${eth_price:,.2f}

Last 3 daily closes:
BTC: {btc_closes}
ETH: {eth_closes}

30-day trend (daily closes):
BTC: {btc_history}
ETH: {eth_history}

Recent news:
{news}

Give your reasoning and final recommendation for each coin.
"""

        # 6. GPT call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )
        analysis = response.choices[0].message.content.strip()

        # 7. Show result
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n🕒 Crypto Summary - {now}\n")
        print(analysis)

        print("\n📰 Relevant News (last 30 days):\n")
        print(news)

        print("\n" + "=" * 60 + "\n")

        # 8. Save in DB
        save_summary_to_db(
            btc_price, eth_price,
            btc_closes, eth_closes,
            news, analysis
        )

    except Exception as e:
        print(f"❌ Error while generating summary:\n{e}")

if __name__ == "__main__":
    generate_summary()
