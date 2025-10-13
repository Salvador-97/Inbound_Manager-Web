from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine, text 

ubicaciones = Blueprint('productos', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\almacen.db')

@ubicaciones.route('/ubicaciones')
def ubicaciones():
    return render_template('ubicaciones.html')