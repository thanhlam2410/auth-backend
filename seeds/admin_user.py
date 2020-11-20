from flask_seeder import Seeder, Faker, generator
from app.models import User
from werkzeug.security import generate_password_hash
from config import Config


class AdminUserSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    # run() will be called by Flask-Seeder
    def run(self):

        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=User,
            init={
                "id": generator.Sequence(),
                "email": "lamttt@mailnesia.com",
                "password_hash": generate_password_hash(Config.ADMIN_PASSWORD)
            }
        )

        payload = faker.create()
        print(payload)
        self.db.session.add(payload[0])
