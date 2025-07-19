import tkinter as tk
from tkinter import ttk

def create_top_controls(root, trading_mode, trade_type):
    """Create the trading mode and trade type selectors."""
    trading_frame = tk.Frame(root, bg="#1e1e1e")
    trading_frame.pack(pady=5)

    tk.Label(trading_frame, text="Trading Mode:", bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=5)
    mode_selector = ttk.Combobox(trading_frame, textvariable=trading_mode, values=["daily", "weekly", "monthly"])
    mode_selector.grid(row=0, column=1, padx=5)

    tk.Label(trading_frame, text="Trade Type:", bg="#1e1e1e", fg="white").grid(row=0, column=2, padx=5)
    type_selector = ttk.Combobox(trading_frame, textvariable=trade_type, values=["spot", "futures"])
    type_selector.grid(row=0, column=3, padx=5)
