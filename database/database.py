import sqlite3
from datetime import datetime

# 1. Initialize the database and create the table (only needs to run once)
def init_db():
    # Connect to (or create) the SQLite database file
    conn = sqlite3.connect("crypto_summaries.db")
    cursor = conn.cursor()

    # Create a table to store summaries if it doesn't already exist
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

    # Commit changes and close connection
    conn.commit()
    conn.close()

# 2. Save a summary to the database
def save_summary_to_db(btc_price, eth_price, btc_closes, eth_closes, news, analysis):
    # Connect to the SQLite database
    conn = sqlite3.connect("crypto_summaries.db")
    cursor = conn.cursor()

    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert the summary data into the table
    cursor.execute("""
        INSERT INTO summaries (timestamp, btc_price, eth_price, btc_closes, eth_closes, news, analysis)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        btc_price,
        eth_price,
        ", ".join([f"{c:.2f}" for c in btc_closes]),  # Convert close list to formatted string
        ", ".join([f"{c:.2f}" for c in eth_closes]),
        news,
        analysis
    ))

    # Commit and close connection
    conn.commit()
    conn.close()

# Optional: run this file directly to initialize the database
if __name__ == "__main__":
    init_db()
