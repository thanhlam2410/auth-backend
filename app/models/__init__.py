from app.models.global_scope import db, migrate
from app.models.user_model import User
from flask import Flask


def initApp(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
