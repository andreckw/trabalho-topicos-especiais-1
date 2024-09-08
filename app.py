from flask import *
from forms import *
from config import app
import user

@app.route("/")
def index():
    return render_template("home/index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    formulario = RegisterForm()
    
    return user.register_form(formulario)

@app.route("/login", methods=["GET", "POST"])
def login():
    login = LoginForm()
    
    return user.login_form(login)
        