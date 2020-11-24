from flask import Blueprint, request
import os

jwtSecret = os.environ.get("JWT_SECRET_KEY")
profileModule = Blueprint("profile", __name__)
