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
from models.harvest import Harvest
from models.logger import Logger
from models.purchase import Purchase


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
        is_register =  User.query.filter_by(username=username).first() != None
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
    return gender in [ "Masculino", "Femenino", 'Otro' ]

# Verify a date string in 3 differents formats
def valid_date(date):
    pat1 = "^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[0-2])([\-/.])\d{4}$"
    pat2 = "^(?:0?[1-9]|1[0-2])([\-/.])(3[01]|[12][0-9]|0?[1-9])([\-/.])\d{4}$"
    pat3 = "^\d{4}([\-/.])(0?[1-9]|1[0-2])([\-/.])(3[01]|[12][0-9]|0?[1-9])$"

    return re.fullmatch(pat1, date) or re.fullmatch(pat2, date) or re.fullmatch(pat3, date)

def valid_ended(start_date, end_date):
    if (end_date > start_date): 
        return end_date
    else: 
        print("fecha invalida")

def valid_date_purchase(start_date, end_date, date):
    if (start_date >= date >= start_date):
        return date
    else: 
        print("fecha fuera de rangos")

# No restriction needed for address yet
def valid_address(address):
    return True

# Verify Permissions   
def verify_permissions(session, User, allowed=['admin']):    
    return 'username' in session and \
    ( allowed == 'all' or User.get_user_rol_by_username(User, session['username']) in allowed)

# A valid cedula example is V-1234567 or E-1234567
def valid_cedula(cedula, update=False):
    is_register = False
    if( not update ):
        is_register =  Productor.query.filter_by(cedula=cedula).first() != None
    pat = "^[VE]-\d{8}$"
    return re.fullmatch(pat, cedula) and not is_register

#------------------------User Rol-----------------------------------------

# Verify if a user rol string is correct or not 
# if is not register in the database return false 
def valid_user_rol(user_rol_desc):
    query = User_rol.query.all()
    rols = []
    for x in query:
        rols.append(x.description)
    return user_rol_desc in rols

#------------------------ProductorType-----------------------------------------
# Verify if a productor type string is correct or not 
# if is not register in the database return false
def valid_productor_type(productor_type_description):
    query = Productor_type.query.all()
    types = []
    for x in query:
        types.append(x.description)
    return productor_type_description in types

#------------------------Productor-----------------------------------------
def valid_productor(product):
    query = Productor.query.all()
    productor = []
    for x in query:
        productor.append(x.name)
    return product in productor

#------------------------User-----------------------------------------
def valid_user(user_name):
    query = User.query.all()
    users = []
    for x in query:
        users.append(x.name)
    return user_name in users


#------------------------Harvest-----------------------------------------
# Verify if a given description corresponds to a valid harvest
def valid_harvest(harvest_id):
    query = Harvest.query.get(harvest_id)
    return query != None

def validate_harvest(harvest_description):
    query = Harvest.query.all()
    harvests = []
    for x in query:
        harvests.append(x.description)
    return harvest_description in harvests

# Verify valid harvest status
def valid_harvest_status(status):
    return ( status in ['active', 'closed'] )



#------------------------Event-----------------------------------------
def valid_event(event):
    query = Logger.query.all()
    events = []
    for x in query:
        events.append(x.event)
    return event in events

def valid_event_module(event):
    query = Logger.query.all()
    events = []
    for x in query:
        events.append(x.module)
    return event in events

#------------------------Purchase-----------------------------------------
def valid_purchase(shopp):
    query = Purchase.query.all()
    purch = []
    for x in query:
        purch.append(x.cacao_type)
    return shopp in purch

def valid_purchase_produc(shopp):
    query = Purchase.query.all()
    purch = []
    for x in query:
        purch.append(x.F_Productor)
    return shopp in purch

def valid_purchase_harvest(shopp):
    query = Purchase.query.all()
    purch = []
    for x in query:
        purch.append(x.F_Harvest)
    return shopp in purch

# Clean the empty side spacing
def clean_string(string):
    return string.strip()
