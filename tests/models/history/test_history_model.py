# import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    test_data = HistoryModel.list_as_json()

    assert "Hello, I like videogame" in test_data
    assert "Do you love music?" in test_data
