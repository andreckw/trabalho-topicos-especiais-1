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
