from unittest.mock import patch
from bot import ask_openai  # Ajusta si tu función está en otro módulo

@patch("bot.ask_openai")  # Mockea la función real
def test_openai_mock(mock_ask):
    mock_ask.return_value = "Mock response."
    response = ask_openai("What is BTC?")
    assert response == "Mock response."
