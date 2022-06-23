import re
from models.user_rol import User_rol
from models.productor import Productor
from models.productor_type import Productor_type
from models.user import User


def valid_name(name):
    pat = "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"
    return re.fullmatch(pat, name)

def valid_username(username):
    pat = "^[A-Za-z]\\w{3,29}$"
    return re.fullmatch(pat, username)

def valid_email(email):
    pat = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    return re.fullmatch(pat, email)

def valid_password(password):
    #pat = "/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&#:])[A-Za-z\d$@$!%*?&#:]{8,15}/"
    #return re.fullmatch(pat, password)
    return True

def valid_gender(gender):
    return gender in [ "male", "female", 'other' ]

def valid_date(date):
    pat1 = "^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[0-2])([\-/.])\d{4}$"
    pat2 = "^(?:0?[1-9]|1[0-2])([\-/.])(3[01]|[12][0-9]|0?[1-9])([\-/.])\d{4}$"
    pat3 = "^\d{4}([\-/.])(0?[1-9]|1[0-2])([\-/.])(3[01]|[12][0-9]|0?[1-9])$"

    return re.fullmatch(pat1, date) or re.fullmatch(pat2, date) or re.fullmatch(pat3, date)

def valid_address(address):
    return True

def valid_user_rol(user_rol_desc):
    query = User_rol.query.all()
    rols = []
    for x in query:
        rols.append(x.description)
    return user_rol_desc in rols

def verify_permissions(session, User, rol=['admin']):
# Verify Permissions       
    return 'username' in session and \
    User.get_user_rol_by_username(User, session['username']) in rol

def valid_cedula(cedula):
    registers = Productor.query.filter_by(cedula=cedula)
    pat = "^([VE])(-)(\d{8})$"

    return len(register)==0

def valid_productor_type(productor_type_description):
    query = Productor_type.query.all()
    types = []
    for x in query:
        types.append(x.description)
    return productor_type_description in types