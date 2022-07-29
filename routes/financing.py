from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from utils.db import db
from models.financing import Financing
from datetime import datetime

financing = Blueprint('financing', __name__)
allowed_rols = ['admin', 'shopping-analyst']

@financing.route('/harvest/<harvest_id>/financing', methods=['GET'])
def index(harvest_id):
        if( not verify_permissions(session, User, allowed_rols) ):
                return redirect(url_for('auth.index'))
        harvest = Harvest.find(Harvest, harvest_id)
        financing = Financing.query.filter_by(F_Harvest = harvest_id)
        productors = Productor.query.all()
        productor_types = Productor_type.query.all()
        status = ""
        if 'management-status' in session: status = session['management-status']
        return render_template("financing.html", harvest=harvest, financing = financing,
                productors=productors, productor_types= productor_types, status=status)

@financing.route('/harvest/<harvest_id>/financing/create', methods=["POST"])
def create(harvest_id):

    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )

    date = datetime.today().strftime('%Y-%m-%d')
    harvest_id = request.form['harvest-id']
    productor_id = request.form['productor-id']
    letter_number = request.form['letter_number']
    expiration_date = request.form['expiration_date']
    amount = float(request.form['amount'])
    payment = request.form['payment']
    observations = request.form['observations']
    new_finance = Financing(date=date, F_Productor=productor_id,\
        F_Harvest=harvest_id, letter_number=letter_number, expiration_date=expiration_date,\
            amount=amount, payment=payment, observations = observations)

    harvest = Harvest.query.get(harvest_id)
    if harvest.status == 'active':
        db.session.add(new_finance)
        db.session.commit()
        session['management-status'] = "Compra Creada"
    else:
        session['management-status'] = "Cosecha Cerrada"
    return redirect(url_for("harvest_route.index"))
