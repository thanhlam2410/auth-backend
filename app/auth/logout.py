from app.auth import authModule
from werkzeug import exceptions
from flask import request


@authModule.route('/logout', methods=['POST'])
def doLogout():
    raise exceptions.NotImplemented("API is under construction")
