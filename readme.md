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
├── bot.py                 ← main script that runs the bot
├── .env                   ← (optional) your Binance API keys
├── requirements.txt       ← required packages for Python users
├── README.md              ← this beautiful guide you're reading
├── dist/
│   └── bot.exe            ← standalone executable (for non-coders)
├── images/
│   └── ai-banner-resized.png ← header image for README

## 🤖 How This Thing Works (The Chill Guide)

✅ Quick Setup
Download this repo as ZIP
Unzip it anywhere you want (for example: Desktop).

Open the unzipped folder, and go to the folder /dist/

Double-click bot.exe
That’s it! A black terminal window will pop up and start fetching crypto prices.

Let it run

Every 3 minutes, it fetches the BTC and ETH prices

It prints the prices in the terminal

It logs them into a file called price_log.txt (in the same folder)

Close the window or press Ctrl + C to stop it

🧠 Bonus tip: If the terminal opens and instantly closes, try launching it via right-click → "Open in Terminal" or use cmd to catch errors.

**What I want to add later:**
Simple buy/sell logic 
OpenAI-powered decision making  
Telegram, or Discord alerts  
Dashboard(it's a need for non tech guys) 
Make it smarter than me

## 🧠 Author

Crafted with curiosity, caffeine, and help from my buddy ChatGPT plus the hope of making it big someday (or at least making some cash which I'm already doing thank God(Jesuschrist))  
**Eduardo Gallifa (eduardogallifaochoa)**
A warm shout-out to my real-life bro **Portillo**, who always helps me with crypto 😎
