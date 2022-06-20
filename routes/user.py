from flask import Blueprint, render_template, redirect, url_for, request, session

user = Blueprint('user', __name__)

@user.route('/user-settings')
def user_settings():
    return render_template('user-settings.html', rol = session['rol'])