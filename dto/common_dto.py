import pymongo
from bson import ObjectId

from constant import *


class CommonDTO:

    def __init__(self):
        self.client = pymongo.MongoClient(DB_BASIC_CONN_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[USER_COLLECTION]

    async def get_by_id(self, obj_id):
        return self.collection.find_one({OBJECT_ID_TAG: ObjectId(obj_id)})

    async def update_by_id(self, obj_id, data):
        pass
