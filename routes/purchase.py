"""

Routes For Purchase Model

Route Map:

/harvest/id/purchase

"""


from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from utils.db import db
from models.purchase import Purchase
purchase = Blueprint('purchase', __name__)
allowed_rols = ['admin', 'shopping-analyst']

@purchase.route('/harvest/<harvest_id>/purchase')
def index(harvest_id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    harvest = Harvest.find(Harvest, harvest_id)
    purchases = Purchase.query.filter_by(F_Harvest = harvest_id)
    render_template("purchase.html", harvest=harvest, purchases=purchases)

@purchase.route('/harvest/<harvest_id>/purchase/create', method=["POST"])
def create(harvest_id):
    return redirect(url_for("purchase.index"))

@purchase.route('/harvest/<harvest_id>/purchase/<purchase_id>/edit', method=["GET"])
def edit(harvest_id):
    pass

@purchase.route('/harvest/<harvest_id>/purchase/update', method=["POST"])
def update(harvest_id):
    pass

@purchase.route('/harvest/<harvest_id>/purchase/<purchase_id>/delete')
def delete(harvest_id):
    pass



