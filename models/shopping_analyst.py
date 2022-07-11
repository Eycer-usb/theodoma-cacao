from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User
from models.shp_data import Shopping_data
from utils.db import db
from utils.functions import *

shp_analyst = Blueprint('shp_analyst', __name__)
allowed_rols = ['admin', 'shopping-analyst']
@shp_analyst.route('/productor-data')
def productor():
    if( not verify_permissions(session, User, allowed_rols) ):
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
    new_productor = Productor(cedula, name, last_name,\
        gender, date_of_birth, local_phone, movil_phone, address_1,\
        address_2, productor_type_description)
    db.session.add(new_productor)
    db.session.commit()
    session['management-status'] = "Created"
    
    return redirect(url_for( 'shp_analyst.productor'))

@shp_analyst.route('/productor-data/delete/<id>')
def productor_delete(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    productor = Productor.query.get(id)
    db.session.delete(productor)
    db.session.commit()
    session['management-status'] = "Productor Deleted"
    return redirect(url_for('shp_analyst.productor'))

@shp_analyst.route('/productor-data/edit-productor/<id>')
def edit_productor(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    productor = Productor.query.get(id)
    types = Productor_type.query.all()
    return render_template("productor-data-edit-productor.html", productor = productor, \
        rol = session['rol'], productor_types=types)


@shp_analyst.route('/productor-data/edit-productor/save', methods = ['POST'])
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
        return redirect(url_for( 'shp_analyst.productor'))
    elif( not valid_name(name) ):
        session["management-status"] = "Invalid Name"
    elif( not valid_date(date_of_birth) ):
        session["management-status"] = "Invalid Date"
        return redirect(url_for( 'shp_analyst.productor'))
    elif ( not valid_productor_type( productor_type_description ) ):
        session["management-status"] = "Invalid Productor type"
        return redirect(url_for( 'shp_analyst.productor'))

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
    return redirect(url_for('shp_analyst.productor'))
    
######################################

@shp_analyst.route('/productor-type')
def productor_type():

    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )
    
    productor_types = Productor_type.query.all()
    if 'management-status' not in session:
        return render_template('productor-type.html', status="",\
            rol = session['rol'], productor_types = productor_types)
    status = session['management-status']
    session.pop('management-status', None)
    return render_template('productor-type.html', status = status,\
            rol = session['rol'], productor_types = productor_types)

@shp_analyst.route('/productor-type/create', methods= ['POST'])
def productor_type_create():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )
    
    description = request.form['description']
    price = request.form['price']
    new_rol = Productor_type(description, price)
    db.session.add(new_rol)
    db.session.commit()
    session['management-status'] = "Productor Type Created"
    return redirect(url_for( 'shp_analyst.productor_type' ))

@shp_analyst.route('/productor-type/search/<query>')
def productor_type_search():
    pass

@shp_analyst.route('/productor-type/delete/<id>')
def productor_type_delete(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    productor_type = Productor_type.query.get(id)
    db.session.delete(productor_type)
    db.session.commit()
    session['management-status'] = "Productor Type Deleted"
    return redirect(url_for('shp_analyst.productor_type'))

@shp_analyst.route('/productor-type/edit-type/<id>')
def productor_type_edit(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    productor_type = Productor_type.query.get(id)
    return render_template("productor-type-edit-type.html", type = productor_type, \
        rol = session['rol'])

@shp_analyst.route('/productor-type/edit-type/save', methods=['POST'])
def productor_type_update():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    id = request.form['id']
    type = Productor_type.query.get(id)
    type.description = request.form['description']
    type.price = request.form['price']
    db.session.commit()
    session['management-status'] = "Updated"
    return redirect(url_for('shp_analyst.productor_type'))

############################################################################################

@shp_analyst.route('/user_shopping')
def user_shopp():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    shp_data = Shopping_data.query.all()
    tips_product = Productor_type.query.all()    
    if 'management-status' not in session:
        return render_template('user_shopping.html', status="",\
            rol = session['rol'], shp_data = shp_data, tips_product = tips_product)
    status = session['management-status']
    session.pop('management-status', None)
    return render_template('user_shopping.html', status = status,\
            rol = session['rol'], shp_data = shp_data, tips_product = tips_product)


    
@shp_analyst.route('/shoppings/create', methods= ['POST'])
def user_shopp_create():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )

    fecha = request.form['fecha']
    cedula = request.form['cedula']
    tip_productor = request.form['productor_type']
    clase= request.form['clase']
    price = request.form['price']
    cant= request.form['cant']
    humed= request.form['humed']
    merma= request.form['merma']
    mermakg= request.form['mermakg']
    cantot= request.form['cantot']
    monto= request.form['monto']

    if( not valid_date(fecha) ):
        session["management-status"] = "Invalid Date"
        return redirect(url_for( 'shp_analyst.user_shopp'))
    if( not valid_cedula(cedula) ):
        session['management-status'] = "Invalid Cedula"
        return redirect(url_for( 'shp_analyst.user_shopp'))

    new_shopping = Shopping_data(fecha, cedula, tip_productor, clase, price, cant, humed, merma, mermakg, cantot, monto)
    db.session.add(new_shopping)
    db.session.commit()
    session['management-status'] = "Shoppings Created"
    return redirect(url_for( 'shp_analyst.user_shopp' ))

@shp_analyst.route('/shoppings/edit/<id>')
def user_shopp_edit(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    shp_data = Shopping_data.query.get(id)
    tips_product = Productor_type.query.all()    
    return render_template("user_shopping-edit.html", editing_shopping = shp_data,\
        rol = session['rol'], tips_product = tips_product)

@shp_analyst.route("/shoppings/edit/save", methods = ['POST'])
def user_shopp_update():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    id = request.form['id']
    editing_shopping = Shopping_data.query.get(id)
    editing_shopping.fecha = request.form['fecha']
    editing_shopping.cedula = request.form['cedula']
    editing_shopping.tip_productor = request.form['productor_type']
    editing_shopping.clase= request.form['clase']
    editing_shopping.price = request.form['price']
    editing_shopping.cant= request.form['cant']
    editing_shopping.humed= request.form['humed']
    editing_shopping.merma= request.form['merma']
    editing_shopping.mermakg= request.form['mermakg']
    editing_shopping.cantot= request.form['cantot']
    editing_shopping.monto= request.form['monto']

    db.session.commit()
    session['management-status'] = "Shopping Updated"
    return redirect(url_for('shp_analyst.user_shopp'))

@shp_analyst.route('/shopp/delete/<id>')
def user_shop_delete(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    shp_data = Shopping_data.query.get(id)
    db.session.delete(shp_data)
    db.session.commit()
    session['management-status'] = "Compra Eliminada"
    return redirect(url_for('shp_analyst.user_shopp'))