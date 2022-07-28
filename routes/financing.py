from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from utils.db import db
from datetime import datetime

financing = Blueprint('financing', __name__)
allowed_rols = ['admin', 'shopping-analyst']

@financing.route('/harvest/<harvest_id>/financing', methods=['GET'])
def index(harvest_id):
        harvest = Harvest.find(Harvest, harvest_id)
        return render_template('financing.html', rol = session['rol'], harvest = harvest)

