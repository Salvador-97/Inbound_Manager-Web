from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, text 

contenedores = Blueprint('contenedores', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\productos.db')

@contenedores.route('/contenedores')
def inicioContenedores():
    return render_template('contenedores.html')

@contenedores.route('/contenedores/arrivo', methods=['GET', 'POST'])
def contenedoresSKU():
    producto = None
    sku = ""
    if request.method == 'GET':
        skuProducto = request.form.get('sku', "")
    if request.method == 'POST':
        skuProducto = request.form.get('sku_producto', "") 
        producto = request.args.get('sku_producto')
    if skuProducto:
        with baseDatos.connect() as connection:
            consulta = text('SELECT * FROM productos WHERE SKU = :sku_producto')
            resultado = connection.execute(consulta, {"sku_producto": producto})
            producto = resultado.fetchone()
    return render_template('/contenedores/arrivo.html', producto=producto, skuProducto = skuProducto)

@contenedores.route('/contenedores/busqueda', methods=['GET', 'POST'])
def busquedaContenedor():
    if request.method == 'GET':
        contenedorID = request.form.get('sku', "")
    return render_template('contenedores/busqueda.html', contenedorID = contenedorID)