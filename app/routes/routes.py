import os
from flask import Blueprint, render_template
from sqlalchemy import create_engine

main = Blueprint('main', __name__, template_folder='app/templates')
# baseDatos = create_engine(r'sqlite:///app/static\db\productos.db')

# Nueva ruta base de datos Render
dirBase = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
dbDir = os.path.join(dirBase, 'static', 'db', 'almacen.db')
dbUbicacion = f"sqlite:///{dbDir}"

baseDatos = create_engine(dbUbicacion)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')