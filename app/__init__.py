from flask import Flask, jsonify
from app.auth import authModule
from werkzeug import exceptions
from app.handle_error import (handleNotFoundError, handleNotImplementedError,
                              handleMethodNotAllowedError, handleGenericError)
from app.models import initApp as initAuthModels
from config import Config


def createApiApp():
    print(Config)

    app = Flask(__name__)
    app.config.from_object(Config)

    initAuthModels(app)

    # add routing
    app.register_blueprint(authModule, url_prefix="/auth")

    # add error handler
    app.register_error_handler(exceptions.NotFound, handleNotFoundError)
    app.register_error_handler(
        exceptions.NotImplemented, handleNotImplementedError)
    app.register_error_handler(
        exceptions.MethodNotAllowed, handleMethodNotAllowedError)
    app.register_error_handler(
        Exception, handleGenericError)

    return app
