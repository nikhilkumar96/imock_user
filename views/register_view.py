import json as json1
from sanic.response import json
from sanic.views import HTTPMethodView

from resources.register_parser import RegisterParser
from controllers.register_controller import RegisterController


class RegisterView(HTTPMethodView):

    async def get(self, request):
        response = "invalid"
        return json(json1.loads(response))

    async def post(self, request):
        parser = RegisterParser().parse(request)
        response = await RegisterController(parser['user_id'], parser['user_data']).save_data()
        return json(response)

    async def patch(self, request):
        response = "invalid"
        return json(response)
