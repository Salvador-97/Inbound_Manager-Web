from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, text 

productos = Blueprint('productos', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\almacen.db')

@productos.route('/producto')
def productosSKU():
    return render_template('producto.html')

@productos.route('/productos/nuevo')
def productoNuevo():
    return render_template('productos/nuevo.html')

@productos.route('/productos/ubicaciones', methods=['GET', 'POST'])
def productosUbicaciones():
    skuProducto = ""
    resultadoUbicaciones = []
    if request.method == 'GET':
        skuProducto = request.args.get('sku_producto', "")
    if skuProducto:
        with baseDatos.connect() as connection:
            consulta = text('SELECT * FROM ubicaciones WHERE SKU = :skuProducto')
            resultado = connection.execute(consulta, {"skuProducto" :skuProducto})
            resultadoUbicaciones = resultado.fetchall()
    return render_template('/productos/ubicaciones.html', skuProducto = skuProducto, resultadoUbicaciones = resultadoUbicaciones)

@productos.route('/productos/infoproducto', methods=['GET', 'POST'])
def productosInfo():
    skuProducto = ""
    resultadoProducto = []
    if request.method == 'GET':
        productoBusqueda = request.args.get("sku_producto", "")
        print("Producto SKU: ", productoBusqueda)
    if productoBusqueda:
        with baseDatos.connect() as connection:
            consulta = text('SELECT * FROM arrivo_productos WHERE sku_producto = :productoBusqueda')
            resultado = connection.execute(consulta, {"productoBusqueda": productoBusqueda})
            resultadoProducto = resultado.fetchall()
            print(resultadoProducto)
    return render_template('/productos/infoproducto.html', skuProducto = skuProducto, resultadoProducto = resultadoProducto)