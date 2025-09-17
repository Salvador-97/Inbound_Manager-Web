from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, text 
from app.scripts.f_generales import consultaDescripcion

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
    descripcion = [""]
    if request.method == 'GET':
        skuProducto = request.args.get('sku_producto', "")
        checkUbicacionSin = request.args.get("checkSin", "")
        checkUbicacionCon = request.args.get("checkCon", "")
    if skuProducto:
        with baseDatos.connect() as connection:
            if ((checkUbicacionSin == '0') and (checkUbicacionCon == "")):
                consultaUbicacion = text("SELECT * FROM arrivo_productos WHERE sku_producto = :skuProducto AND ubicacion = 'S/A'")
            elif ((checkUbicacionCon == '1') and (checkUbicacionSin == "")):
                consultaUbicacion = text("SELECT * FROM arrivo_productos WHERE sku_producto = :skuProducto AND ubicacion != 'S/A'")
            else:
                consultaUbicacion = text("SELECT * FROM arrivo_productos WHERE sku_producto = :skuProducto")
            resultado = connection.execute(consultaUbicacion, {"skuProducto" :skuProducto})
            resultadoUbicaciones = resultado.fetchall()
            
            descripcion = consultaDescripcion(connection, skuProducto)
            
    return render_template('/productos/ubicaciones.html', skuProducto = skuProducto, 
                           resultadoUbicaciones = resultadoUbicaciones, descripcion = descripcion[0])

@productos.route('/productos/infoproducto', methods=['GET', 'POST'])
def productosInfo():
    skuProducto = ""
    descripcion = ""
    resultadoProducto = []
    if request.method == 'GET':
        productoBusqueda = request.args.get("sku_producto", "")
        print("Producto SKU: ", productoBusqueda)
    if productoBusqueda:
        with baseDatos.connect() as connection:
            
            descripcion = consultaDescripcion(connection, productoBusqueda)

            consulta = text('SELECT * FROM arrivo_productos WHERE sku_producto = :productoBusqueda')
            resultado = connection.execute(consulta, {"productoBusqueda": productoBusqueda})
            resultadoProducto = resultado.fetchall()
    return render_template('/productos/infoproducto.html', skuProducto = skuProducto, resultadoProducto = resultadoProducto,
                           descripcion = descripcion)