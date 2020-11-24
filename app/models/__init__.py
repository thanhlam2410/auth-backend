from app.models.global_scope import db, migrate, seeder
from .user_model import User
from .client_account_model import ClientAccount
from .country_model import Country
from .session import Session


def initApp(app):
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)
