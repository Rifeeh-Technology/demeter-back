from flask_lambda import FlaskLambda
from flask import request

app = FlaskLambda(__name__)


@app.route("/user", methods=["GET"])
def post_user():
    header = {
        'Content-Type': 'application/json',
    }
    body = {"mensage" : "hello user"}
    return body, 200, header