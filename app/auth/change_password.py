from app.models import ClientAccount, db
from flask.json import jsonify
from app.auth import authModule
from flask import request
from .global_scope import jwtSecret
import jwt
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {"password": {"type": "string", "minLength": 8, "maxLength": 32}},
    "required": ["password"],
}


@authModule.route("/change-password", methods=["POST"])
def changePassword():
    input = request.get_json()
    validate(instance=input, schema=schema)

    data = verifyJWTToken(token=input["token"])

    if data is None:
        return jsonify({"error": "Invalid Token"}), 400

    user = ClientAccount.getUserById(userId=data["userId"])
    if user is None:
        return jsonify({"error": "Invalid User"}), 400

    user.changePassword(password=input["password"])
    db.session.commit()
    return jsonify({"success": True})


def verifyJWTToken(token: str):
    try:
        return jwt.decode(token, jwtSecret)
    except:
        return None