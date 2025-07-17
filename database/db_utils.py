# db_utils.py

import sqlite3
from datetime import datetime

# Create the SQLite database and the summaries table (run once)
def init_db():
    conn = sqlite3.connect("crypto_summaries.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            btc_price REAL,
            eth_price REAL,
            btc_closes TEXT,
            eth_closes TEXT,
            news TEXT,
            analysis TEXT
        )
    """)
    conn.commit()
    conn.close()

# Save one summary entry into the database
def save_summary_to_db(btc_price, eth_price, btc_closes, eth_closes, news, analysis):
    conn = sqlite3.connect("crypto_summaries.db")
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO summaries (timestamp, btc_price, eth_price, btc_closes, eth_closes, news, analysis)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        btc_price,
        eth_price,
        ", ".join([f"{c:.2f}" for c in btc_closes]),
        ", ".join([f"{c:.2f}" for c in eth_closes]),
        news,
        analysis
    ))

    conn.commit()
    conn.close()
