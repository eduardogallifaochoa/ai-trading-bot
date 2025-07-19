# gui_modules/gui_buttons.py

import tkinter as tk
from tkinter import simpledialog
import subprocess
from services.pattern_analysis import analyze_all_cryptos
from services.portfolio_manager import add_trade, analyze_portfolio

def run_command(command, output_box):
    """Run a CLI command and display output in the text box."""
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, encoding="utf-8")
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, result.stdout if result.stdout else result.stderr)
        return result.stdout
    except Exception as e:
        output_box.insert(tk.END, f"Error: {e}")
        return None

def generate_report(output_box):
    """Prompt user for input and generate a report."""
    prompt = simpledialog.askstring("Generate Report", "Enter your prompt:")
    if prompt:
        run_command(f'python generate_report.py "{prompt}"', output_box)

def show_history(output_box):
    """Display the full report history."""
    run_command("python generate_report.py --history", output_box)

def show_last(output_box):
    """Show the last N reports."""
    n = simpledialog.askinteger("Show Last Reports", "Enter N:")
    if n:
        run_command(f"python generate_report.py --last {n}", output_box)

def read_report(output_box):
    """Read a report by ID."""
    report_id = simpledialog.askinteger("Read Report", "Enter report ID:")
    if report_id:
        run_command(f"python generate_report.py --read {report_id}", output_box)

def show_patterns(output_box, trading_mode, trade_type):
    """Analyze patterns with current trading mode and type."""
    run_command(
        f"python generate_report.py --patterns --mode {trading_mode.get()} --trade_type {trade_type.get()}",
        output_box
    )

def clean_db(output_box):
    """Clean the database."""
    run_command("python generate_report.py --clean", output_box)

def add_trade_ui(output_box):
    """UI for adding a trade to the portfolio."""
    symbol = simpledialog.askstring("Add Trade", "Enter symbol (e.g., ETHUSDT):")
    if not symbol:
        return
    usdt = simpledialog.askfloat("Add Trade", "How many USDT did you invest?")
    buy_price = simpledialog.askfloat("Add Trade", "What was the buy price (USD)?")
    if symbol and usdt and buy_price:
        add_trade(symbol.upper(), usdt, buy_price)
        output_box.insert(tk.END, f"\nTrade added: {symbol}, {usdt} USDT @ {buy_price} USD\n")

def show_portfolio_ui(output_box, trade_type):
    """Display portfolio analysis in the output box."""
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "[PORTFOLIO ANALYSIS]\n\n")
    portfolio_data = analyze_portfolio(trade_type=trade_type.get())
    if not portfolio_data:
        output_box.insert(tk.END, "Portfolio is empty.\n")
        return

    for p in portfolio_data:
        if "error" in p:
            output_box.insert(tk.END, f"{p['symbol']}: {p['error']}\n")
        else:
            output_box.insert(
                tk.END,
                f"{p['symbol']} | Invested: {p['usdt_invested']} USDT | Buy: {p['buy_price']:.2f} USD | "
                f"Current: {p['current_price']:.2f} USD | PnL: {p['pnl_usdt']:.2f} USDT "
                f"({p['pnl_percent']:.2f}%) | Action: {p['action']}\n"
            )

def create_buttons_section(root, btn_style, output_box, trading_mode, trade_type):
    """
    Create the vertical panel of buttons.
    Clean version: no dropdowns or extra widgets here.
    """
    button_frame = tk.Frame(root, bg="#1e1e1e")
    button_frame.pack(pady=10)

    buttons = [
        ("1. Generate (Report+Summary)", lambda: generate_report(output_box)),
        ("2. Show History", lambda: show_history(output_box)),
        ("3. Show Last N Reports", lambda: show_last(output_box)),
        ("4. Read Report by ID", lambda: read_report(output_box)),
        ("5. Show Patterns (Text)", lambda: show_patterns(output_box, trading_mode, trade_type)),
        ("6. Show Portfolio", lambda: show_portfolio_ui(output_box, trade_type)),
        ("7. Add Trade to Portfolio", lambda: add_trade_ui(output_box)),
        ("8. Clean Database", lambda: clean_db(output_box)),
    ]

    for text, cmd in buttons:
        tk.Button(
            button_frame, text=text, command=cmd,
            bg="#333333", fg="white",
            activebackground="#555555", activeforeground="white",
            relief="flat", width=30, height=1, font=("Roboto", 10, "bold")
        ).pack(pady=4, padx=10)
