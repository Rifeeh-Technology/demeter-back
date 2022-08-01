from flask_lambda import FlaskLambda
from flask import request
from service import create, restore, update

app = FlaskLambda(__name__)


@app.route("/property", methods=["POST"])
def post_property():
    return create.execute(request)


@app.route("/property", methods=["GET"])
def get_property():
    return restore.execute(request)


@app.route("/property", methods=["PUT"])
def update_property():
    return update.execute(request)
