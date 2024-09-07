from flask import redirect, render_template, url_for
from models import User, db
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash


def register_form(registro: RegisterForm):
    username = registro.username.data
    password = generate_password_hash(registro.password.data)
    
    exist_user = User.query(username=username).first()
    
    if not exist_user:
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for("login"))

    return render_template("register.html", formulario=registro)
