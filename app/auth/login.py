from app.models import Session
from .global_scope import authModule, jwtSecret
from flask import request, jsonify
from app.models import ClientAccount
import jwt
import uuid

schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string", "minLength": 8, "maxLength": 32},
    },
    "required": [
        "email",
        "password",
    ],
}


@authModule.route("/login", methods=["POST"])
def doLogin():
    input = request.get_json()
    user = ClientAccount.query.filter_by(email=input["email"]).first()

    if user is None:
        return jsonify({"error": "email and password does not match"}), 400

    isValid = user.checkPassword(input["password"])

    if isValid is False:
        return jsonify({"error": "email and password does not match"}), 400

    sessionId = generateUUID()
    accessToken = generateJWTToken(user.id, sessionId=sessionId)
    Session.createSession(userId=user.id, sessionId=sessionId)

    # return "OK"
    return jsonify({"accessToken": accessToken})


def generateJWTToken(userId, sessionId):
    return jwt.encode(
        {"userId": userId, "sessionId": sessionId}, jwtSecret, algorithm="HS256"
    ).decode("utf-8")


def generateUUID():
    return str(uuid.uuid4())
