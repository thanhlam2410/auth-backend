import datetime
from app.models import Session
from .global_scope import authModule
from flask import request, jsonify, current_app
from app.models import ClientAccount
from .helper import generateJWTToken, generateUUID
from jsonschema import validate

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
    validate(instance=input, schema=schema)

    user = ClientAccount.query.filter_by(email=input["email"]).first()

    if user is None:
        return jsonify({"error": "email and password does not match"}), 400

    isValid = user.checkPassword(input["password"])

    if isValid is False:
        return jsonify({"error": "email and password does not match"}), 400

    Session.revokeAllToken(user.id)

    sessionId = generateUUID()
    accessToken = generateJWTToken(
        user.id,
        sessionId=sessionId,
        expire=datetime.datetime.utcnow() + datetime.timedelta(days=1),
        jwtSecret=current_app.config.get("JWT_SECRET_KEY"),
    )
    Session.createSession(userId=user.id, sessionId=sessionId)

    # return "OK"
    return jsonify({"accessToken": accessToken})
