from pymongo import MongoClient
import os


client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017/"))


db = client[os.environ.get("DB_NAME", "test_db_traduzo")]
