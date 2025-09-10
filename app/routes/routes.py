from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, text 

main = Blueprint('main', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\productos.db')

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')