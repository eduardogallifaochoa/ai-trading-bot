# services/report_generator.py

from datetime import datetime
from openai import OpenAI

from services.price_fetcher import get_price, get_last_closes
from services.news_fetcher import get_crypto_news
from database.db_utils import save_report_to_db
from analytics.patterns import analyze_patterns


def extract_final_recommendation(analysis):
    """
    Extracts final recommendation (BUY, HOLD, SELL) from GPT analysis.
    If GPT doesn't provide a clear recommendation, fallback logic is applied.
    """
    text = analysis.lower()

    # Check explicit keywords
    if "buy" in text:
        return "**BUY**"
    elif "sell" in text:
        return "**SELL**"
    elif "hold" in text:
        return "**HOLD**"

    # Fallback logic: detect sentiment/trend
    positive_words = ["increase", "gain", "rise", "positive", "bullish"]
    negative_words = ["drop", "decline", "fall", "negative", "bearish"]

    if any(word in text for word in positive_words):
        return "**BUY**"
    elif any(word in text for word in negative_words):
        return "**SELL**"
    else:
        return "**HOLD**"


def generate_analysis(client, user_prompt=None):
    """
    Generates a crypto analysis using GPT-3.5, merging the old 'report' and 'summary'.
    :param client: OpenAI client instance.
    :param user_prompt: Custom prompt for analysis.
    """
    btc_price = get_price("BTCUSDT")
    eth_price = get_price("ETHUSDT")
    btc_closes = get_last_closes("BTCUSDT", limit=3)
    eth_closes = get_last_closes("ETHUSDT", limit=3)
    news = get_crypto_news(limit=5, currencies="BTC,ETH")

    # Historical Insights
    patterns = analyze_patterns()
    patterns_text = f"""
Historical Insights:
- Average BTC daily change: {patterns['avg_btc_change']:.2f}%
- Average ETH daily change: {patterns['avg_eth_change']:.2f}%
"""

    if user_prompt:
        prompt = f"""
You are a crypto market analyst bot. User request: {user_prompt}

Current prices:
- BTC: ${btc_price:,.2f}
- ETH: ${eth_price:,.2f}

Last 3 daily closes:
BTC: {btc_closes}
ETH: {eth_closes}

Relevant crypto news:
{news}

{patterns_text}

Finally, give your recommendation clearly for each coin (BTC and ETH) with one of these options: BUY, HOLD, or SELL. 
End with: "FINAL RECOMMENDATION: BUY/HOLD/SELL".
"""
    else:
        prompt = f"""
You're a crypto market analyst bot. Summarize the following news headlines briefly.
Then, analyze the current situation of BTC and ETH based on the news, price trends, and historical patterns.
Finally, give your recommendation clearly for each coin (BTC and ETH) with one of these options: BUY, HOLD, or SELL. 
End with: "FINAL RECOMMENDATION: BUY/HOLD/SELL".

Current prices:
- BTC: ${btc_price:,.2f}
- ETH: ${eth_price:,.2f}

Last 3 daily closes:
BTC: {btc_closes}
ETH: {eth_closes}

Relevant crypto news:
{news}

{patterns_text}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700
    )

    analysis = response.choices[0].message.content.strip()
    final_recommendation = extract_final_recommendation(analysis)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\nAnalysis - {now}\n")
    print("Relevant News:\n")
    print(news)
    print("\nHistorical Insights:\n")
    print(patterns_text.strip())
    print("\nGPT Analysis:\n")
    print(analysis)
    print(f"\n>>> FINAL RECOMMENDATION: {final_recommendation}\n")
    print("=" * 60 + "\n")

    # Save to reports table
    save_report_to_db(user_prompt or "Default Analysis", analysis + f"\n\n>>> FINAL RECOMMENDATION: {final_recommendation}")

    return analysis
