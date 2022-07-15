"""
Routes For the User Rol Model

Route Map:

/user-rol-management
/user-rol-management/create
/user-rol-management/edit-rol/<id>
/user-rol-management/edit-rol/save", methods = ['POST']
/user-rol-management/delete/<id>


"""


from crypt import methods
from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User, User_rol
from utils.db import db
from utils.functions import *
user_rol = Blueprint('user_rol', __name__)


"""
User Rol routes

"""

# Show Users Rol
@user_rol.route('/user-rol-management')
def user_rol_management():
    if( not verify_permissions(session, User) ):
        return redirect( url_for('auth.index') )
    
    rols = User_rol.query.all()
    if 'management-status' not in session:
        return render_template('user-rol-management.html', status="",\
            rols = rols)
    status = session['management-status']
    session.pop('management-status', None)
    return render_template('user-rol-management.html', status = status,\
            rols = rols)

# Create User Rol
@user_rol.route('/user-rol-management/create', methods = ['POST'])
def user_rol_create():
    if( not verify_permissions(session, User) ):
        return redirect( url_for('auth.index') )
    
    description = clean_string(request.form['description'])
    str_description = clean_string(request.form['str_description'])
    new_rol = User_rol(description,str_description)
    db.session.add(new_rol)
    db.session.commit()
    session['management-status'] = "Rol Created"
    return redirect(url_for( 'user_rol.user_rol_management' ))

# Edit User rol
@user_rol.route('/user-rol-management/edit-rol/<id>')
def edit_rol(id):
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    rol = User_rol.query.get(id)
    return render_template("user-rol-management-edit-rol.html", editing_rol = rol)

# Save Edition        
@user_rol.route("/user-rol-management/edit-rol/save", methods = ['POST'])
def update_user_rol():

    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    id = request.form['id']
    user_rol = User_rol.query.get(id)
    user_rol.str_description = request.form['str_description']
    user_rol.description = request.form['description']

    db.session.commit()
    session['management-status'] = "User Rol Updated"
    return redirect(url_for('user_rol.user_rol_management'))

# Delete User Rol by id
@user_rol.route('/user-rol-management/delete/<id>')
def delete_user_rol(id):
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    user_rol = User_rol.query.get(id)
    db.session.delete(user_rol)
    db.session.commit()
    session['management-status'] = "User Rol Deleted"
    return redirect(url_for('user_rol.user_rol_management'))

