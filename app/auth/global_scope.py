from flask import Blueprint, request
from werkzeug import exceptions
import os

jwtSecret = os.environ.get("JWT_SECRET_KEY")
authModule = Blueprint("auth", __name__)
