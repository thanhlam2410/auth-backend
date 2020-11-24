from app.models import db


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    sessionId = db.Column(db.String(128), index=True, unique=True)
    isValid = db.Column(db.Boolean)

    def __repr__(self):
        return "<Session {}>".format(self.id)

    def invalidateSession(userId):
        query = db.session.query(Session).filter(userId=userId, isValid=True)
        query.update({Session.isValid: False}, synchronize_session=False)
        db.session.commit()

    @staticmethod
    def findSession(sessionId):
        return Session.query.filter_by(sessionId=sessionId).first()

    @staticmethod
    def createSession(userId, sessionId):
        session = Session(
            userId=userId,
            sessionId=sessionId,
            isValid=True,
        )
        db.session.add(session)
        db.session.commit()
        return session