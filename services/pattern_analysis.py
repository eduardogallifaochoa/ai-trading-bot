# services/pattern_analysis.py
import statistics
import json
import os
from services.binance_service import get_candles

def analyze_market(candles, trading_mode="daily", trade_type="spot", buy_price=None):
    """
    Analyze latest candlesticks and return:
    - pattern detected
    - action (Buy / Hold / Sell)
    - suggestion (target price)
    - explanation (simple meaning of the pattern)
    - trade_type-aware advice
    """
    if not candles or len(candles) < 1:
        return {"error": "No candlestick data available."}

    last_candle = candles[-1]
    open_price = float(last_candle[1])
    high = float(last_candle[2])
    low = float(last_candle[3])
    close_price = float(last_candle[4])

    body = abs(close_price - open_price)
    shadow = high - low
    avg_price = statistics.mean([open_price, close_price, high, low])

    # Defaults
    pattern = "Neutral"
    action = "Hold"
    explanation = "No clear pattern detected."
    suggestion = build_suggestion(trading_mode, trade_type, close_price, close_price, "Hold", buy_price)

    # Detect patterns
    if body < shadow * 0.1:
        pattern = "Doji"
        action = "Hold"
        explanation = "Doji = indecision in the market."
        suggestion = build_suggestion(trading_mode, trade_type, close_price, avg_price, "Hold", buy_price, pattern_type="Doji")
    elif close_price > open_price and (close_price - open_price) > (high - low) * 0.6:
        pattern = "Bullish Engulfing"
        action = "Buy"
        explanation = "Bullish Engulfing = buyers taking control."
        target = close_price * 1.02
        suggestion = build_suggestion(trading_mode, trade_type, close_price, target, "Buy", buy_price, pattern_type=pattern)
    elif close_price < open_price and (open_price - close_price) > (high - low) * 0.6:
        pattern = "Bearish Engulfing"
        action = "Sell"
        explanation = "Bearish Engulfing = sellers dominating."
        target = close_price * 0.98
        suggestion = build_suggestion(trading_mode, trade_type, close_price, target, "Sell", buy_price, pattern_type=pattern)
    elif close_price > open_price and (high - close_price) < (body * 0.2):
        pattern = "Hammer"
        action = "Buy"
        explanation = "Hammer = potential reversal."
        target = close_price * 1.03
        suggestion = build_suggestion(trading_mode, trade_type, close_price, target, "Buy", buy_price, pattern_type=pattern)

    return {
        "pattern": pattern,
        "action": action,
        "suggestion": suggestion,
        "explanation": explanation,
        "current_price": close_price
    }

def build_suggestion(trading_mode, trade_type, current_price, target_price, action, buy_price=None, pattern_type=None):
    """
    Builds user-friendly suggestions based on trading mode and trade type.
    """
    # Base time horizon text
    horizon_text = {
        "daily": "short-term view",
        "weekly": "swing (mid-term) view",
        "monthly": "longer-term view"
    }.get(trading_mode, "short-term view")

    # SPOT logic (chill)
    if trade_type == "spot":
        base_msg = f"[SPOT] {horizon_text.capitalize()} ({pattern_type or 'neutral'} pattern): {action} near {current_price:.2f} USD."
        if buy_price:
            if current_price < buy_price:
                base_msg += f" Price is below your entry ({buy_price:.2f} USD). Consider holding to avoid losses."
            else:
                base_msg += f" Price is above your entry ({buy_price:.2f} USD). You could take profits near {target_price:.2f} USD."
        else:
            base_msg += f" Monitor the market and hold unless strong signals show up."
        return base_msg

    # FUTURES logic (strict)
    else:
        return (
            f"[FUTURES] {horizon_text.capitalize()} ({pattern_type or 'neutral'} pattern): {action} near {current_price:.2f} USD. "
            f"Set strict stop-loss near {current_price * 0.98:.2f} USD if long, or {current_price * 1.02:.2f} USD if short. "
            f"Target around {target_price:.2f} USD."
        )

def analyze_all_cryptos(config_path="config.json", trading_mode="daily", trade_type="spot", limit=50):
    """
    Analyze all cryptos defined in config.json (or default list).
    Returns a list of analysis dicts with:
    - symbol
    - pattern
    - action
    - suggestion
    - explanation
    - current_price
    """
    intervals = {
        "daily": "1h",
        "weekly": "4h",
        "monthly": "1d"
    }
    interval = intervals.get(trading_mode, "1h")

    # Load crypto list
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
        symbols = config.get("cryptos", [])
    else:
        symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]

    results = []
    for symbol in symbols:
        try:
            candles = get_candles(symbol, interval=interval, limit=limit)
            analysis = analyze_market(candles, trading_mode=trading_mode, trade_type=trade_type)
            analysis["symbol"] = symbol
            results.append(analysis)
        except Exception as e:
            results.append({
                "symbol": symbol,
                "error": str(e)
            })
    return results
