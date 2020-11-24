from app.auth import authModule
from werkzeug import exceptions


@authModule.route("/forgot-password", methods=["POST"])
def forgotPassword(user, session):
    raise exceptions.NotImplemented("API is under construction")
