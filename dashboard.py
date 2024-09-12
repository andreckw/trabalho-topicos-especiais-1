from flask import redirect, render_template, url_for
from flask_login import current_user

from models import *


def view_dashboard():
    pendentes =  Tarefa.query.filter_by(status=Status.pendente, user_id=current_user.id).all()
    andamento = Tarefa.query.filter_by(status=Status.em_andamento, user_id=current_user.id).all()
    concluido = Tarefa.query.filter_by(status=Status.concluido, user_id=current_user.id).all()
    
    tarefas_com = CompartilharTarefa.query.filter_by(user_id=current_user.id).all()
    for task in tarefas_com:
        com_task = Tarefa.query.filter_by(id=task.tarefa_id).all()

        if com_task[0].status == Status.pendente:
            pendentes.extend(com_task)
        elif com_task[0].status == Status.em_andamento:
            andamento.extend(com_task)
        else:
            concluido.extend(com_task)
    
    tarefas = {
        'pendente': pendentes,
        'em_andamento': andamento,
        'concluido': concluido
    }
    
    return render_template('dashboard/dashboard.html',tarefas=tarefas, current_user=current_user)