
#!/usr/bin/env python
import unittest
import sys
import os

from config import Config
from app import createApiApp
from app.models import db
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


class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.flaskApp = setupTestEnvironment(self)
        self.client = self.flaskApp.test_client()

    def tearDown(self):
        destroyTestEnvironment(self)

    def register(self, email, password):
        return self.client.post(
            '/auth/register',
            data=json.dumps(dict(email=email)),
            content_type='application/json'
        )

    def testRegister(self):
        response = self.register(
            'patkennedy79@gmail.com', 'FlaskIsAwesome')
        self.assertEqual(response.data, '')
        self.assertEqual(response.status_code, 200)
