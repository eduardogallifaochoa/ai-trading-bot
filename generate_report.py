import argparse
from openai import OpenAI
from dotenv import load_dotenv
import os
import sys
import io

# === FIX PATHS ===
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

SERVICES_PATH = os.path.join(ROOT_DIR, "services")
UTILS_PATH = os.path.join(ROOT_DIR, "utils")
for path in [SERVICES_PATH, UTILS_PATH]:
    if path not in sys.path:
        sys.path.append(path)
# =================

from services.report_generator import generate_analysis
from database.db_utils import get_reports_history, get_report_by_id, init_db

# Fix encoding
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize database (creates tables if not exist)
init_db()


def show_history(limit=10):
    """Display the last N reports (default: 10)."""
    try:
        reports = get_reports_history(limit=limit)
        for r in reports:
            print(f"[ID {r.get('id', '?')}] {r['created_at']} | {r['prompt']}\n-> {r['content'][:150]}...\n")
    except Exception as e:
        print(f"Error fetching history: {e}")


def read_report(report_id):
    """Display a specific report by ID."""
    try:
        report = get_report_by_id(report_id)
        if report:
            print(f"\n[Report ID {report['id']}] - {report['created_at']}")
            print(f"Prompt: {report['prompt']}\n")
            print(f"Content:\n{report['content']}\n")
        else:
            print(f"No report found with ID {report_id}.")
    except Exception as e:
        print(f"Error reading report: {e}")


# CLI Argument Parsing
parser = argparse.ArgumentParser(description="AI Trading Bot - Report Generator")
parser.add_argument("prompt", nargs="?", help="Custom prompt for GPT analysis")
parser.add_argument("--history", action="store_true", help="Show history (last 10 reports)")
parser.add_argument("--last", type=int, help="Show the last N reports")
parser.add_argument("--read", type=int, help="Read a specific report by ID")
parser.add_argument("--patterns", action="store_true", help="Show real-time market patterns")
parser.add_argument("--clean", action="store_true", help="Clean database entries with errors")

args = parser.parse_args()

# Command execution
if args.history:
    show_history(limit=10)

elif args.last is not None:
    if args.last > 0:
        show_history(limit=args.last)
    else:
        print("Please provide a positive integer for --last.")

elif args.read is not None:
    read_report(args.read)

elif args.patterns:
    from services.pattern_analysis import analyze_all_cryptos

    print("\n[REAL-TIME PATTERN ANALYSIS]\n")
    crypto_analyses = analyze_all_cryptos()
    for analysis in crypto_analyses:
        symbol = analysis.get("symbol", "Unknown").replace("USDT", "")
        if "error" in analysis:
            print(f"{symbol} → Error: {analysis['error']}\n")
        else:
            # Mensaje intuitivo en una sola línea
            print(f"{symbol} → {analysis['suggestion']}")

elif args.clean:
    from utils.clean_db import clean_db
    clean_db()

elif args.prompt:
    generate_analysis(client, user_prompt=args.prompt)

else:
    parser.print_help()
