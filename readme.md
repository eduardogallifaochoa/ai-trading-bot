# **AI Trading Bot - Pro GUI**

Hey there, I’m **Eduardo Gallifa** — a Manual QA Engineer transitioning into automation (because, let’s be real: better pay, smarter work). I’m also an Industrial Engineer with a second degree in Psychology. Been into crypto since 2018. I’ve seen BTC at 20k, and now over 100k. Wild ride.

This repo started as my **personal playground** to experiment with automation, APIs, AI, and connecting smart tools. I see APIs as engines that talk via JSON — and I love building the gearbox.

The **OpenAI API** acts like the brain, **Binance provides real-time crypto prices**, and **CryptoPanic adds global news context**. Together?  
**An AI-powered crypto assistant with market awareness.** 😎

---

## **💬 Features**

### **AI & Market Analysis**
- **OpenAI GPT-4o** for natural-language crypto insights.  
- **Daily, weekly, monthly outlooks** for **BTC, ETH, BNB, SOL, XRP**.  
- **BUY / HOLD / SELL** calls with **TP/SL** hints (for spot trades).  
- **PnL calculations** when buy price is provided.

### **Market Data & News**
- **Live price feeds** (Binance API).  
- **Last 3 daily closes** for each coin.  
- **CryptoPanic news** merged with price analysis.

### **Pattern Recognition**
- Detects **bullish/bearish patterns** and merges results with AI insights.

### **GUI Application (Tkinter)**
- **Dashboard** with real-time prices & recommendations.  
- **Chat Section** for AI queries.  
- **Control Panel** with dropdowns (`daily/weekly/monthly`, `spot/futures`) — locked to prevent accidental edits.  
- **Action Buttons**: Generate Report, Analyze Patterns, Show History, etc.

### **Reports & Database**
- AI-generated reports stored in **SQLite (`crypto_summaries.db`)**.  
- Summaries combining price data, news, and historical patterns.

---

## 📦 **Project Structure**

```plaintext
ai-trading-bot/
├── bot.py                   ← Classic bot (CLI)
├── gui_launcher.py          ← GUI launcher
├── generate_report.py       ← Report generator
├── services/                ← APIs & AI logic
├── analytics/               ← Pattern detection
├── database/                ← SQLite database helpers
├── utils/                   ← Tools (cleanup)
├── crypto_summaries.db      ← Saved AI reports
├── price_log.txt            ← Price logs (3-min intervals)
├── requirements.txt         ← Packages
├── .env                     ← API keys
└── dist/                    ← Windows executable
```

## ⚙️ How to Use
Option 1: GUI
```plaintext
python gui_launcher.py
```
Use buttons like Generate Report or Analyze Patterns.

Option 2: CLI
```plaintext
# Generate a custom report
python generate_report.py "Analyze BTC market for the weekend"

# Show historical reports
python generate_report.py --history

# Analyze price patterns
python generate_report.py --patterns
```

Option 3: Classic Bot
```plaintext
python bot.py
```
Ask:
“What’s up with ETH today?” or
“What’s BTC outlook for this weekend?”

## 🧠 Showcase Note
This project is archived as a portfolio piece.
It demonstrates:

- API integrations (Binance, CryptoPanic, OpenAI).
- AI prompt engineering.
- Tkinter-based GUI design.
- Data analysis & storage logic.

I’ve decided to evolve this idea into a Custom GPT connected to APIs,
focusing on real-time AI-driven trading insights.

## ✍️ Author
Built with curiosity, caffeine, and my buddy ChatGPT.
Eduardo Gallifa – QA Automation Engineer, Industrial Engineer, Crypto enthusiast, Gamer 🤓, Catholic (Jesuschrist is King 🗿👑).

Shout-out to my bro Portillo, always helping with crypto brainstorming. 😎

## 📨 Contact
- [LinkedIn](https://www.linkedin.com/in/eduardogallifaochoa)
- [GitHub](https://github.com/eduardogallifaochoa)
