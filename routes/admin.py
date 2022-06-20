from crypt import methods
from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User, User_rol
from utils.db import db
from utils.functions import *
admin = Blueprint('admin', __name__)


def verify_permissions():
    # Verify Permissions       
    return 'username' in session and \
        User.get_user_rol_by_username(User, session['username']) == 'admin'


@admin.route('/user-management')
def user_management():    
    if( not verify_permissions() ):
        return redirect(url_for('auth.index'))

    rols = User_rol.query.all()
    users = User.query.all()
    if 'management-status' not in session:
        return render_template('user-management.html', status="",\
            rol = session['rol'], rols = rols, users = users)
    status = session['management-status']
    session.pop('management-status', None)  
    return render_template('user-management.html', status=status, \
        rol = session['rol'], rols=rols, users = users )
    

@admin.route('/user-management/create', methods = ['POST'])
def user_create():

    # db.session.add(User_rol("admin"))
    # db.session.add(User_rol("user"))
    # db.session.commit()
    if( not verify_permissions() ):
        return redirect(url_for('auth.index'))

    name = request.form['name']
    last_name = request.form['last_name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    gender = request.form['gender']
    date_of_birth = request.form['date_of_birth']
    phone = request.form['phone']
    address = request.form['address']
    user_rol_desc = request.form['user_rol']

    if( not valid_name(name) ):
        session["management-status"] = "Invalid Name"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_name(last_name) ):
        session["management-status"] = "Invalid Last Name"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_username(username) ):
        session["management-status"] = "Invalid Username"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_email(email) ):
        session["management-status"] = "Invalid Email"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_password(password) ):
        session["management-status"] = "Invalid Password"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_gender(gender) ):
        session["management-status"] = "Invalid Gender"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_date(date_of_birth) ):
        session["management-status"] = "Invalid Date"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_address(address) ):
        session["management-status"] = "Invalid Address"
        return redirect(url_for( 'admin.user_management'))
    elif ( not valid_user_rol(user_rol_desc) ):
        session["management-status"] = "Invalid User Rol"
        return redirect(url_for( 'admin.user_management'))

    ## Create User
    new_user = User(name, last_name, username, email, password, gender, date_of_birth, phone, address, user_rol_desc)
    db.session.add(new_user)
    db.session.commit()
    session['management-status'] = "Created"
    
    return redirect(url_for( 'admin.user_management'))

@admin.route('/user-management/edit-user/<id>')
def edit_user(id):
    if( not verify_permissions() ):
        return redirect(url_for('auth.index'))
    user = User.query.get(id)
    rols = User_rol.query.all()
    return render_template("user-management-edit-user.html", user = user, \
        rol = session['rol'], rols=rols)

@admin.route('/user-management/edit-user/save', methods = ["POST"])
def update_user():

    if( not verify_permissions() ):
        return redirect(url_for('auth.index'))

    if( not valid_name(request.form["name"]) ):
        session["management-status"] = "Invalid Name"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_name(request.form["last_name"]) ):
        session["management-status"] = "Invalid Last Name"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_username(request.form["username"]) ):
        session["management-status"] = "Invalid Username"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_email(request.form["email"]) ):
        session["management-status"] = "Invalid Email"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_password(request.form["password"]) ):
        session["management-status"] = "Invalid Password"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_gender(request.form["gender"]) ):
        session["management-status"] = "Invalid Gender"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_date(request.form["date_of_birth"]) ):
        session["management-status"] = "Invalid Date"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_address(request.form["address"]) ):
        session["management-status"] = "Invalid Address"
        return redirect(url_for( 'admin.user_management'))
    elif ( not valid_user_rol(request.form["user_rol"]) ):
        session["management-status"] = "Invalid User Rol"
        return redirect(url_for( 'admin.user_management'))

    id = request.form['id']
    user = User.query.get(id)
    user.name = request.form['name']
    user.last_name = request.form['last_name']
    user.username = request.form['username']
    user.email = request.form['email']
    user.phone = request.form['phone']
    user.date_of_birth = request.form['date_of_birth']
    user.address = request.form['address']
    user.gender = request.form['gender']
    user.user_rol = request.form['user_rol']
    user.set_password(request.form['password'])


    db.session.commit()
    session['management-status'] = "User Updated"
    return redirect(url_for('admin.user_management'))

@admin.route('/user-management/delete/<id>')
def delete_user(id):
    if( not verify_permissions() ):
        return redirect(url_for('auth.index'))
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    session['management-status'] = "User Deleted"
    return redirect(url_for('admin.user_management'))