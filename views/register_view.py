from sanic.response import json
from sanic.views import HTTPMethodView

from constant import *
from resources.register_parser import RegisterParser
from controllers.register_controller import RegisterController


class RegisterView(HTTPMethodView):

    async def get(self, request):
        parser = RegisterParser().get_parse(request)
        response = await RegisterController(parser[USER_ID_LOCAL_TAG], None).get_user_data()
        return json(response)

    async def post(self, request):
        parser = RegisterParser().post_parse(request)
        response = await RegisterController(parser[USER_ID_LOCAL_TAG], parser[USER_DATA_LOCAL_TAG]).save_data()
        return json(response)

    async def patch(self, request):
        parser = RegisterParser().patch_parse(request)
        response = await RegisterController(parser[USER_ID_LOCAL_TAG], parser[USER_DATA_LOCAL_TAG]).update_user_data()
        return json(response)
