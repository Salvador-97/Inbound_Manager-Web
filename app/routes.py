from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, text 

main = Blueprint('main', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\productos.db')

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/contenedores')
def inicioContenedores():
    return render_template('contenedores.html')

@main.route('/contenedores/arrivo', methods=['GET', 'POST'])
def contenedores():
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

@main.route('/contenedores/busqueda', methods=['GET', 'POST'])
def busquedaContenedor():
    if request.method == 'GET':
        contenedorID = request.form.get('sku', "")
    return render_template('contenedores/busqueda.html', contenedorID = contenedorID)

@main.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')

@main.route('/productos')
def productos():
    return render_template('productos.html')