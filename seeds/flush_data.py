from app.models import User, Country
from flask_seeder import Seeder


class FlushData(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 0

    # run() will be called by Flask-Seeder
    def run(self):
        User.query.filter_by().delete()
        Country.query.filter_by().delete()
        self.db.session.commit()
