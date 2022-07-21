"""
Routes for Productor Type

Routes map

/productor-type
/productor-type/create
/productor-type/delete/<id>
/productor-type/search/<query>
/productor-type/edit-type/<id>
/productor-type/edit-type/save


"""

from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User
from utils.db import db
from utils.functions import *

productor_type_route = Blueprint('productor_type_route', __name__)
allowed_rols = ['admin', 'shopping-analyst']

@productor_type_route.route('/productor-type')
def productor_type():

    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )
    
    productor_types = Productor_type.query.all()
    if 'management-status' not in session:
        return render_template('productor-type.html', status="",\
            productor_types = productor_types)
    status = session['management-status']
    session.pop('management-status', None)
    return render_template('productor-type.html', status = status,\
            productor_types = productor_types)

@productor_type_route.route('/productor-type/create', methods= ['POST'])
def productor_type_create():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )
    
    description = request.form['description']
    price = float(request.form['price'])
    if ( price <= 0 ):
        return redirect(url_for("productor_type_route.productor_type"))
    new_rol = Productor_type(description, price)
    db.session.add(new_rol)
    db.session.commit()
    session['management-status'] = "Productor Type Created"
    return redirect(url_for( 'productor_type_route.productor_type' ))


@productor_type_route.route('/productor-type/search/<query>')
def productor_type_search():
    pass



@productor_type_route.route('/productor-type/delete/<id>')
def productor_type_delete(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    productor_type = Productor_type.query.get(id)
    db.session.delete(productor_type)
    db.session.commit()
    session['management-status'] = "Productor Type Deleted"
    return redirect(url_for('productor_type_route.productor_type'))

@productor_type_route.route('/productor-type/edit-type/<id>')
def productor_type_edit(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    productor_type = Productor_type.query.get(id)
    return render_template("productor-type-edit-type.html", types = productor_type)

@productor_type_route.route('/productor-type/edit-type/save', methods=['POST'])
def productor_type_update():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    id = request.form['id']
    types = Productor_type.query.get(id)
    types.description = request.form['description']
    types.price_percentage = float(request.form['price_percentage'])
    if ( types.price_percentage <= 0 ):
        return redirect(url_for("productor_type_route.productor_type"))

    db.session.commit()
    session['management-status'] = "Updated"
    return redirect(url_for('productor_type_route.productor_type'))
