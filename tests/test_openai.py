import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest.mock
import bot

@unittest.mock.patch("bot.ask_openai")
def test_openai_mock(mock_ask):
    mock_ask.return_value = "Mock response."
    response = bot.ask_openai("What is BTC?")
    assert response == "Mock response."
