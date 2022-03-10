from sanic.response import json
import json as json1
from sanic.views import HTTPMethodView


class RegisterView(HTTPMethodView):

    async def get(self, request):
        response = "invalid"
        return json(json1.loads(response))

    async def post(self, request):
        response = "invalid"
        return json(response)

    async def patch(self, request):
        response = "invalid"
        return json(response)
