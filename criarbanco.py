from config import app, db
from models import User, Tarefa


with app.app_context():
    db.create_all()