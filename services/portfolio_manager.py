# services/portfolio_manager.py
import json
import os
from services.binance_service import get_price

PORTFOLIO_FILE = "portfolio.json"

def _load_portfolio():
    if os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, "r") as f:
            return json.load(f)
    return []

def _save_portfolio(data):
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_trade(symbol, usdt_invested, buy_price):
    """
    Agrega una operación al portafolio.
    - symbol: "ETHUSDT"
    - usdt_invested: cantidad invertida en USDT
    - buy_price: precio de compra en USD/ETH
    """
    portfolio = _load_portfolio()
    portfolio.append({
        "symbol": symbol,
        "usdt_invested": float(usdt_invested),
        "buy_price": float(buy_price)
    })
    _save_portfolio(portfolio)

def get_portfolio():
    return _load_portfolio()

def analyze_portfolio(trade_type="spot"):
    """
    Analiza el portafolio calculando PnL basado en el precio actual.
    Retorna una lista con:
    - symbol
    - usdt_invested
    - buy_price
    - current_price
    - pnl_usdt
    - pnl_percent
    - action
    """
    portfolio = _load_portfolio()
    results = []

    for trade in portfolio:
        symbol = trade["symbol"]
        buy_price = trade["buy_price"]
        usdt_invested = trade["usdt_invested"]

        try:
            current_price = get_price(symbol)
            # Cantidad de crypto comprada con el monto en USDT
            amount_crypto = usdt_invested / buy_price
            pnl_usdt = (current_price - buy_price) * amount_crypto
            pnl_percent = ((current_price - buy_price) / buy_price) * 100

            action = "Hold"
            if trade_type == "futures":
                # En futures, más estrictos: vender si ganancia > 5%, cortar pérdida > 2%
                if pnl_percent > 5:
                    action = "Sell (Take Profit)"
                elif pnl_percent < -2:
                    action = "Cut Loss"
            else:
                # Spot: recomendación más relajada
                if pnl_percent > 10:
                    action = "Consider Partial Sell"
                elif pnl_percent < -15:
                    action = "Hold, wait for recovery"

            results.append({
                "symbol": symbol,
                "usdt_invested": usdt_invested,
                "buy_price": buy_price,
                "current_price": current_price,
                "pnl_usdt": pnl_usdt,
                "pnl_percent": pnl_percent,
                "action": action
            })
        except Exception as e:
            results.append({
                "symbol": symbol,
                "error": str(e)
            })

    return results
