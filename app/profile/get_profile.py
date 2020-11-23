from app.profile import profileModule
from werkzeug import exceptions
from flask import request
from app.decorators.token_required import token_required


@profileModule.route('/me', methods=['GET'])
@token_required("jwtSecret")
def getMyProfile():
    print(request)
    raise exceptions.NotImplemented("API is under construction")
