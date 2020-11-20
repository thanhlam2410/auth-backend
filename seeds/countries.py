from flask_seeder import Seeder, Faker
from app.models import Country
from config import Config


class CountrySeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    # run() will be called by Flask-Seeder
    def run(self):
        countries = [{"code": "VN", "name": "Viet Nam"},
                     {"code": "SG", "name": "Singapore"}]

        # Create a new Faker and tell it how to create Country objects
        index = 1
        for country in countries:
            print(country)
            faker = Faker(
                cls=Country,
                init={
                    "id": index,
                    "code": country['code'],
                    "name": country['name']
                }
            )

            payload = faker.create()
            self.db.session.add(payload[0])
            index += 1
