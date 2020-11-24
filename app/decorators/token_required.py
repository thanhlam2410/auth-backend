from flask import jsonify, request
import jwt
from app.models import Session, ClientAccount


def token_required(jwtSecret):
    def decorator(f):
        def wrapper(*args, **kwargs):
            token = None

            if "Authorization" in request.headers:
                token = str(request.headers["Authorization"]).removeprefix("Bearer ")

            if token is None:
                return jsonify({"error": "Unauthorized"}), 401

            try:
                data = jwt.decode(token, jwtSecret)
                session = Session.query.filter_by(sessionId=data["sessionId"]).first()

                if session.isValid is False:
                    return jsonify({"error": "Unauthorized"}), 401

                user = ClientAccount.query.filter_by(id=data["userId"]).first()
                if user is None:
                    return jsonify({"error": "Unauthorized"}), 401

            except Exception as e:
                print(e)
                return jsonify({"error": "Unauthorized"}), 401

            return f(user, session, *args, **kwargs)

        return wrapper

    return decorator
