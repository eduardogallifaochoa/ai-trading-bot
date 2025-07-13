AI Trading Playground: BTC and ETH Tracker Bot

Hey there, I’m Eduardo Gallifa — a Manual QA Engineer currently transitioning into automation (because, let’s be real: better pay, smarter work). I’m also an Industrial Engineer with a second degree in Psychology. Been into crypto since 2018. I’ve seen BTC at 20k, and now over 100k. Wild ride.

This repo is my personal playground. I built it to mess around with everything I’ve been learning lately: automation, APIs, and how to connect smart stuff to get real value. I see APIs as engines that talk via JSON.

The OpenAI API is like a thinking brain. Binance is a real-time crypto data stream.One thinks. The other feeds numbers.Together? An AI-powered crypto assistant 😎

💬 What Can This Bot Do?

✅ Shows live BTC and ETH prices in the terminal

✅ Logs prices every 3 minutes to price_log.txt

✅ You can ask crypto related stuff like:

“How much is ETH right now?”

“What was the candle close for ETH yesterday?”

“What do you think of Bitcoin today?”

✅ Answers using OpenAI, with contextual info

✅ Fetches historical candle closes from Binance (supports up to 30 days)

🧠 Next Steps (Planned Features)


Basic buy/sell logic

OpenAI-based trading suggestions

Telegram, or Discord alerts

A clean dashboard (for non-dev users)

Improve decision-making logic with OpenAI

🗖️ Project Structure

ai-trading-bot/
├── bot.py                 ← main script
├── .env                   ← your OpenAI key here
├── requirements.txt       ← required packages
├── README.md              ← this file
├── dist/
│   └── bot.exe            ← standalone .exe for Windows
├── images/
│   └── ai-banner-resized.png
└── price_log.txt          ← stores price logs every 3 minutes

**⚙️ How to Use It**

👟 Option 1: Run the .exe

Download or clone the repo

Go to the /dist/ folder

Run bot.exe

Ask whatever you want, like:

What was ETH’s candle close yesterday?

What’s the current BTC price?

🐍 Option 2: Run with Python (for devs)

git clone https://github.com/eduardogallifaochoa/ai-trading-bot.git
cd ai-trading-bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python bot.py

🧠 Tip: If the terminal closes instantly, right-click the folder → "Open in Terminal" and run it from there to check for errors.

✍️ Author

Built with curiosity, caffeine, and help from my buddy ChatGPT.Eduardo Gallifa – QA Engineer, Crypto Enthusiast, and Self-Taught Dev.

Massive shout-out to my real-life bro Portillo, who always helps with crypto stuff 😎If you want to collab or hire me — let’s talk.

📨 Contact:LinkedIn | GitHub