from sanic import Blueprint

from constant import *
from views.register_view import RegisterView

API_VERSION = 'v1'


def setup_api(app):
    api_prefix = f'/{SERVICENAME.lower()}/{API_VERSION}'
    api_v1 = Blueprint(API_VERSION, url_prefix=api_prefix)

    api_v1.add_route(RegisterView.as_view(), '/register', strict_slashes=False)
    app.blueprint(api_v1)
