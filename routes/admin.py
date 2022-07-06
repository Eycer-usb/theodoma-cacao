"""
Routes For the Administrator Rol

Route Map:

/user-rol-management
/user-rol-management/create
/user-rol-management/edit-rol/<id>
/user-rol-management/edit-rol/save", methods = ['POST']
/user-rol-management/delete/<id>

/user-management
/user-management/create
/user-management/edit-user/<id>
/user-management/edit-user/save
/user-management/delete/<id>
"""


from crypt import methods
from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User, User_rol
from models.user_harvest import User_harvest
from utils.db import db
from utils.functions import *
admin = Blueprint('admin', __name__)


"""
User Rol routes

"""

# Show Users Rols #####################################################################
@admin.route('/user-rol-management')
def user_rol_management():
    if( not verify_permissions(session, User) ):
        return redirect( url_for('auth.index') )
    
    rols = User_rol.query.all()
    if 'management-status' not in session:
        return render_template('user-rol-management.html', status="",\
            rol = session['rol'], rols = rols)
    status = session['management-status']
    session.pop('management-status', None)
    return render_template('user-rol-management.html', status = status,\
            rol = session['rol'], rols = rols)

# Create User Rol
@admin.route('/user-rol-management/create', methods = ['POST'])
def user_rol_create():
    if( not verify_permissions(session, User) ):
        return redirect( url_for('auth.index') )
    
    description = clean_string(request.form['description'])
    str_description = clean_string(request.form['str_description'])
    new_rol = User_rol(description,str_description)
    db.session.add(new_rol)
    db.session.commit()
    session['management-status'] = "Rol Created"
    return redirect(url_for( 'admin.user_rol_management' ))

# Edit User rol
@admin.route('/user-rol-management/edit-rol/<id>')
def edit_rol(id):
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    rol = User_rol.query.get(id)
    return render_template("user-rol-management-edit-rol.html", editing_rol = rol, \
        rol = session['rol'])

# Save Edition        
@admin.route("/user-rol-management/edit-rol/save", methods = ['POST'])
def update_user_rol():

    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    id = request.form['id']
    user_rol = User_rol.query.get(id)
    user_rol.str_description = request.form['str_description']
    user_rol.description = request.form['description']

    db.session.commit()
    session['management-status'] = "User Rol Updated"
    return redirect(url_for('admin.user_rol_management'))

# Delete User Rol by id
@admin.route('/user-rol-management/delete/<id>')
def delete_user_rol(id):
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    user_rol = User_rol.query.get(id)
    db.session.delete(user_rol)
    db.session.commit()
    session['management-status'] = "User Rol Deleted"
    return redirect(url_for('admin.user_rol_management'))

"""
User routes
"""
# Show Users #####################################################################
@admin.route('/user-management')
def user_management():    
    if( not verify_permissions(session, User) ):
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
    
# Create User
@admin.route('/user-management/create', methods = ['POST'])
def user_create():


    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))

    name = request.form['name']
    last_name = request.form['last_name']
    username = clean_string(request.form['username'])
    email = request.form['email']
    password = request.form['password']
    gender = request.form['gender']
    date_of_birth = request.form['date_of_birth']
    phone = request.form['phone']
    address = request.form['address']
    user_rol_desc = request.form['user_rol']
    
    # Verify if correct respons 
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

    # Create New User
    new_user = User(name, last_name, username, email, password, gender, date_of_birth, phone, address, user_rol_desc)
    db.session.add(new_user)
    db.session.commit()
    session['management-status'] = "Created"
    
    return redirect(url_for( 'admin.user_management'))

# Edit User 
@admin.route('/user-management/edit-user/<id>')
def edit_user(id):
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    user = User.query.get(id)
    rols = User_rol.query.all()
    return render_template("user-management-edit-user.html", user = user, \
        rol = session['rol'], rols=rols)

# Save Edition User
@admin.route('/user-management/edit-user/save', methods = ["POST"])
def update_user():

    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))

    if( not valid_name(request.form["name"]) ):
        session["management-status"] = "Invalid Name"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_name(request.form["last_name"]) ):
        session["management-status"] = "Invalid Last Name"
        return redirect(url_for( 'admin.user_management'))
    elif( not valid_username(request.form["username"], True) ):
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

# Delete User by id
@admin.route('/user-management/delete/<id>')
def delete_user(id):
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    session['management-status'] = "User Deleted"
    return redirect(url_for('admin.user_management'))


# Show users harvest #####################################################################
@admin.route('/user-harvest')
def user_harvest_management():
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))

    harvest = User_harvest.query.all()
    if 'management-status' not in session:
        return render_template('user-harvest.html', status="",\
            rol = session['rol'], harvest = harvest)

    status = session['management-status']
    session.pop('management-status', None)
    return render_template('user-harvest.html', status = status,\
            rol = session['rol'], harvest = harvest)

@admin.route('/user-harvest/create', methods = ['POST'])
def user_harvest_create():
    if( not verify_permissions(session, User) ):
        return redirect( url_for('auth.index') )
    description = request.form['description']
    start_date = request.form['start_date']
    ended_date = request.form['ended_date']
    new_harvest = User_harvest(description,start_date,ended_date)
    db.session.add(new_harvest)
    db.session.commit()
    session['management-status'] = "harvest Created"
    return redirect(url_for( 'admin.user_harvest_management' ))
