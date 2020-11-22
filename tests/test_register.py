
#!/usr/bin/env python
import unittest
import sys
import os

from config import Config
from app import createApiApp
from app.models import db, Country
import json
rootDir = os.path.abspath(os.path.dirname(__file__))


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(rootDir, 'test.db')


def setupTestEnvironment(test):
    app = createApiApp(TestConfig)
    test.app_context = app.app_context()
    test.app_context.push()
    db.create_all()
    return app


def destroyTestEnvironment(test):
    db.session.remove()
    db.drop_all()
    test.app_context.pop()


def seedData():
    country = Country(code='VN', name='Viet Nam')
    db.session.add(country)
    db.session.commit()


class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.flaskApp = setupTestEnvironment(self)
        seedData()
        self.client = self.flaskApp.test_client()

    def tearDown(self):
        destroyTestEnvironment(self)

    def postRegister(self, email, password, firstName, lastName, country):
        return self.client.post(
            '/auth/register',
            data=json.dumps(dict(email=email, password=password,
                                 firstName=firstName, lastName=lastName, country=country)),
            content_type='application/json'
        )

    def test_register(self):
        response = self.postRegister(
            'lamttt@mailnesia.com', 'test password', 'lam', 'tran', 'VN')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data, b'{"email":"lamttt@mailnesia.com","firstName":"lam","id":1,"lastName":"tran"}\n')
