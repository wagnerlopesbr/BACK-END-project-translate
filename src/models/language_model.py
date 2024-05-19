from models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self) -> dict[str, str]:
        return {
            # .get() instead of [] to avoid KeyError
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym"),
        }

    @classmethod
    def list_dicts(cls, query={}):
        results = cls._collection.find(query, {"_id": 0})
        return [result for result in results]
