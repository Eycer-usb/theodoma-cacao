from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from utils.db import db
from models.bank import Bank
from datetime import datetime

bank = Blueprint('bank', __name__)
allowed_rols = ['admin', 'shopping-analyst']

@bank.route('/bank')
def index():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    banks = Bank.query.all()

    if 'management-status' not in session:
        return render_template('bank.html', status="",\
            banks = banks)
    status = session['management-status']
    session.pop('management-status', None)
    return render_template("bank.html", banks=banks)