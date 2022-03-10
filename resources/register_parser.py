from constant import *


class RegisterParser:

    def __init__(self):
        self.data = {}

    def parse(self, request):
        self.data['user_data'] = request.json
        self.data['user_id'] = request.json.get(USER_ID_TAG) if self.data['user_data'] else None
        return self.data
