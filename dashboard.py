from flask import redirect, render_template, url_for
from models import *

def view_dashboard():
    
    return render_template('dashboard/dashboard.html')