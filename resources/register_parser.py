from constant import *
from sanic import exceptions


class RegisterParser:

    def __init__(self):
        self.data = {}

    def get_parse(self, request):
        self.data[USER_ID_LOCAL_TAG] = request.args.get(USER_ID_TAG)
        if not self.data[USER_ID_LOCAL_TAG]:
            raise exceptions.InvalidUsage(f"User Id not present in request")
        return self.data

    def post_parse(self, request):
        self.data[USER_DATA_LOCAL_TAG] = request.json
        if not self.data[USER_DATA_LOCAL_TAG]:
            raise exceptions.InvalidUsage(f"User Data not present in request")
        self.data[USER_ID_LOCAL_TAG] = request.json.get(USER_ID_TAG)
        return self.data
