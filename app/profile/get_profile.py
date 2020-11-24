from flask.json import jsonify
from app.profile import profileModule
from werkzeug import exceptions
from flask import request
from app.decorators.token_required import token_required


@profileModule.route("/me", methods=["GET"])
@token_required()
def getMyProfile(user, session):
    print(request, user, session)
    return jsonify(user.toDict())
