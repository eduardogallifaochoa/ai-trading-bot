import tkinter as tk
from tkinter import ttk
from services.pattern_analysis import analyze_all_cryptos

def create_dashboard_section(root, default_font, trading_mode, trade_type):
    """
    Creates the dashboard frame and fills it with real-time crypto analysis.
    """

    # Dropdowns: Trading Mode y Trade Type como Combobox (solo lectura)
    mode_label = tk.Label(root, text="Trading Mode:", bg="#1e1e1e", fg="white", font=(default_font, 11, "bold"))
    mode_label.pack(anchor="w", padx=5)
    trading_mode = ttk.Combobox(root, values=["daily", "weekly", "monthly"], state="readonly")
    trading_mode.current(0)
    trading_mode.pack(anchor="w", padx=5)

    type_label = tk.Label(root, text="Trade Type:", bg="#1e1e1e", fg="white", font=(default_font, 11, "bold"))
    type_label.pack(anchor="w", padx=5)
    trade_type = ttk.Combobox(root, values=["spot", "futures"], state="readonly")
    trade_type.current(0)
    trade_type.pack(anchor="w", padx=5)

    dashboard_frame = tk.Frame(root, bg="#1e1e1e")
    dashboard_frame.pack(fill="both", expand=True, pady=10)

    headers = ["Crypto", "Price", "Recommendation"]
    widths = [10, 15, 80]
    for i, header in enumerate(headers):
        tk.Label(
            dashboard_frame,
            text=header,
            bg="#333333",
            fg="white",
            font=(default_font, 12, "bold"),
            width=widths[i],
            anchor="w",
            padx=5,
            pady=5
        ).grid(row=0, column=i, sticky="w")

    def refresh_dashboard():
        # Clear old data
        for widget in dashboard_frame.winfo_children()[3:]:  # skip headers
            widget.destroy()

        # Fetch analysis
        crypto_analyses = analyze_all_cryptos(
            trading_mode=trading_mode.get(),
            trade_type=trade_type.get()
        )

        for idx, analysis in enumerate(crypto_analyses, start=1):
            symbol = analysis.get("symbol", "Unknown").replace("USDT", "")
            price = f"{analysis.get('current_price', 0):.2f} USD"
            recommendation = analysis.get("suggestion", "No data.")

            color = "gray"
            if analysis.get("action") == "Buy":
                color = "green"
            elif analysis.get("action") == "Sell":
                color = "red"

            tk.Label(
                dashboard_frame,
                text=symbol,
                bg="#1e1e1e",
                fg=color,
                width=widths[0],
                anchor="w",
                padx=5,
                pady=2
            ).grid(row=idx, column=0, sticky="w")

            tk.Label(
                dashboard_frame,
                text=price,
                bg="#1e1e1e",
                fg=color,
                width=widths[1],
                anchor="w",
                padx=5,
                pady=2
            ).grid(row=idx, column=1, sticky="w")

            tk.Label(
                dashboard_frame,
                text=recommendation,
                bg="#1e1e1e",
                fg=color,
                wraplength=600,
                justify="left",
                anchor="w",
                padx=5,
                pady=2
            ).grid(row=idx, column=2, sticky="w")

        root.after(60000, refresh_dashboard)

    refresh_dashboard()
    return dashboard_frame
