import json
from dotenv import load_dotenv
from openai import OpenAI
import os
import sys

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

from database.db_utils import init_db
from services.report_generator import generate_analysis
from services.pattern_analysis import analyze_all_cryptos

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Init DB
init_db()

print("🟢 Manual summary generation started...\n")

# 1. Analyze all cryptos
crypto_analyses = analyze_all_cryptos()
for analysis in crypto_analyses:
    symbol = analysis.get("symbol", "Unknown").replace("USDT", "")
    if "error" in analysis:
        print(f"[{symbol}] Error: {analysis['error']}\n")
    else:
        print(f"[{symbol}] {analysis['suggestion']}\n")

# 2. Generate AI analysis and save summary
generate_analysis(client)
