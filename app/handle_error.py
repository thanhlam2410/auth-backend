from flask import jsonify
from werkzeug import exceptions


def handleNotFoundError(err: exceptions.NotFound):
    print("got NotFound error", err)
    return jsonify({"error": "Not Found"}), 404


def handleNotImplementedError(err: exceptions.NotImplemented):
    print("got NotImplemented error", err)
    return jsonify({"error": err.description}), err.code


def handleMethodNotAllowedError(err: exceptions.MethodNotAllowed):
    print("got MethodNotAllowed error", err)
    return jsonify({"error": err.description}), err.code


def handleGenericError(err):
    print("got error", err.message)
    return err, 500


def handleValidationError(err):
    return jsonify({"error": err.message}), 400
