import pymongo
from bson import ObjectId

from constant import *


class RegisterDTO:

    def __init__(self):
        self.client = pymongo.MongoClient(DB_BASIC_CONN_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[USER_COLLECTION]

    async def add_user(self, user_data):
        user_data[OBJECT_ID_TAG] = ObjectId()
        result = self.collection.insert_one(user_data)
        return {STATUS_TAG: result.acknowledged, VALUE_TAG: str(result.inserted_id)}

    async def check_user(self, user_id):
        result = self.collection.find_one({USER_ID_TAG: user_id}, {})
        return str(result[OBJECT_ID_TAG]) if result else None

