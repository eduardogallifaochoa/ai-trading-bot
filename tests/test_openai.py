import sys, os
import unittest

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import services.gpt_analyzer as gpt_analyzer


class TestOpenAIIntegration(unittest.TestCase):

    def test_openai_analysis(self):
        """Test real call to OpenAI GPT analysis using fake prices and news."""
        btc_price = 68000.0
        eth_price = 3600.0
        btc_closes = [67500.0, 67800.0, 67900.0]
        eth_closes = [3500.0, 3550.0, 3580.0]
        news_text = "Bitcoin and Ethereum markets are experiencing strong momentum."

        response = gpt_analyzer.generate_analysis(
            btc_price=btc_price,
            eth_price=eth_price,
            btc_closes=btc_closes,
            eth_closes=eth_closes,
            news_text=news_text
        )

        # Validates that OpenAI returned a non-empty response
        self.assertTrue(len(response) > 0, "OpenAI response is empty")


if __name__ == "__main__":
    unittest.main()
