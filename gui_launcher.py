import tkinter as tk
from tkinter import scrolledtext, simpledialog
import subprocess

# Run command in subprocess and capture output
def run_command(command):
    try:
        result = subprocess.run(
            command, shell=True, text=True, capture_output=True
        )
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, result.stdout if result.stdout else result.stderr)
    except Exception as e:
        output_box.insert(tk.END, f"Error: {e}")

def generate_report():
    prompt = simpledialog.askstring("Generate Report", "Enter your prompt:")
    if prompt:
        run_command(f'python generate_report.py "{prompt}"')

def show_history():
    run_command("python generate_report.py --history")

def show_last():
    n = simpledialog.askinteger("Show Last Reports", "Enter N:")
    if n:
        run_command(f"python generate_report.py --last {n}")

def read_report():
    report_id = simpledialog.askinteger("Read Report", "Enter report ID:")
    if report_id:
        run_command(f"python generate_report.py --read {report_id}")

def show_patterns():
    run_command("python generate_report.py --patterns")

def clean_db():
    run_command("python generate_report.py --clean")

# GUI setup
root = tk.Tk()
root.title("AI Trading Bot - GUI (Unified Reports)")
root.configure(bg="#1e1e1e")

# Buttons with dark theme
btn_style = {"width": 30, "bg": "#333333", "fg": "white", "activebackground": "#444444", "activeforeground": "white"}

tk.Button(root, text="1. Generate (Report+Summary)", command=generate_report, **btn_style).pack(pady=5)
tk.Button(root, text="2. Show History", command=show_history, **btn_style).pack(pady=5)
tk.Button(root, text="3. Show Last N Reports", command=show_last, **btn_style).pack(pady=5)
tk.Button(root, text="4. Read Report by ID", command=read_report, **btn_style).pack(pady=5)
tk.Button(root, text="5. Show Patterns", command=show_patterns, **btn_style).pack(pady=5)
tk.Button(root, text="6. Clean Database", command=clean_db, **btn_style).pack(pady=5)

# Output box with dark theme
output_box = scrolledtext.ScrolledText(root, width=100, height=20, bg="#1e1e1e", fg="#00FF00", insertbackground="white")
output_box.pack(pady=10)

# Run loop
root.mainloop()
