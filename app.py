from sanic import Sanic
from sanic_motor import BaseModel

from constant import *

app = Sanic(SERVICENAME)

settings = dict(
    MOTOR_URI=DB_CONN_URI,
    LOGO=None,
)
app.config.update(settings)

BaseModel.init_app(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
