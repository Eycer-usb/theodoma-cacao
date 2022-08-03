from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from utils.db import db
from models.bank import Bank
from datetime import datetime

bank = Blueprint('bank', __name__)
allowed_rols = ['admin', 'shopping-analyst', 'shopping-manager']

@bank.route('/bank')
def index():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    banks = Bank.query.all()

    total_cantidad = sum(bank.amount for bank in banks)

    if 'management-status' not in session:
        return render_template('bank.html', status="",\
            banks = banks, total_cantidad=total_cantidad)
    status = session['management-status']
    session.pop('management-status', None)
    return render_template("bank.html", banks=banks, total_cantidad=total_cantidad)

@bank.route('/bank/add-credit', methods=['POST'])
def add():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    try:
        amount = float(request.form['amount'])
        if amount > 0:
            session['management-status'] = "Credito Agregado"
            date = datetime.today().strftime('%Y-%m-%d')
            time = datetime.now().strftime("%H:%M:%S")
            new = Bank(amount, date, time, "Credito para Compras (+)", amount)
            db.session.add(new)
            db.session.commit()
        else:
            session['management-status'] = "Monto debe ser Mayor que cero"
    except:
        session['management-status'] = "Error en los datos suministrados"

    return redirect(url_for("bank.index"))