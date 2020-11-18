from flask import Blueprint, request
from werkzeug import exceptions

authModule = Blueprint('auth', __name__)

# register routes


@authModule.route('/login', methods=['GET', 'POST'])
def doLogin():
    print(request)
    raise exceptions.NotImplemented("API is under construction")


@authModule.route('/logout', methods=['POST'])
def doLogout():
    raise exceptions.NotImplemented("API is under construction")
