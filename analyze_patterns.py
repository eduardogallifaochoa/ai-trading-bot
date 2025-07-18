# analyze_patterns.py

from analytics.patterns import analyze_patterns

print("🔍 Analyzing patterns from crypto_summaries.db...\n")
insights = analyze_patterns()

print(f"📈 Average BTC daily change: {insights['avg_btc_change']:.2f}%")
print(f"📈 Average ETH daily change: {insights['avg_eth_change']:.2f}%\n")

print("📰 Latest News in DB:")
print(insights['latest_news'], "\n")

print("📊 Last 5 entries overview:")
print(insights['raw_data'].to_string(index=False))
