from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

db = SQLAlchemy()
migrate = Migrate()
seeder = FlaskSeeder()
