from flask_lambda import FlaskLambda
from flask import request
from service import create, restore

app = FlaskLambda(__name__)


@app.route("/property", methods=["POST"])
def post_property():
    return create.execute(request)


@app.route("/property", methods=["GET"])
def get_property():
    return "bunda mole"
