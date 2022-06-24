"""
Function Library

Here are the validators functions
and utility functions

"""


import re
from models.user_rol import User_rol
from models.productor import Productor
from models.productor_type import Productor_type
from models.user import User

# Standar String Name and Lastname validator
def valid_name(name):
    pat = "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"
    return re.fullmatch(pat, name)

# Verify if a username string is correct or not 
# if is already register in the database return false 
# except when the update parameter is set True
def valid_username(username, update=False):
    is_register = False
    if( not update ):
        is_register =  User.query.filter_by(username=username).first() == None
    pat = "^[A-Za-z]\\w{3,29}$"
    return re.fullmatch(pat, username) and not is_register

# Verify a email string
def valid_email(email):
    pat = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    return re.fullmatch(pat, email)

# No restrictions needed yet for password
def valid_password(password):
    #pat = "/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&#:])[A-Za-z\d$@$!%*?&#:]{8,15}/"
    #return re.fullmatch(pat, password)
    return True

# Only exist two gender, if not agree you have the other option
def valid_gender(gender):
    return gender in [ "male", "female", 'other' ]

# Verify a date string in 3 differents formats
def valid_date(date):
    pat1 = "^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[0-2])([\-/.])\d{4}$"
    pat2 = "^(?:0?[1-9]|1[0-2])([\-/.])(3[01]|[12][0-9]|0?[1-9])([\-/.])\d{4}$"
    pat3 = "^\d{4}([\-/.])(0?[1-9]|1[0-2])([\-/.])(3[01]|[12][0-9]|0?[1-9])$"

    return re.fullmatch(pat1, date) or re.fullmatch(pat2, date) or re.fullmatch(pat3, date)

# No restriction needed for address yet
def valid_address(address):
    return True

# Verify if a user rol string is correct or not 
# if is not register in the database return false 
def valid_user_rol(user_rol_desc):
    query = User_rol.query.all()
    rols = []
    for x in query:
        rols.append(x.description)
    return user_rol_desc in rols

# Verify Permissions   
def verify_permissions(session, User, allowed=['admin']):    
    return 'username' in session and \
    ( allowed == 'all' or User.get_user_rol_by_username(User, session['username']) in allowed)

def valid_cedula(cedula, update=False):
    is_register = False
    if( not update ):
        is_register =  Productor.query.filter_by(cedula=cedula).first() == None or update
    pat = "^[VE]-\d{6,7}$"
    return re.fullmatch(pat, cedula) and not is_register

def valid_productor_type(productor_type_description):
    query = Productor_type.query.all()
    types = []
    for x in query:
        types.append(x.description)
    return productor_type_description in types


def clean_string(string):
    return string.strip()
