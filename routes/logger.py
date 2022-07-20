from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from models.logger import Logger
app = Blueprint('logger', __name__)
allowed_rols = ['admin']

@app.route('/logger')
def index():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    registers = Logger.query.all()
    return render_template("logger.html", registers=registers)