import os
import openai
import dotenv

# Load environment variables
dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ask OpenAI to generate an analysis based on the crypto context
def generate_analysis(btc_price, eth_price, btc_closes, eth_closes, news_text):
    # Create the OpenAI client only when this function runs
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
You're a crypto market analyst bot. Generate a professional but casual summary of the current situation for BTC and ETH.

Current prices:
- BTC: ${btc_price:,.2f}
- ETH: ${eth_price:,.2f}

Last 3 daily closes:
BTC:
- 3 days ago: ${btc_closes[0]:,.2f}
- 2 days ago: ${btc_closes[1]:,.2f}
- Yesterday: ${btc_closes[2]:,.2f}
ETH:
- 3 days ago: ${eth_closes[0]:,.2f}
- 2 days ago: ${eth_closes[1]:,.2f}
- Yesterday: ${eth_closes[2]:,.2f}

Recent news:
{news_text}

Please analyze current trends, risks, and possible moves based on this info.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600
    )
    return response.choices[0].message.content.strip()
