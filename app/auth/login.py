from app.auth import authModule
from werkzeug import exceptions
from flask import request


@authModule.route('/login', methods=['POST'])
def doLogin():
    print(request)
    raise exceptions.NotImplemented("API is under construction")
