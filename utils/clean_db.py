# utils/clean_db.py
import sqlite3

DB_PATH = "crypto_summaries.db"

def clean_db():
    """
    Remove entries from 'summaries' and 'reports' tables that have errors
    or empty fields. Then vacuum the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Find and delete entries with error messages
    cursor.execute("SELECT COUNT(*) FROM summaries WHERE news LIKE '%⚠️%' OR analysis LIKE '%⚠️%'")
    error_summaries = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reports WHERE content LIKE '%⚠️%'")
    error_reports = cursor.fetchone()[0]

    print(f"Found {error_summaries} entries with errors in 'summaries'.")
    print(f"Found {error_reports} entries with errors in 'reports'.")

    cursor.execute("DELETE FROM summaries WHERE news LIKE '%⚠️%' OR analysis LIKE '%⚠️%'")
    cursor.execute("DELETE FROM reports WHERE content LIKE '%⚠️%'")
    conn.commit()

    # Optimize database
    cursor.execute("VACUUM")
    conn.commit()
    conn.close()

    print(f"Deleted {error_summaries} summaries and {error_reports} reports with errors.")
    print("Database vacuumed and optimized.")
