from app.auth import authModule
from werkzeug import exceptions


@authModule.route("/change-password", methods=["POST"])
def changePassword(user, session):
    raise exceptions.NotImplemented("API is under construction")