# utils/pattern_explainer.py

from textwrap import dedent

def explain_patterns(patterns):
    """
    Generate a human-friendly explanation of BTC & ETH patterns,
    including a recommendation (Buy, Hold, or Sell).
    """

    avg_btc = patterns.get("avg_btc_change", 0)
    avg_eth = patterns.get("avg_eth_change", 0)
    news = patterns.get("latest_news", "No recent news available.")

    # Build the explanation
    explanation = "\n📊 Market Patterns Detected:\n"
    explanation += f"- Average BTC daily change: {avg_btc:.2f}%\n"
    explanation += f"- Average ETH daily change: {avg_eth:.2f}%\n\n"

    # Interpret trends
    if avg_btc > 0.5 and avg_eth > 1:
        recommendation = "The market is showing strong positive momentum. 🚀 Recommendation: **BUY** or HOLD for short-term gains."
    elif avg_btc > 0 and avg_eth > 0:
        recommendation = "Both BTC and ETH show a mild uptrend. Recommendation: **HOLD** and monitor news closely."
    elif avg_btc < -0.5 or avg_eth < -1:
        recommendation = "The market shows signs of correction or decline. ⚠️ Recommendation: **SELL** or wait for better entry points."
    else:
        recommendation = "The market is stable with low volatility. Recommendation: **HOLD** and wait for a clear trend."

    # Include news highlights
    explanation += "📰 Latest Market News Highlights:\n"
    news_lines = [f" - {line.strip()}" for line in news.split("\n") if line.strip()]
    explanation += "\n".join(news_lines[:5]) + "\n\n"
    explanation += f"🤖 AI Insight: {recommendation}"

    return dedent(explanation)
