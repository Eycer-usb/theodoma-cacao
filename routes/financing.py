from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from utils.db import db
from models.financing import Financing
from datetime import datetime

financing = Blueprint('financing', __name__)
allowed_rols = ['admin', 'shopping-analyst']

@financing.route('/harvest/<harvest_id>/financing', methods=['GET'])
def index(harvest_id):
        if( not verify_permissions(session, User, allowed_rols) ):
                return redirect(url_for('auth.index'))
        harvest = Harvest.find(Harvest, harvest_id)
        financing = Financing.query.filter_by(F_Harvest = harvest_id)
        productors = Productor.query.all()
        productor_types = Productor_type.query.all()
        status = ""
        if 'management-status' in session: status = session['management-status']
        return render_template("financing.html", harvest=harvest, financing = financing,
                productors=productors, productor_types= productor_types, status=status)






