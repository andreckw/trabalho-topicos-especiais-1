from config import app, db
from models import User, Tarefa, CompartilharTarefa


with app.app_context():
    db.create_all()
