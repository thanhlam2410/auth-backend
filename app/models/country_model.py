from app.models import db, migrate


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), index=True, unique=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return '<Country {}>'.format(self.id)

    @staticmethod
    def getCountryFromCode(code):
        return Country.query.filter_by(code=code).first()
