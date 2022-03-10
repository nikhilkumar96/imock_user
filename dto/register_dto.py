import pymongo
from bson import ObjectId

from constant import *
from dto.common_dto import CommonDTO


class RegisterDTO(CommonDTO):

    def __init__(self):
        super().__init__()
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

    async def get_filtered_user(self, user_id):
        result = self.collection.find_one({USER_ID_TAG: user_id}, {OBJECT_ID_TAG: 0})
        return result

    async def get_user(self, user_id):
        result = self.collection.find_one({USER_ID_TAG: user_id})
        return result

    async def update_user(self, user_id, user_data):
        result = self.collection.update_one({USER_ID_TAG: user_id}, {"$set": user_data})
        return {STATUS_TAG: result.acknowledged}
