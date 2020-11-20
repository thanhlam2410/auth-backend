from app.models.global_scope import db, migrate, seeder
from app.models.user_model import User
from app.models.client_account_model import ClientAccount, Country
from flask import Flask


def initApp(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)
