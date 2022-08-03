from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User
from models.harvest import Harvest
from utils.db import db
from utils.functions import *

harvest_route = Blueprint('harvest_route', __name__)
allowed_rols = ['admin', 'shopping-analyst', 'shopping-manager']

# Index page display all Harvest and create form
@harvest_route.route('/harvest')
def index():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    harvests = Harvest.query.all()
    productors = Productor.query.all()
    if ( 'management-status' in session ):
        status = session['management-status']
        session.pop('management-status', None)
        return render_template("harvest.html",\
        status = status,\
        harvests = harvests, productors=productors )
    return render_template("harvest.html",\
        status = "",\
        harvests = harvests, productors=productors )

@harvest_route.route('/harvest-show')
def showIndex():
    if( not verify_permissions(session, User, allowed_rols + ['shopping-analyst']) ):
        return redirect(url_for('auth.index'))
    harvests = Harvest.query.all()
    productors = Productor.query.all()
    if ( 'management-status' in session ):
        status = session['management-status']
        session.pop('management-status', None)
        return render_template("show-harvest.html",\
        status = status,\
        harvests = harvests, productors=productors )
    return render_template("show-harvest.html",\
        status = "",\
        harvests = harvests, productors=productors )

# Add a new Harvest to the Database
@harvest_route.route('/harvest/create', methods= ['POST'])
def create():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    description = request.form['description']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    status = request.form['status']


    if( not valid_date(start_date) ):
        session['management-status'] = "Invalid Start Date"
        return redirect(url_for('harvest_route.index'))
    elif (not valid_date(end_date)):
        session['management-status'] = "Invalid End Date"
        return redirect(url_for('harvest_route.index'))
    elif (not valid_harvest_status(status) ):
        session['management-status'] = "Invalid harvest status"
        return redirect(url_for('harvest_route.index'))
    elif (not valid_ended(start_date, end_date)): 
        session['management-status'] = "Invalid Date"
        return redirect(url_for('harvest_route.index'))


    new_harvest = Harvest(description, start_date, end_date, status)
    db.session.add(new_harvest)
    db.session.commit()
    session['management-status'] = "Created"
    return redirect( url_for('harvest_route.index') )

# Edit Harvest to the Database
@harvest_route.route('/harvest/edit/<id>')
def edit(id):

    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    
    harvest = Harvest.find(Harvest,id)
    return render_template("harvest-edit.html",\
        harvest = harvest )

    
# Update Harvest to the Database
@harvest_route.route('/harvest/update', methods=['POST'])
def update():
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    id = request.form['id']
    description = request.form['description']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    status = request.form['status']


    if( not valid_date(start_date) ):
        session['management-status'] = "Invalid Start Date"
        return redirect(url_for('harvest_route.index'))
    elif (not valid_date(end_date)):
        session['management-status'] = "Invalid End Date"
        return redirect(url_for('harvest_route.index'))
    elif (not valid_harvest_status(status) ):
        session['management-status'] = "Invalid harvest status"
        return redirect(url_for('harvest_route.index'))
    elif (not valid_ended(start_date, end_date)): 
        session['management-status'] = "Invalid Date"
        return redirect(url_for('harvest_route.index'))

    harvest = Harvest.find(Harvest,id)
    harvest.description = description
    harvest.start_date = start_date
    harvest.end_date = end_date
    harvest.status = status
    db.session.commit()
    session['management-status'] = "Updated"
    return redirect( url_for('harvest_route.index') )

# Delete Harvest from the Database
@harvest_route.route('/harvest/delete/<id>')
def delete(id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    harvest = Harvest.find(Harvest,id)
    db.session.delete(harvest)
    db.session.commit()
    session['management-status'] = "Harvest Deleted"
    return redirect(url_for('harvest_route.index'))


@harvest_route.route("/harvest/activate/<harvest_id>")
def activate_harvest(harvest_id):
    if( not verify_permissions(session, User, allowed_rols + ['shopping-analyst']) ):
        return redirect(url_for('harvest_route.index'))
    harvest = Harvest.find(Harvest, harvest_id)
    harvest.status = 'active'
    db.session.add(harvest)
    db.session.commit()
    return redirect(url_for("harvest_route.index"))

@harvest_route.route("/harvest/close/<harvest_id>")
def close_harvest(harvest_id):
    if( not verify_permissions(session, User, allowed_rols + ['shopping-analyst']) ):
        return redirect(url_for('harvest_route.index'))
    harvest = Harvest.find(Harvest, harvest_id)
    harvest.status = 'closed'
    db.session.add(harvest)
    db.session.commit()
    return redirect(url_for("harvest_route.index"))
