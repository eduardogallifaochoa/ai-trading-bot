# gui_launcher.py
import tkinter as tk
from tkinter import scrolledtext
import tkinter.font as tkFont
import sys
import os

# === UTF-8 output ===
sys.stdout.reconfigure(encoding='utf-8')

# === Fix Python Paths ===
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICES_PATH = os.path.join(ROOT_DIR, "services")
GUI_MODULES_PATH = os.path.join(ROOT_DIR, "gui_modules")

for path in [SERVICES_PATH, GUI_MODULES_PATH]:
    if path not in sys.path:
        sys.path.append(path)

# === Import modules ===
from gui_modules.gui_top_controls import create_top_controls
from gui_modules.gui_buttons import create_buttons_section
from gui_modules.gui_dashboard import create_dashboard_section
from gui_modules.gui_chat import create_chat_section

# === MAIN WINDOW ===
root = tk.Tk()
root.title("AI Trading Bot - Pro GUI")
root.configure(bg="#1e1e1e")
root.geometry("1200x800")
root.minsize(1100, 700)

# Default font
default_font = tkFont.Font(family="Roboto", size=12)
root.option_add("*Font", default_font)

# Variables
trading_mode = tk.StringVar(value="daily")
trade_type = tk.StringVar(value="spot")

# ======== GRID CONFIG ========
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

# ======== TOP CONTROLS (full width) ========
top_controls_frame = tk.Frame(root, bg="#1e1e1e")
top_controls_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)
create_top_controls(top_controls_frame, trading_mode, trade_type)

# ======== LEFT PANEL (Output + Buttons) ========
left_panel = tk.Frame(root, bg="#1e1e1e")
left_panel.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
left_panel.grid_rowconfigure(0, weight=1)

# Output box (Top)
output_box = scrolledtext.ScrolledText(
    left_panel, width=40, height=10, bg="#1e1e1e",
    fg="#00FF00", insertbackground="white", font=default_font
)
output_box.pack(fill="x", pady=5)

# Button panel
btn_style = {
    "width": 30,
    "bg": "#333333",
    "fg": "white",
    "activebackground": "#444444",
    "activeforeground": "white",
    "relief": "flat",
    "highlightthickness": 1,
    "highlightbackground": "#555555"
}
buttons_frame = tk.Frame(left_panel, bg="#1e1e1e")
buttons_frame.pack(fill="y", pady=10)
create_buttons_section(buttons_frame, btn_style, output_box, trading_mode, trade_type)

# ======== RIGHT PANEL (Dashboard + Chat) ========
right_panel = tk.Frame(root, bg="#1e1e1e")
right_panel.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)
right_panel.grid_rowconfigure(0, weight=3)
right_panel.grid_rowconfigure(1, weight=1)
right_panel.grid_columnconfigure(0, weight=1)

# Dashboard
dashboard_frame = tk.Frame(right_panel, bg="#1e1e1e")
dashboard_frame.grid(row=0, column=0, sticky="nsew")
create_dashboard_section(dashboard_frame, default_font, trading_mode, trade_type)

# Chat
chat_frame = tk.Frame(right_panel, bg="#1e1e1e")
chat_frame.grid(row=1, column=0, sticky="nsew", pady=(10, 0))
create_chat_section(chat_frame, output_box, trading_mode, trade_type)

# === Start loop ===
root.mainloop()
