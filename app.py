from flask import *
from forms import *
import user

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home/index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    register = RegisterForm()
    
    user.register_form(register)
        