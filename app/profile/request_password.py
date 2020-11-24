from app.profile import profileModule
from werkzeug import exceptions
from flask import request
from app.decorators.token_required import token_required
from .global_scope import jwtSecret


@profileModule.route("/password", methods=["PUT"])
@token_required(jwtSecret)
def getMyProfile(user, session):
    print(request, user, session)
    raise exceptions.NotImplemented("API is under construction")
