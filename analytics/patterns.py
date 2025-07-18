# analytics/patterns.py

import sqlite3
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
import html

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

DB_PATH = "crypto_summaries.db"


def clean_text(text):
    """Clean text by fixing encoding issues and removing broken characters."""
    if not text:
        return ""
    text = html.unescape(text)
    return text.encode("utf-8", "ignore").decode("utf-8", "ignore")


def load_summaries():
    """Load all summaries from the database into a pandas DataFrame."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM summaries ORDER BY timestamp DESC", conn)
    conn.close()
    return df


def analyze_patterns():
    """
    Analyze BTC and ETH price patterns based on summaries.
    Returns a dictionary with insights.
    """
    df = load_summaries()

    # Convert btc_closes and eth_closes to lists of floats
    df['btc_closes'] = df['btc_closes'].apply(lambda x: [float(v) for v in x.split(', ')])
    df['eth_closes'] = df['eth_closes'].apply(lambda x: [float(v) for v in x.split(', ')])

    # Calculate daily % change for BTC
    df['btc_daily_change'] = [
        ((c[-1] - c[-2]) / c[-2]) * 100 if len(c) >= 2 else 0
        for c in df['btc_closes']
    ]

    # Calculate daily % change for ETH
    df['eth_daily_change'] = [
        ((c[-1] - c[-2]) / c[-2]) * 100 if len(c) >= 2 else 0
        for c in df['eth_closes']
    ]

    # Basic insights
    avg_btc_change = df['btc_daily_change'].mean()
    avg_eth_change = df['eth_daily_change'].mean()
    latest_news = clean_text(df.iloc[0]['news']) if not df.empty else "No news available."

    return {
        "avg_btc_change": avg_btc_change,
        "avg_eth_change": avg_eth_change,
        "latest_news": latest_news,
        "raw_data": df[['timestamp', 'btc_price', 'btc_daily_change', 'eth_price', 'eth_daily_change', 'news']].head(5)
    }


def generate_pattern_analysis():
    """
    Generate a human-readable analysis of historical patterns and news trends using GPT.
    """
    patterns = analyze_patterns()
    avg_btc = patterns["avg_btc_change"]
    avg_eth = patterns["avg_eth_change"]
    latest_news = clean_text(patterns["latest_news"])

    # Build a compact summary of the last 5 entries
    df = patterns["raw_data"].copy()
    df = df[['timestamp', 'btc_price', 'btc_daily_change', 'eth_price', 'eth_daily_change']]
    last_entries = df.to_dict(orient='records')

    # Prepare GPT prompt
    news_summary = "\n".join(latest_news.split("\n")[:5])
    entries_summary = "\n".join(
        [f"- {e['timestamp']} | BTC: {e['btc_price']} ({e['btc_daily_change']:.2f}%), "
         f"ETH: {e['eth_price']} ({e['eth_daily_change']:.2f}%)" for e in last_entries]
    )

    prompt = f"""
You are a crypto market analyst.
You have historical data and news.
Analyze them, find trends or patterns, and give a simple recommendation (BUY, HOLD, or SELL).

[Average Daily Changes]
- BTC: {avg_btc:.2f}%
- ETH: {avg_eth:.2f}%

[Last 5 Entries]
{entries_summary}

[Latest News]
{news_summary}

Now write a short analysis in natural language explaining what is happening with BTC and ETH.
End with a final line starting with: ">>> FINAL RECOMMENDATION:" and your recommendation in **bold**.
"""

    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400
    )

    return clean_text(response.choices[0].message.content.strip())
