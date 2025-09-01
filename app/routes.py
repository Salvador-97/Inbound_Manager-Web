from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, text 

main = Blueprint('main', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\productos.db')

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/contenedores', methods=['GET', 'POST'])
def contenedores():
    prod = None
    if request.method == 'GET':
        producto = request.args.get('sku_producto')
        with baseDatos.connect() as connection:
            consulta = text('SELECT * FROM productos WHERE SKU = :sku_producto')
            resultado = connection.execute(consulta, {"sku_producto": producto})
            prod = resultado.fetchone()
    return render_template('contenedores.html', producto=prod)

@main.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')

@main.route('/productos')
def productos():
    return render_template('productos.html')