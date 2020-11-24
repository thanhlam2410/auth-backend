from flask import Blueprint
import os

jwtSecret = os.environ.get("JWT_SECRET_KEY")
authModule = Blueprint("auth", __name__)
