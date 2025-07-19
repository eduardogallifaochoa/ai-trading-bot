import tkinter as tk
from tkinter import ttk

def create_top_controls(root, trading_mode, trade_type):
    """
    Create the trading mode and trade type selectors.

    Both dropdowns are set to 'readonly' to prevent users from typing
    arbitrary values. They can only select from the given options.
    """
    trading_frame = tk.Frame(root, bg="#1e1e1e")
    trading_frame.pack(pady=5)

    # --- Trading Mode Selector ---
    tk.Label(
        trading_frame,
        text="Trading Mode:",
        bg="#1e1e1e",
        fg="white"
    ).grid(row=0, column=0, padx=5)

    mode_selector = ttk.Combobox(
        trading_frame,
        textvariable=trading_mode,
        values=["daily", "weekly", "monthly"],
        state="readonly"  # Prevent typing
    )
    mode_selector.grid(row=0, column=1, padx=5)
    mode_selector.current(0)  # Default to "daily"

    # --- Trade Type Selector ---
    tk.Label(
        trading_frame,
        text="Trade Type:",
        bg="#1e1e1e",
        fg="white"
    ).grid(row=0, column=2, padx=5)

    type_selector = ttk.Combobox(
        trading_frame,
        textvariable=trade_type,
        values=["spot", "futures"],
        state="readonly"  # Prevent typing
    )
    type_selector.grid(row=0, column=3, padx=5)
    type_selector.current(0)  # Default to "spot"
