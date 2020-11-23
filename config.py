import os
from dotenv import load_dotenv

rootDir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(rootDir, 'db', 'auth_backend.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_PASSWORD = os.environ.get(
        'ADMIN_PASSWORD')
    JWT_SECRET_KEY = os.environ.get(
        'JWT_SECRET_KEY')
