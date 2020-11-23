from flask import jsonify, request
import jwt
from app.models import ClientAccount


def token_required(jwtSecret):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print((jwtSecret))
            token = None
            if 'authorization' in request.headers:
                token = request.headers['authorization']

            if not token:
                return jsonify({'message': 'Unauthorized'}), 401

            try:
                data = jwt.decode(token, jwtSecret)
                current_user = ClientAccount.query.filter_by(
                    id=data['userId']).first()
            except:
                return jsonify({'message': 'token is invalid'})

            return f(current_user, *args, **kwargs)

        return wrapper
    return decorator
