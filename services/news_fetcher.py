# news_fetcher.py
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("CRYPTOPANIC_API_KEY")
BASE_URL = "https://cryptopanic.com/api/v1/posts/"

def get_crypto_news(limit=5, currencies="BTC,ETH"):
    params = {
        "auth_token": API_KEY,
        "currencies": currencies,
        "public": "true",
        "kind": "news",
        "regions": "en"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        news_items = data.get("results", [])[:limit]

        if not news_items:
            return "⚠️ No news found."

        formatted_news = []
        for item in news_items:
            title = item.get("title", "No title")
            url = item.get("url", "")
            published_at = item.get("published_at", "")

            # Try to format the timestamp safely
            try:
                time_fmt = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%S%z").strftime("%d %b %Y %H:%M")
            except:
                time_fmt = "unknown time"

            formatted_news.append(f"- {title} ({time_fmt})\n  {url}")

        return "\n".join(formatted_news)

    except Exception as e:
        return f"⚠️ Error fetching news: {e}"