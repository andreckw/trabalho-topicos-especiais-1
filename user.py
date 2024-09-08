from flask import redirect, render_template, url_for
from flask_login import login_user
from models import User, db
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash


def register_form(registro: RegisterForm):
    
    if registro.validate_on_submit():
        username = registro.username.data
        password = generate_password_hash(registro.password.data)
        
        exist_user = User.query.filter_by(username=username).first()
        
        if not exist_user:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for("login"))

    return render_template("user/register.html", attr=registro)

def login_form(login: LoginForm):
    
    if login.validate_on_submit():
        username = login.username.data
        password = login.password.data
        
        user = User.query.filter_by(username=username).first()
        
        if user:
            if check_password_hash(user.password, password):
                
                login_user(user)
                
                return redirect(url_for("index"))

    return render_template("user/login.html", attr=login)
