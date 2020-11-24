from flask.json import jsonify
from app.auth import authModule
from app.models import db
from werkzeug import exceptions
from flask import request
from app.decorators import token_required
from .global_scope import jwtSecret


@authModule.route("/logout", methods=["POST"])
@token_required(jwtSecret)
def doLogout(user, session):
    print(user, session)
    session.invalidateSession()
    db.session.commit()
    return jsonify({"success": True})
