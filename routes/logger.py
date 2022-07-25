from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.db import db
from utils.functions import *
from models.logger import Logger

logg = Blueprint('logger', __name__)
allowed_rols = ['admin']

@logg.route('/logger')
def index():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    registers = Logger.query.all()

    if 'management-status' not in session:
        return render_template('logger.html', status="",\
            registers = registers)
    status = session['management-status']
    session.pop('management-status', None)
    return render_template("logger.html", registers=registers)



@logg.route('/logger/delete/<id>')
def logger_delete(id):
    print("esta accediendo?")
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    registers= Logger.query.get(id)
    db.session.delete(registers)
    db.session.commit()
    session['management-status'] = "Evento Eliminado"
    return redirect(url_for('logger.index'))


