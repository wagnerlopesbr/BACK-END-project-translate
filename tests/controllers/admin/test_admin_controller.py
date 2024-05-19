from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
from datetime import datetime
from bson import ObjectId


def test_history_delete(app_test):
    test_user = UserModel({"name": "test_name", "token": "test_token"})
    test_user.save()
    test_history = HistoryModel({
        "text_to_translate": "House",
        "translated": "Casa",
        "translate_from": "en",
        "translate_to": "pt",
        "timestamp": datetime.now(),
    })
    test_history.save()
    test_history_id = str(test_history.data.get("_id"))
    response = app_test.delete(
        f"/admin/history/{test_history_id}",
        headers={
            "Authorization": "test_token",
            "User": "test_name",
            }
        )
    assert response.status_code == 204
    assert HistoryModel.find_one({"_id": ObjectId(test_history_id)}) is None
