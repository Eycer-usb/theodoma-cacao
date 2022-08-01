"""

Routes For Purchase Model

Route Map:

/harvest/id/purchase

"""


from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from utils.db import db
from models.purchase import Purchase
from datetime import datetime
purchase = Blueprint('purchase', __name__)
allowed_rols = ['admin', 'shopping-analyst']

@purchase.route('/harvest/<harvest_id>/purchase', methods=['GET'])
def index(harvest_id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    harvest = Harvest.find(Harvest, harvest_id)
    purchases = Purchase.query.filter_by(F_Harvest = harvest_id)
    productors = Productor.query.all()
    productor_types = Productor_type.query.all()
    status = ""

    total_cantidad = sum(purchase.total_amount_kg for purchase in purchases)

    total_monto = ("{0:.2f}".format(sum(purchase.total_dolar for purchase in purchases)))
    
    if 'management-status' in session: status = session['management-status']
    return render_template("purchase.html", harvest=harvest, purchases=purchases,
    productors=productors, productor_types= productor_types, status=status, total_cantidad=total_cantidad, total_monto=total_monto)

@purchase.route('/harvest/<harvest_id>/purchase/create', methods=["POST"])
def create(harvest_id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )

    date = datetime.today().strftime('%Y-%m-%d')
    harvest_id = request.form['harvest-id']
    productor_id = request.form['productor-id']
    cacao_type= request.form['cacao-type']
    price = float(request.form['price-dolar'])
    cant = request.form['amount-kg']
    humed = request.form['wetness-percentage']
    merma = request.form['waste-percentage']
    merma1 = float(merma)/100
    mermakg = float(cant)*float(merma1)

    """if( not valid_date_purchase(date) ):
        session['management-status'] = "Fecha fuera de rangos"
        return redirect(url_for('purchase.index'))"""

    greenAlmond = True if request.form.get("greenAlmond") == "on" else False
    if (greenAlmond):
        merma2 = mermakg*2    
        total_amount_kg= float(cant)-float(merma2)
        monto = float(price)*float(total_amount_kg)
        observation = request.form['observation']
        new_shopping = Purchase(date=date, F_Productor=productor_id,\
        F_Harvest=harvest_id, cacao_type=cacao_type, price_dolar=price,\
            amount_kg=cant, wetness_percentage=humed, waste_percentage=merma,\
                 waste_kg=mermakg, total_amount_kg=total_amount_kg,\
                    total_dolar=monto, observation=observation )

        
        harvest = Harvest.query.get(harvest_id)
        if harvest.status == 'active':
            db.session.add(new_shopping)
            db.session.commit()
            session['management-status'] = "Compra Creada"
        else:
            session['management-status'] = "Cosecha Cerrada"
        return redirect(url_for("harvest_route.index"))


    else: 
        print("entra else")
        mermakg = float(cant)*float(merma1)
        total_amount_kg= float(cant)-float(mermakg)
        monto = float(price)*float(total_amount_kg)
        observation = request.form['observation']

        new_shopping = Purchase(date=date, F_Productor=productor_id,\
        F_Harvest=harvest_id, cacao_type=cacao_type, price_dolar=price,\
            amount_kg=cant, wetness_percentage=humed, waste_percentage=merma,\
                 waste_kg=mermakg, total_amount_kg=total_amount_kg,\
                    total_dolar=monto, observation=observation )

        harvest = Harvest.query.get(harvest_id)
        if harvest.status == 'active':
            db.session.add(new_shopping)
            db.session.commit()
            session['management-status'] = "Compra Creada"
        else:
            session['management-status'] = "Cosecha Cerrada"
        return redirect(url_for("harvest_route.index"))

@purchase.route('/harvest/<harvest_id>/purchase/<purchase_id>/edit', methods=["GET"])
def edit(harvest_id, purchase_id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))

    shp_data = Purchase.query.get(purchase_id)
    tips_product = Productor_type.query.all()  
    productors = Productor.query.all()
    harvest = Harvest.query.get(harvest_id)
    return render_template("purchase-edit.html", purchase = shp_data,\
        tips_product = tips_product, productors = productors, harvest=harvest)


@purchase.route('/harvest/<harvest_id>/purchase/update', methods=["POST"])
def update(harvest_id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect( url_for('auth.index') )
    id = request.form['id']
    purchase = Purchase.query.get(id)
    purchase.date = request.form['date']
    purchase.F_Harvest = request.form['harvest-id']
    purchase.F_Productor = request.form['productor-id']
    purchase.cacao_type= request.form['cacao-type']
    purchase.price_dolar = request.form['price-dolar']
    purchase.amount_kg = request.form['amount-kg']
    purchase.wetness_percentage = request.form['wetness-percentage']
    purchase.waste_percentage = request.form['waste-percentage']
    merma1 = float(purchase.waste_percentage)/100
    purchase.waste_kg = float(purchase.amount_kg)*float(merma1)
    purchase.total_amount_kg= float(purchase.amount_kg)-float(purchase.waste_kg)
    purchase.total_dolar = float(purchase.price_dolar)*float(purchase.total_amount_kg)
    purchase.observation = request.form['observation']
    db.session.add(purchase)
    db.session.commit()
    session['management-status'] = "Purchase Created"
    return redirect(url_for("purchase.index", harvest_id=harvest_id))

@purchase.route('/harvest/<harvest_id>/purchase/<purchase_id>/delete')
def delete(purchase_id, harvest_id):
    if( not verify_permissions(session, User, allowed_rols) ):
        return redirect(url_for('auth.index'))
    shp_data = Purchase.query.get(purchase_id)
    db.session.delete(shp_data)
    db.session.commit()
    session['management-status'] = "Compra Eliminada"
    return redirect(url_for("purchase.index", harvest_id=harvest_id))

