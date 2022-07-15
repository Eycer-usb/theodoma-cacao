"""
Routes for Productor Model

Routes map

/productor-data
/productor-data/search/<query>
/productor-data/create
/productor-data/delete/<id>
/productor-data/edit-productor/<id>
/productor-data/edit-productor/save

"""

from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User
from utils.db import db
from utils.functions import *

productor_route = Blueprint('productor_route', __name__)
allowed_rols = ['admin', 'shopping-analyst']

@productor_route.route('/productor-data')
def productor():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    productor_types = Productor_type.query.all()
    productors = Productor.query.all()
    if 'management-status' not in session:
        return render_template('productor-data.html', status="",\
            productor_types = productor_types, productors = productors)
    status = session['management-status']
    session.pop('management-status', None)  
    return render_template('productor-data.html', status=status, \
            productor_types = productor_types, productors = productors)

@productor_route.route('/productor-data/search/<query>')
def productor_search(query):
    pass


@productor_route.route('/productor-data/create', methods = ['POST'])
def productor_create():

    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    cedula = request.form['cedula']
    name = request.form['name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    date_of_birth = request.form['date_of_birth']
    local_phone = request.form['local_phone']
    movil_phone = request.form['movil_phone']
    address_1 = request.form['address_1']
    address_2 = request.form['address_2']
    productor_type_description = request.form['productor_type']

    if( not valid_cedula(cedula) ):
        session['management-status'] = "Invalid Cedula"
        return redirect(url_for( 'productor_route.productor'))
    elif( not valid_name(name) ):
        session["management-status"] = "Invalid Name"
        return redirect(url_for( 'productor_route.productor'))
    elif( not valid_name(last_name) ):
        session["management-status"] = "Invalid Last Name"
        return redirect(url_for( 'productor_route.productor'))
    elif( not valid_gender(gender) ):
        session["management-status"] = "Invalid Gender"
        return redirect(url_for( 'productor_route.productor'))
    elif( not valid_date(date_of_birth) ):
        session["management-status"] = "Invalid Date"
        return redirect(url_for( 'productor_route.productor'))
    elif ( not valid_productor_type( productor_type_description ) ):
        session["management-status"] = "Invalid Productor type"
        return redirect(url_for( 'productor_route.productor'))

    ## Create Productor
    new_productor = Productor(cedula, name, last_name,\
        gender, date_of_birth, local_phone, movil_phone, address_1,\
        address_2, productor_type_description)
    db.session.add(new_productor)
    db.session.commit()
    session['management-status'] = "Created"
    
    return redirect(url_for( 'productor_route.productor'))

@productor_route.route('/productor-data/delete/<id>')
def productor_delete(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    productor = Productor.query.get(id)
    db.session.delete(productor)
    db.session.commit()
    session['management-status'] = "Productor Deleted"
    return redirect(url_for('productor_route.productor'))

@productor_route.route('/productor-data/edit-productor/<id>')
def edit_productor(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    productor = Productor.query.get(id)
    types = Productor_type.query.all()
    return render_template("productor-data-edit-productor.html", productor = productor, \
        productor_types=types)


@productor_route.route('/productor-data/edit-productor/save', methods = ['POST'])
def productor_update():

    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    cedula = request.form['cedula']
    name = request.form['name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    date_of_birth = request.form['date_of_birth']
    local_phone = request.form['local_phone']
    movil_phone = request.form['movil_phone']
    address_1 = request.form['address_1']
    address_2 = request.form['address_2']
    productor_type_description = request.form['productor_type']

    if( not valid_cedula(cedula, True) ):
        session['management-status'] = "Invalid Cedula"
        return redirect(url_for( 'productor_route.productor'))
    elif( not valid_name(name) ):
        session["management-status"] = "Invalid Name"
    elif( not valid_date(date_of_birth) ):
        session["management-status"] = "Invalid Date"
        return redirect(url_for( 'productor_route.productor'))
    elif ( not valid_productor_type( productor_type_description ) ):
        session["management-status"] = "Invalid Productor type"
        return redirect(url_for( 'productor_route.productor'))

    id = request.form['id']
    productor = Productor.query.get(id)
    productor.cedula = cedula
    productor.name = name
    productor.last_name = last_name
    productor.gender = gender
    productor.date_of_birth = date_of_birth
    productor.local_phone = local_phone
    productor.movil_phone = movil_phone
    productor.address_1 = address_1
    productor.address_2 = address_2
    productor.productor_type_id = Productor_type.getId(productor_type_description)
    db.session.commit()
    session['management-status'] = "Productor Updated"
    return redirect(url_for('productor_route.productor'))
    