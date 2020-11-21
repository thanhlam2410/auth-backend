from app.models import db, migrate


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
