from flask import Flask, jsonify
from app.auth import authModule
from werkzeug import exceptions
from app.handle_error import (handleNotFoundError, handleNotImplementedError,
                              handleMethodNotAllowedError, handleGenericError)


def createApiApp():
    app = Flask(__name__)
    app.register_blueprint(authModule, url_prefix="/auth")

    app.register_error_handler(exceptions.NotFound, handleNotFoundError)
    app.register_error_handler(
        exceptions.NotImplemented, handleNotImplementedError)
    app.register_error_handler(
        exceptions.MethodNotAllowed, handleMethodNotAllowedError)
    app.register_error_handler(
        Exception, handleGenericError)

    return app
