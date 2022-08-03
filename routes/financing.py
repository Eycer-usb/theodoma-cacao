from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from utils.db import db
from models.financing import Financing
from datetime import datetime
from models.bank import Bank

financing = Blueprint('financing', __name__)
allowed_rols = ['admin', 'shopping-analyst', 'shopping-manager']

# Index page display all Harvest and create form
@financing.route('/harvestFinancing')
def harvestFinancing():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    harvests = Harvest.query.all()
    if ( 'management-status' in session ):
        status = session['management-status']
        session.pop('management-status', None)
        return render_template("harvestFinancing.html", harvests = harvests)
    return render_template("harvestFinancing.html", harvests = harvests)

@financing.route('/harvest/<harvest_id>/financingShow', methods=['GET'])
def financingShow(harvest_id):
        if( not verify_permissions(session, User, allowed_rols) ):
                return redirect(url_for('auth.index'))
        harvest = Harvest.find(Harvest, harvest_id)
        financing = Financing.query.filter_by(F_Harvest = harvest_id)
        productors = Productor.query.all()
        productor_types = Productor_type.query.all()

        if 'management-status' in session: status = session['management-status']
        return render_template("financingShow.html", harvest=harvest, financing = financing,
                productors=productors, productor_types= productor_types)


@financing.route('/harvest/<harvest_id>/financing', methods=['GET'])
def index(harvest_id):
        if( not verify_permissions(session, User, allowed_rols) ):
                return redirect(url_for('auth.index'))
        harvest = Harvest.find(Harvest, harvest_id)
        financing = Financing.query.filter_by(F_Harvest = harvest_id)
        productors = Productor.query.all()
        productor_types = Productor_type.query.all()

        if 'management-status' in session: status = session['management-status']
        return render_template("financing.html", harvest=harvest, financing = financing,
                productors=productors, productor_types= productor_types)

@financing.route('/harvest/<harvest_id>/financing/create', methods=["POST"])
def create(harvest_id):

    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )

    date = datetime.today().strftime('%Y-%m-%d')
    harvest_id = request.form['harvest-id']
    productor_id = request.form['productor-id']
    letter_number = int(request.form['letter_number'])
    expiration_date = request.form['expiration_date']
    amount = float(request.form['amount'])
    payment = request.form['payment']
    observations = request.form['observations']
    new_finance = Financing( date, productor_id, harvest_id, letter_number,
                            expiration_date, amount, payment, observations )
    db.session.add(new_finance)
    db.session.commit()
    session['management-status'] = "Financiamiento Creado"
    return redirect(url_for("financing.harvestFinancing"))


@financing.route('/harvest/<harvest_id>/financing/<financing_id>/edit', methods=["GET"])
def edit(harvest_id, financing_id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    financing = Financing.query.get(financing_id)
    productor_types = Productor_type.query.all()
    productors = Productor.query.all()
    harvest = Harvest.query.get(harvest_id)
    return render_template("financing-edit.html", financing = financing, productor_types=productor_types,
        productors=productors, harvest = harvest)


@financing.route('/harvest/<harvest_id>/financing/update', methods=["POST"])
def update(harvest_id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )
    id = request.form['id']
    financing = Financing.query.get(id)
    financing.date = request.form['date']
    financing.F_Harvest = request.form['harvest-id']
    financing.F_Productor = request.form['productor-id']
    financing.letter_number= request.form['letter_number']
    financing.expiration_date = request.form['expiration_date']
    financing.amount = float(request.form['amount'])
    financing.payment = request.form['payment']
    financing.observations = request.form['observations']
    db.session.add(financing)
    db.session.commit()
    session['management-status'] = "Financiamiento Editado"
    return redirect(url_for("financing.index", harvest_id = harvest_id))

@financing.route('/harvest/<harvest_id>/financing/<financing_id>/delete')
def delete(harvest_id, financing_id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    financing = Financing.query.get(financing_id)
    db.session.delete(financing)
    db.session.commit()
    session['management-status'] = "Compra Eliminada"
    return redirect(url_for("financing.index", harvest_id = harvest_id))
