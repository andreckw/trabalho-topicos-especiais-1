from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 's3nh4Tr4b4lh0Pyth0n@1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_manager.db'

db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'