from flask.json import jsonify
from app.auth import authModule
from app.models import db
from app.decorators import token_required


@authModule.route("/logout", methods=["POST"])
@token_required()
def doLogout(user, session):
    print(user, session)
    session.invalidateSession()
    db.session.commit()
    return jsonify({"success": True})
