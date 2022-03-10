import pymongo
from bson import ObjectId

from constant import *


class RegisterDTO:

    def __init__(self):
        self.client = pymongo.MongoClient(DB_BASIC_CONN_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[USER_COLLECTION]

    async def add_user(self, data):
        data['_id'] = ObjectId()
        save = self.collection.insert_one(data)
        return {"status": save.acknowledged, "value": str(save.inserted_id)}
