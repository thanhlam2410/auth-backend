from app import createApiApp
from app.models import db, Country
from config import Config
import os
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
