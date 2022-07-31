from flask import Blueprint, render_template, redirect, url_for, request, session
from utils.functions import *
from utils.db import db
from datetime import datetime

bank = Blueprint('bank', __name__)
allowed_rols = ['admin', 'shopping-analyst']

@bank.route('/bank')
def index():
        return render_template("bank.html")

