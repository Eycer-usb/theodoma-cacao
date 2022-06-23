from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User
from utils.db import db
from utils.functions import *

shp_analyst = Blueprint('shp_analyst', __name__)

@shp_analyst.route('/productor-data')
def productor():
    if( not verify_permissions(session, User, ['admin', 'shopping analyst']) ):
        return redirect(url_for('auth.index'))

    productor_types = Productor_type.query.all()
    productors = Productor.query.all()
    if 'management-status' not in session:
        return render_template('productor-data.html', status="",\
            rol = session['rol'], productor_types = productor_types, productors = productors)
    status = session['management-status']
    session.pop('management-status', None)  
    return render_template('productor-data.html', status=status, \
            rol = session['rol'], productor_types = productor_types, productors = productors)

@shp_analyst.route('/productor-data/search/<query>')
def productor_search(query):
    pass


@shp_analyst.route('/productor-data/create', methods = ['POST'])
def productor_create():

    if( not verify_permissions(session, User, ['admin', 'shopping analyst']) ):
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
        return redirect(url_for( 'shp_analyst.productor'))
    elif( not valid_name(name) ):
        session["management-status"] = "Invalid Name"
        return redirect(url_for( 'shp_analyst.productor'))
    elif( not valid_name(last_name) ):
        session["management-status"] = "Invalid Last Name"
        return redirect(url_for( 'shp_analyst.productor'))
    elif( not valid_gender(gender) ):
        session["management-status"] = "Invalid Gender"
        return redirect(url_for( 'shp_analyst.productor'))
    elif( not valid_date(date_of_birth) ):
        session["management-status"] = "Invalid Date"
        return redirect(url_for( 'shp_analyst.productor'))
    elif ( not valid_productor_type( productor_type_description ) ):
        session["management-status"] = "Invalid Productor type"
        return redirect(url_for( 'shp_analyst.productor'))

    ## Create Productor
    new_productor = productor(cedula, name, last_name,\
        gender, date_of_birth, local_phone, movil_phone, address_1,\
        address_2, productor_type_description)
    db.session.add(new_productor)
    db.session.commit()
    session['management-status'] = "Created"
    
    return redirect(url_for( 'shp_analyst.productor'))


######################################

@shp_analyst.route('/productor-type')
def productor_type():
    return render_template('productor-type.html', rol = session['rol'])

@shp_analyst.route('/productor-type/search/<query>')
def productor_type_search():
    pass

