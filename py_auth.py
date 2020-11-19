from app import createApiApp
from config import Config

print(Config.SQLALCHEMY_DATABASE_URI)

app = createApiApp()
