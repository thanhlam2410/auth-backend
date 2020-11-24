from app import createApiApp
from app.models import db
from config import Config
import os

rootDir = os.path.abspath(os.path.dirname(__file__))


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(rootDir, "test.db")
    JWT_SECRET_KEY = "Abc@1234"


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
