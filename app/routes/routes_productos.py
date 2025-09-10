from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, text 

productos = Blueprint('productos', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\productos.db')

@productos.route('/producto')
def productosSKU():
    return render_template('producto.html')

@productos.route('/productos/nuevo')
def productoNuevo():
    return render_template('productos/nuevo.html')

@productos.route('/productos/ubicaciones')
def productosUbicaciones():
    return render_template('/productos/ubicaciones.html')

@productos.route('/productos/infoproducto')
def productosInfo():
    return render_template('/productos/infoProducto.html')