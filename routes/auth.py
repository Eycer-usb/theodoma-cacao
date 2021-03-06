from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User
from utils.functions import clean_string

auth = Blueprint('auth', __name__)

@auth.route('/')
def index():
    if( 'username' in session and 'rol' in session):
        return render_template('home.html', rol = session['rol'])
    elif( 'login_status' in session ):
        login_status = session['login_status']
        session.pop('login_status', None)
        return render_template('login.html', login_status = login_status)
    return render_template('login.html')

@auth.route('/login',  methods=['GET', 'POST'])
def login():

    if( request.method == 'POST' and \
        'username' in request.form and \
        'password' in request.form):

        username = clean_string(request.form['username'])
        password = request.form['password']
        if( not User.is_user(username) ): 
            session['login_status'] = 'User Not Found'
            return redirect(url_for('auth.index'))
        if( User.verify_password( User , username, password ) ):
            session['username'] = username
            session['user_id'] = User.getId(User, username)
            session['rol'] = User.get_user_rol_by_username(User, username)
            return redirect(url_for('auth.index'))
        session['login_status'] = 'Incorrect Password'
        return redirect(url_for('auth.index'))

    return redirect(url_for('auth.index'))

@auth.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('rol', None)
    return redirect(url_for('auth.index'))
