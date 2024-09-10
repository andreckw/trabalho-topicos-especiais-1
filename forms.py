from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4)])
    password = StringField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Registrar")
    

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class TaskForm(FlaskForm):
    titulo = StringField('Título da Tarefa', validators=[DataRequired()])
    descricao = TextAreaField('Descrição')
    status = SelectField('Status', choices=[('pendente', 'Pendente'), ('em_andamento', 'Em Andamento'), ('concluido', 'Concluído')])
    submit = SubmitField('Criar Tarefa')