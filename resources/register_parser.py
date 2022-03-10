from constant import *


class RegisterParser:

    def __init__(self):
        self.data = {}

    def get_parse(self, request):
        self.data[USER_ID_LOCAL_TAG] = request.args.get(USER_ID_TAG)
        return self.data

    def post_parse(self, request):
        self.data[USER_DATA_LOCAL_TAG] = request.json
        self.data[USER_ID_LOCAL_TAG] = request.json.get(USER_ID_TAG) if self.data[USER_DATA_LOCAL_TAG] else None
        return self.data
