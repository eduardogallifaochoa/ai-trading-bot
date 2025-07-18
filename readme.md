# **AI Trading Playground: BTC and ETH Tracker Bot**

Hey there, I’m Eduardo Gallifa — a Manual QA Engineer currently transitioning into automation (because, let’s be real: better pay, smarter work). I’m also an Industrial Engineer with a second degree in Psychology. Been into crypto since 2018. I’ve seen BTC at 20k, and now over 100k. Wild ride.

This repo is my personal playground. I built it to mess around with everything I’ve been learning lately: automation, APIs, and how to connect smart stuff to get real value. I see APIs as engines that talk via JSON.

The OpenAI API is like a thinking brain. Binance is a real-time crypto data stream. One thinks. The other feeds numbers. Together? An AI-powered crypto assistant 😎

---

## **💬 Features**

### **Core**
✅ Shows live BTC and ETH prices.  
✅ Fetches historical candle closes from Binance (up to 30 days).  
✅ Uses OpenAI to generate market insights and natural-language crypto analysis.  
✅ Generates **BUY / HOLD / SELL** recommendations based on market trends.  

### **Interactive Commands**
```plaintext
“How much is ETH right now?”
“What was the candle close for ETH yesterday?”
“What do you think of Bitcoin today?”
“Analyze the BTC market for this weekend”
```
## **Reports and Summaries**
- ✅ Generate detailed **market reports** using `generate_report.py`.
- ✅ Save all reports in a local **SQLite database (`crypto_summaries.db`)**.
- ✅ **Show history** of reports, read by **ID**, or fetch the **last N reports**.
- ✅ Analyze **historical patterns** (BTC/ETH price changes, average volatility, etc.).
- ✅ **GPT-powered market insights** combining historical data + latest news.

---

## **News Integration**
- ✅ Fetches the **latest crypto news** from **CryptoPanic API**.
- ✅ Merges **news headlines with price analysis** for better decision-making.

---

## **GUI Launcher**
- ✅ A simple **Graphical User Interface (Tkinter-based)** to run commands by clicking buttons:

  - **Generate Report**  
  - **Generate Summary**  
  - **Show History**  
  - **Show Last N Reports**  
  - **Read Report by ID**  
  - **Analyze Patterns**  
  - **Clean Database** (remove corrupted entries)

---

## **Smart Pattern Analysis**
- ✅ The bot can **read its own database** and detect price/news patterns.
- ✅ Explains **patterns in human-friendly language**, using GPT.
- ✅ Outputs a **final recommendation** in **bold** (e.g., `>>> FINAL RECOMMENDATION: BUY`).

---

## **🧠 Next Steps (Planned Features)**
- Advanced **buy/sell trading logic**.  
- **Telegram or Discord alerts** for price thresholds.  
- **Dashboard with real-time charts** for BTC and ETH.  
- Enhanced AI insights using **multi-day pattern recognition**.  
- Improve database management with **automatic pruning & backups**.


## 📦 Project Structure
```plaintext
ai-trading-bot/
├── bot.py                   ← Main script
├── gui_launcher.py          ← GUI launcher (Tkinter)
├── generate_report.py       ← CLI report generator
├── services/
│   ├── price_fetcher.py     ← Fetch prices from Binance
│   ├── news_fetcher.py      ← Fetch crypto news
│   └── report_generator.py  ← AI-powered analysis
├── analytics/
│   └── patterns.py          ← Historical patterns + AI insight
├── database/
│   └── db_utils.py          ← SQLite database helpers
├── utils/
│   └── clean_db.py          ← Database cleanup tool
├── crypto_summaries.db      ← SQLite database with reports/summaries
├── price_log.txt            ← Stores price logs every 3 minutes
├── requirements.txt         ← Required packages
├── .env                     ← API keys
├── README.md                ← This file
└── dist/
    └── bot.exe              ← Standalone executable (Windows)
```
## ⚙️ How to Use It
Option 1: GUI (Recommended for non-coders)
```plaintext
python gui_launcher.py
From here, you can click buttons like Generate Report, Analyze Patterns, or Show History.
```
Option 2: CLI (Command Line)
```plaintext
# Generate a custom report
python generate_report.py "Analyze BTC market for the weekend"
```
# Show historical reports
```plaintext
python generate_report.py --history
```
# Analyze historical patterns (BUY / HOLD / SELL)
```plaintext
python generate_report.py --patterns
```
# Clean database from errors
```plaintext
python generate_report.py --clean
```
Option 3: Classic Bot
```plaintext
python bot.py
Ask natural-language crypto questions directly.
```
## ✍️ Author
Built with curiosity, caffeine, and help from my buddy ChatGPT.
Eduardo Gallifa – QA Automation Engineer, Industrial Engineer, Crypto enthusiast, Gamer🤓, Catholic (Jesuschrist is King 🗿👑).

Massive shout-out to my real-life bro Portillo, who always helps with crypto stuff 😎

## 📨 Contact
- [LinkedIn](https://www.linkedin.com/in/eduardogallifaochoa)
- [GitHub](https://github.com/eduardogallifaochoa)
