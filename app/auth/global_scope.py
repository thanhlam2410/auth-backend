from flask import Blueprint, request
from werkzeug import exceptions

authModule = Blueprint('auth', __name__)
