from app.auth.helper import generateJWTToken, generateUUID
from app.auth import authModule
from flask import request, jsonify, current_app
from app.models import ClientAccount
import datetime
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {"email": {"type": "string", "format": "email"}},
    "required": ["email"],
}


@authModule.route("/forgot-password", methods=["POST"])
def forgotPassword():
    input = request.get_json()
    validate(instance=input, schema=schema)

    user = ClientAccount.query.filter_by(email=input["email"]).first()

    if user is None:
        return jsonify({"error": "Invalid Email"}), 400

    sessionId = generateUUID()
    token = generateJWTToken(
        userId=user.id,
        sessionId=sessionId,
        expire=datetime.datetime.utcnow() + datetime.timedelta(seconds=300),
        jwtSecret=current_app.config.get("JWT_SECRET_KEY"),
    )

    sendResetPasswordEmail(token=token)
    return jsonify({"success": True})


def sendResetPasswordEmail(token: str):
    # Integrate with smtp server
    print("Send Email: " + token)