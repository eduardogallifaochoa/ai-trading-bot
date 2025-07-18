# database/db_utils.py

import sqlite3
from datetime import datetime

DB_PATH = "crypto_summaries.db"

# Create the SQLite database and the summaries table (run once)
def init_db():
    conn = sqlite3.connect(DB_PATH)
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
    # Create reports table (for manual or on-demand reports)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Save one summary entry into the database
def save_summary_to_db(btc_price, eth_price, btc_closes, eth_closes, news, analysis):
    conn = sqlite3.connect(DB_PATH)
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

# Save a manual or custom report
def save_report_to_db(prompt, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reports (prompt, content)
        VALUES (?, ?)
    """, (prompt, content))
    conn.commit()
    conn.close()

# Retrieve report history
def get_reports_history(limit=10):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, prompt, content, created_at FROM reports
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [{'id': r[0], 'prompt': r[1], 'content': r[2], 'created_at': r[3]} for r in rows]

def get_report_by_id(report_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, prompt, content, created_at FROM reports WHERE id=?
    """, (report_id,))
    row = cursor.fetchone()
    conn.close()
    return {'id': row[0], 'prompt': row[1], 'content': row[2], 'created_at': row[3]} if row else None
