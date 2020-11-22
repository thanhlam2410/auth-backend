from app.models import db, migrate
from werkzeug.security import generate_password_hash


class ClientAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(256), nullable=True)
    phone = db.Column(db.String(30), nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

    def __repr__(self):
        return '<ClientAccount {}>'.format(self.email)

    def toDict(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }

    @staticmethod
    def createClientUser(email, password, firstName, lastName, countryId):
        clientAccount = ClientAccount(email=email, password_hash=generate_password_hash(password), first_name=firstName, last_name=lastName, country_id=countryId)
        db.session.add(clientAccount)
        db.session.commit()
        return clientAccount