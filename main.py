from flask import *
from flask_login import login_required
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
def logout():
    return logout_session()

@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return view_dashboard()