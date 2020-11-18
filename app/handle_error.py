from flask import jsonify
from werkzeug import exceptions


def handleNotFoundError(err: exceptions.NotFound):
    print("got NotFound error", err)
    return 'Got Error', 404


def handleNotImplementedError(err: exceptions.NotImplemented):
    print("got NotImplemented error", err)
    return jsonify({"message": err.description}), err.code


def handleMethodNotAllowedError(err: exceptions.MethodNotAllowed):
    print("got MethodNotAllowed error", err)
    return jsonify({"message": err.description}), err.code


def handleGenericError(err):
    print("got error", err)
    return 'Got Error', 500
