import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history(prepare_base):
    history_translations_str = HistoryModel.list_as_json()
    history_translations = json.loads(history_translations_str)
    assert any(
        entry["text_to_translate"] == "Hello, I like videogame"
        for entry in history_translations
    )
    assert any(
        entry["text_to_translate"] == "Do you love music?"
        for entry in history_translations
    )
