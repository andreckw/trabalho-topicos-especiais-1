from flask import *
from flask_login import login_required, current_user
from forms import *
from config import app
from user import *
from dashboard import *


@app.route("/")
def index():
    return render_template("home/index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    formulario = RegisterForm()
    
    return register_form(formulario)


@app.route("/login", methods=["GET", "POST"])
def login():
    login = LoginForm()
    
    return login_form(login)


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    return logout_session()


@app.route("/tarefa/nova", methods=["GET", "POST"])
@login_required
def new_task():
    formulario = TaskForm()
    if formulario.validate_on_submit():
        titulo = formulario.titulo.data
        descricao = formulario.descricao.data
        status = formulario.status.data

        nova_tarefa = Tarefa(
            titulo=titulo,
            descricao=descricao,
            status=Status(status),
            user_id=current_user.id
        )
        db.session.add(nova_tarefa)
        db.session.commit()

        flash('Tarefa criada com sucesso!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('dashboard/new_task.html', form=formulario)


@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return view_dashboard()


@app.route("/tarefa/<int:task_id>/editar", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    tarefa = Tarefa.query.get_or_404(task_id)

    if tarefa.user_id != current_user.id:
        flash('Você não tem permissão para editar esta tarefa.', 'danger')
        return redirect(url_for('dashboard'))

    formulario = TaskForm(obj=tarefa)

    if formulario.validate_on_submit():
        tarefa.titulo = formulario.titulo.data
        tarefa.descricao = formulario.descricao.data
        tarefa.status = Status(formulario.status.data)
        
        if formulario.compartilhar.data:
            user_com = User.query.filter_by(username=formulario.compartilhar.data).first()
            
            if user_com:
                new_compartilhamento = CompartilharTarefa(
                    user_id=user_com.id, 
                    tarefa_id=task_id
                )
                db.session.add(new_compartilhamento)
        
        db.session.commit()
        flash('Tarefa atualizada com sucesso!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('dashboard/edit_task.html',tarefa=tarefa, form=formulario)


@app.route("/tarefa/excluir/<int:task_id>", methods=["POST"])
@login_required
def delete_task(task_id):
    tarefa = Tarefa.query.get_or_404(task_id)

    if tarefa.user_id != current_user.id:
        flash('Você não tem permissão para excluir esta tarefa.', 'danger')
        return redirect(url_for('dashboard'))

    db.session.delete(tarefa)
    db.session.commit()

    flash('Tarefa excluída com sucesso!', 'success')
    return redirect(url_for('dashboard'))
