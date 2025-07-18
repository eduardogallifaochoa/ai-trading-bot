from dotenv import load_dotenv
from openai import OpenAI
import os
from database.db_utils import init_db
from services.report_generator import generate_analysis

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

init_db()

print("🟢 Manual summary generation started...\n")
generate_analysis(client, save_to="summary")
