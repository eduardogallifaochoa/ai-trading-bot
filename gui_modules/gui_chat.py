import tkinter as tk
from tkinter import scrolledtext
from services.report_generator import generate_analysis
from services.pattern_analysis import analyze_all_cryptos
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load OpenAI client
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def ask_cryptobot(query, trading_mode, trade_type):
    """Ask the CryptoBot using GPT and market analysis."""
    analysis = analyze_all_cryptos(trading_mode=trading_mode.get(), trade_type=trade_type.get())
    pattern_summary = "\n".join([
        f"- {a.get('symbol', '??')} → {a.get('pattern')} ({a.get('action')}): {a.get('suggestion')}"
        for a in analysis
    ])
    user_prompt = (
        f"User question: {query}\n\n"
        f"Trade Type: {trade_type.get()}\n"
        f"Crypto pattern analysis:\n{pattern_summary}\n\n"
        "Answer with a professional but friendly tone and give a clear final recommendation."
    )
    return generate_analysis(client, user_prompt=user_prompt)

def create_chat_section(root, output_box, trading_mode, trade_type):
    """Create the chat panel and suggestions."""
    chat_label = tk.Label(root, text="CryptoBot Chat", bg="#1e1e1e", fg="cyan", font=("Roboto", 14, "bold"))
    chat_label.pack(pady=(5, 0))

    chat_frame = tk.Frame(root, bg="#1e1e1e")
    chat_frame.pack(fill="both", expand=True, pady=5)

    # Historial (solo lectura)
    chat_history = scrolledtext.ScrolledText(
        chat_frame,
        wrap="word",
        height=10,
        bg="#1e1e1e",
        fg="white",
        font=("Roboto", 11),
        state='disabled'
    )
    chat_history.pack(fill="both", expand=True, padx=5, pady=5)
    chat_history.tag_config("user", foreground="#00FF00")
    chat_history.tag_config("bot", foreground="#00BFFF")

    # Entrada usuario
    chat_entry = tk.Entry(root, font=("Roboto", 12), bg="#333333", fg="white")
    chat_entry.pack(fill="x", padx=5, pady=5)

    def send_message():
        user_msg = chat_entry.get().strip()
        if not user_msg:
            return
        chat_history.config(state='normal')
        chat_history.insert(tk.END, f"You: {user_msg}\n", "user")
        chat_history.see(tk.END)
        chat_entry.delete(0, tk.END)
        response = ask_cryptobot(user_msg, trading_mode, trade_type)
        chat_history.insert(tk.END, f"CryptoBot: {response}\n\n", "bot")
        chat_history.see(tk.END)
        chat_history.config(state='disabled')

    chat_entry.bind("<Return>", lambda e: send_message())
    tk.Button(root, text="Send", command=send_message, bg="#444444", fg="white").pack(pady=5)
