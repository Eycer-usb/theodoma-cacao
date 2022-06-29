from this import s
from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from models.user import User
user = Blueprint('user', __name__)

@user.route('/user-settings')
def user_settings():
    if( not verify_permissions(session, User, 'all') ):
        return redirect(url_for('auth.index'))
    return render_template('user-settings.html', rol = session['rol'])
