"""

Routes For User Model

Route Map:

/user-management
/user-management/create
/user-management/edit-user/<id>
/user-management/edit-user/save
/user-management/delete/<id>


"""

from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from models.user import User
from models.harvest import Harvest
from utils.db import db
user = Blueprint('user', __name__)



# User Settings
@user.route('/user-settings')
def user_settings():
    if( not verify_permissions(session, User, 'all') ):
        return redirect(url_for('auth.index'))
    status = ""
    if ("management-status" in session):
        status = session['management-status']
        session.pop("management-status", None)
    return render_template('user-settings.html', rol = session['rol'], status=status)

# User Reset Password
@user.route("/user-settings/update-password", methods=["POST"])
def update_password():
    if( not verify_permissions(session, User, 'all') ):
        return redirect(url_for('auth.index'))
    username = session['username']
    old_password = request.form['old_password']
    if( User.verify_password( User , username, old_password ) ):
        new_password = request.form['new_password']
        id = session['user_id']
        user = User.query.get(id)
        user.set_password(new_password)
        db.session.add(user)
        db.session.commit()
        session['management-status'] = "Password Updated"
    else:
        session['management-status'] = "Incorrect Password"



    return redirect(url_for("user.user_settings"))


# Show Users
@user.route('/user-management')
def user_management():    
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))

    rols = User_rol.query.all()
    users = User.query.all()
    harvests = Harvest.query.all()
    if 'management-status' not in session:
        return render_template('user-management.html', status="",\
            rol = session['rol'], rols = rols, users = users,  harvests = harvests)
    status = session['management-status']
    session.pop('management-status', None)  
    return render_template('user-management.html', status=status, \
        rol = session['rol'], rols=rols, users = users, harvests = harvests )
    
# Create User
@user.route('/user-management/create', methods = ['POST'])
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
    F_Harvest = request.form['harvest_id']
    
    # Verify if correct respons 
    if( not valid_name(name) ):
        session["management-status"] = "Invalid Name"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_name(last_name) ):
        session["management-status"] = "Invalid Last Name"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_username(username) ):
        session["management-status"] = "Invalid Username"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_email(email) ):
        session["management-status"] = "Invalid Email"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_password(password) ):
        session["management-status"] = "Invalid Password"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_gender(gender) ):
        session["management-status"] = "Invalid Gender"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_date(date_of_birth) ):
        session["management-status"] = "Invalid Date"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_address(address) ):
        session["management-status"] = "Invalid Address"
        return redirect(url_for( 'user.user_management'))
    elif ( not valid_user_rol(user_rol_desc) ):
        session["management-status"] = "Invalid User Rol"
        return redirect(url_for( 'user.user_management'))
    elif ( not valid_harvest(F_Harvest) ):
        session["management-status"] = "Invalid Harvest"
        return redirect(url_for( 'user.user_management'))


    # Create New User
    new_user = User(name, last_name, username, email, password, gender, date_of_birth, phone, address, user_rol_desc, F_Harvest)
    db.session.add(new_user)
    db.session.commit()
    session['management-status'] = "Created"
    
    return redirect(url_for( 'user.user_management'))

# Edit User
@user.route('/user-management/edit-user/<id>')
def edit_user(id):
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    user = User.query.get(id)
    rols = User_rol.query.all()
    harvests = Harvest.query.all()
    return render_template("user-management-edit-user.html", user = user, \
        rol = session['rol'], rols=rols, harvests=harvests)

# Save Edition User
@user.route('/user-management/edit-user/save', methods = ["POST"])
def update_user():

    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))

    if( not valid_name(request.form["name"]) ):
        session["management-status"] = "Invalid Name"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_name(request.form["last_name"]) ):
        session["management-status"] = "Invalid Last Name"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_username(request.form["username"], True) ):
        session["management-status"] = "Invalid Username"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_email(request.form["email"]) ):
        session["management-status"] = "Invalid Email"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_password(request.form["password"]) ):
        session["management-status"] = "Invalid Password"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_gender(request.form["gender"]) ):
        session["management-status"] = "Invalid Gender"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_date(request.form["date_of_birth"]) ):
        session["management-status"] = "Invalid Date"
        return redirect(url_for( 'user.user_management'))
    elif( not valid_address(request.form["address"]) ):
        session["management-status"] = "Invalid Address"
        return redirect(url_for( 'user.user_management'))
    elif ( not valid_user_rol(request.form["user_rol"]) ):
        session["management-status"] = "Invalid User Rol"
        return redirect(url_for( 'user.user_management'))
    elif ( not valid_harvest(F_Harvest) ):
        session["management-status"] = "Invalid Harvest"
        return redirect(url_for( 'user.user_management'))

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
    user.F_Harvest = request.form['harvest_id']



    db.session.commit()
    session['management-status'] = "User Updated"
    return redirect(url_for('user.user_management'))

# Delete User by id
@user.route('/user-management/delete/<id>')
def delete_user(id):
    if( not verify_permissions(session, User) ):
        return redirect(url_for('auth.index'))
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    session['management-status'] = "User Deleted"
    return redirect(url_for('user.user_management'))
