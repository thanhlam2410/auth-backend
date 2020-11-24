from flask import Flask, jsonify
from app.auth import authModule
from app.profile import profileModule
from werkzeug import exceptions
from app.handle_error import (
    handleNotFoundError,
    handleNotImplementedError,
    handleMethodNotAllowedError,
    handleGenericError,
    handleValidationError,
)
from app.models import initApp as initDbModel, db
from config import Config
from jsonschema import ValidationError

app: Flask


def createApiApp(appConfig=Config):
    app = Flask(__name__)
    app.config.from_object(appConfig)

    initDbModel(app)

    # add routing
    app.register_blueprint(authModule, url_prefix="/auth")
    app.register_blueprint(profileModule, url_prefix="/profile")

    # add error handler
    app.register_error_handler(ValidationError, handleValidationError)
    app.register_error_handler(exceptions.NotFound, handleNotFoundError)
    app.register_error_handler(exceptions.NotImplemented, handleNotImplementedError)
    app.register_error_handler(exceptions.MethodNotAllowed, handleMethodNotAllowedError)
    app.register_error_handler(Exception, handleGenericError)

    return app
