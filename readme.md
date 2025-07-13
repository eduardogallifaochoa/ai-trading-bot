![AI Trading Banner](images/ai-banner-resized.png)

# 🧠 AI Trading Playground: BTC and ETH Tracker Bot

Hey there! I'm Eduardo Gallifa, a Manual QA Engineer currently transitioning into automation (because let’s be honest: they make more money and work less hahahaha). Hopefully, someday I’ll land a QA Manager role. Officially, I’m an Industrial Engineer and I also have a degree in Psychology.

Since around 2018 I’ve been into crypto for a while now. I’ve seen Bitcoin go up and down thousands of times. I remember it at 20k, and now it's over 100k. Crazy stuff.

This little project is my playground. It’s where I mess around with the things I’ve been learning lately in automation, especially APIs. I see APIs as engines, chunks of code that can talk to each other (or at least that’s how it makes sense in my head). Digital assets that you can connect to each other with the powerful, and they can communicate with themselves through the power of JSON(JavaScript Object Notation)

The OpenAI API feels like a smart robot brain you can connect to anything. The Binance API is more like a real-time crypto data feed. One thinks(OpenAI API), and the other shows numbers(Binance API).

Together? An AI trader XD

Right now, this project just connects to Binance and shows BTC and ETH prices in the terminal, but the goal is to build a full GPT-powered auto-trading bot. One step at a time.

This repo is a mix of crypto, automation, curiosity, and a bit of humor(TDHD coding JK full respect to the mental illness person out there I send them love). I also use this project to show my coding progress in case someone wants to hire me (please do, I need a job jasjasjdasd).

Thanks for reading this far. Now let me walk you through how this bot works, in a chill, and simple way.(According to me)

## 📦 Project Structure

ai-trading-bot/  
├── bot.py  
├── .env  
├── requirements.txt  
└── README.md

## 🤖 How This Thing Works (The Chill Guide)

Step 1

Generate your Binance API keys here:  
https://www.binance.com/en/my/settings/api-management
(This is the official website of Binance, but you can navigate to it by yourself as well for max security.)

Open VSCode create a new folder, or open one, name it for example: ai-bot
Then create a file called `.env` (Yes literally ".env"), and paste your Binance API keys like this:

BINANCE_API_KEY=your_api_key_here  
BINANCE_API_SECRET=your_api_secret_here

Save it. Ctrl + S (Trust me in VSCode you have to save everything)

**(🗝️ Do I need Binance API keys right now?**

**Technically? No.**

**The bot only uses public endpoints from Binance, so no authentication is needed *yet*.  **
**But I added `.env` handling because I plan to add private features later (like balance tracking, trading, alerts, etc.).**

**So yeah, you'll see `.env` stuff in the code, but it doesn't break if you don't have one yet — it's future-proof 😎)**

Step 2

Open a terminal in VSCode, and install the requirements.txt file  
You have to write, and enter the code in the terminal like this to install the packages inside your virtual environment, or your general environment doesn't matter, but it's a good practice to use virtual environments(clean copies of Python in this case without any other dependencies, or libraries (requirements.txt) installed.):

pip install -r requirements.txt

Step 3  
In the terminal you have to write a code to run the bot, like this:

python bot.py

And click enter.

Step 4  
What it does:  
It connects to Binance  
Gets the price of BTC and ETH in USDT  
Shows the prices in the terminal  
Saves them (with time) into a file called `price_log.txt`  
Waits 3 minutes, and repeats forever.



What I want to add later:  
Simple buy/sell logic 
OpenAI-powered decision making  
Telegram, or Discord alerts  
Dashboard(it's a need for non tech guys) 
Make it smarter than me



## ⚡️ Quick Recap (TL;DR version)
👉 *Heads up*: You don’t need a .env file for now, but the code supports it in case you wanna scale it up later.
(You can jump to step 3)
1. Go to [Binance API Management](https://www.binance.com/en/my/settings/api-management) and generate your keys  
2. Create a `.env` file in your folder and paste this inside (replace with your real keys):  

    BINANCE_API_KEY=your_api_key_here
    BINANCE_API_SECRET=your_api_secret_here

3. Open terminal, and install the packages:  
   `pip install -r requirements.txt`  
4. Run the bot with:  
   `python bot.py`  
5. The bot will:  
   - Fetch BTC, and ETH prices from Binance  
   - Print them in the terminal  
   - Save them to `price_log.txt`  
   - Repeat every 3 minutes

Sit back, relax, and watch the magic happen 🧙‍♂️



## 🧠 Author

Crafted with curiosity, caffeine, and help from my buddy ChatGPT — plus the hope of making it big someday (or at least making some cash)  
**Eduardo Gallifa (eduardogallifaochoa)**
A warm shout-out to my real-life bro **Portillo**, who always helps me with crypto 😎
