from constant import *
from sanic import exceptions

from exceptions.exception_constants import ExceptionConstants


class RegisterParser:

    def __init__(self):
        self.data = {}

    def get_parse(self, request):
        self.data[USER_ID_LOCAL_TAG] = request.args.get(USER_ID_TAG)
        if not self.data[USER_ID_LOCAL_TAG]:
            raise exceptions.InvalidUsage(ExceptionConstants(USER_ID_LOCAL_TAG).not_present_in_request())
        return self.data

    def post_parse(self, request):
        self.data[USER_DATA_LOCAL_TAG] = request.json
        if not self.data[USER_DATA_LOCAL_TAG]:
            raise exceptions.InvalidUsage(ExceptionConstants(USER_DATA_LOCAL_TAG).not_present_in_request())
        self.data[USER_ID_LOCAL_TAG] = request.json.get(USER_ID_TAG)
        return self.data

    def patch_parse(self, request):
        self.data[USER_DATA_LOCAL_TAG] = request.json
        if not self.data[USER_DATA_LOCAL_TAG]:
            raise exceptions.InvalidUsage(ExceptionConstants(USER_DATA_LOCAL_TAG).not_present_in_request())
        self.data[USER_ID_LOCAL_TAG] = request.args.get(USER_ID_TAG)
        if not self.data[USER_ID_LOCAL_TAG]:
            raise exceptions.InvalidUsage(ExceptionConstants(USER_ID_LOCAL_TAG).not_present_in_request())
        return self.data
