import jwt
import uuid
from .global_scope import jwtSecret


def generateUUID():
    return str(uuid.uuid4())


def generateJWTToken(userId, sessionId, expire):
    return jwt.encode(
        {"userId": userId, "sessionId": sessionId, "exp": expire},
        jwtSecret,
        algorithm="HS256",
    ).decode("utf-8")
