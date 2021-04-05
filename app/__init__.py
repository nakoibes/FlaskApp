from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

app = Flask(__name__)
login = LoginManager(app)
db = SQLAlchemy(app)
app.config.from_object(Config)
migrate = Migrate(app, db)
login.login_view = 'login'

from app import routes, forms, models
