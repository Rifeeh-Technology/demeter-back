from flask_lambda import FlaskLambda
from flask import request
from service.create import execute

app = FlaskLambda(__name__)


@app.route("/property", methods=["POST"])
def post_property():
    return execute(request)
