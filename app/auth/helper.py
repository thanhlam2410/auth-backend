import jwt
import uuid


def generateUUID():
    return str(uuid.uuid4())


def generateJWTToken(userId, sessionId, expire, jwtSecret):
    return jwt.encode(
        {"userId": userId, "sessionId": sessionId, "exp": expire},
        jwtSecret,
        algorithm="HS256",
    ).decode("utf-8")
