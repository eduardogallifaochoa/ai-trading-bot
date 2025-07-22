import sys, os
import unittest
from dotenv import load_dotenv

# Asegura que el directorio raíz esté en el path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import bot  # Importamos todo el bot

# Carga variables de entorno
load_dotenv()

class TestOpenAIIntegration(unittest.TestCase):
    def test_api_key_exists(self):
        """Check if OPENAI_API_KEY is loaded correctly."""
        api_key = os.getenv("OPENAI_API_KEY")
        self.assertIsNotNone(api_key, "OPENAI_API_KEY is not set in environment variables.")

    def test_openai_mock(self):
        """Mock test for ask_openai."""
        with unittest.mock.patch("bot.ask_openai", return_value="Mock response."):
            response = bot.ask_openai("What is BTC?")
            self.assertEqual(response, "Mock response.", "Mocked response did not match expected output.")


if __name__ == "__main__":
    unittest.main()
