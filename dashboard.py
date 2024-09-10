from flask import redirect, render_template, url_for
from flask_login import current_user

from models import *


def view_dashboard():
    tarefas = {
        'pendente': Tarefa.query.filter_by(status=Status.pendente, user_id=current_user.id).all(),
        'em_andamento': Tarefa.query.filter_by(status=Status.em_andamento, user_id=current_user.id).all(),
        'concluido': Tarefa.query.filter_by(status=Status.concluido, user_id=current_user.id).all()
    }
    
    return render_template('dashboard/dashboard.html',tarefas=tarefas)