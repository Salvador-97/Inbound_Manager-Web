from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine, text 
from app.scripts.f_generales import consultaDescripcion, obtencionDatos

productos = Blueprint('productos', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\almacen.db')

@productos.route('/producto')
def productosSKU():
    return render_template('producto.html')

@productos.route('/productos/nuevo', methods=['GET', 'POST'])
def productoNuevo():
    tuplaDatos = ()
    if request.method == 'POST':
        tuplaDatos = obtencionDatos()
    if tuplaDatos:
        with baseDatos.connect() as connection:
            insertDB = text('INSERT INTO productos VALUES(:sku, :nombre, :codigoBarras, :productoTarima, :cajasTarima, :masterPack)')
            connection.execute(insertDB, {"sku" :tuplaDatos[1], "nombre": tuplaDatos[8],
                               "codigoBarras" :tuplaDatos[10], "productoTarima" :tuplaDatos[2],
                               "cajasTarima" :tuplaDatos[4], "masterPack" :tuplaDatos[6]})
            connection.commit()  
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
                           resultadoUbicaciones = resultadoUbicaciones, descripcion = descripcion)

@productos.route('/productos/infoproducto', methods=['GET', 'POST'])
def productosInfo():
    skuProducto = ""
    descripcion = []
    resultadoProducto = []
    checkEditar = ""
    if request.method == 'GET':
        productoBusqueda = request.args.get("sku_producto", "")
        print("Recibido en Flask:", productoBusqueda) 
        # checkEditar = request.args.get("checkEditar", "")
    """
    if productoBusqueda:
        with baseDatos.connect() as connection:
            
            if checkEditar == "editar":
                resultado = consultaDescripcion(connection, productoBusqueda)
                resultadoProducto = [resultado]
            else:
                consulta = text('SELECT * FROM arrivo_productos WHERE sku_producto = :productoBusqueda')
                resultado = connection.execute(consulta, {"productoBusqueda": productoBusqueda})
                resultadoProducto = resultado.fetchall()
            descripcion = consultaDescripcion(connection, productoBusqueda)
    """
    
                            
    return render_template('/productos/infoproducto.html', skuProducto = productoBusqueda, resultadoProducto = resultadoProducto,
                           descripcion = descripcion, check = checkEditar)
    
@productos.route('/api/productos/infoproducto', methods=['GET', 'POST'])
def productosInformacionFetch():
    if request.method == 'GET':
        productoBusqueda = request.args.get("sku_producto", "")
        checkEditar = request.args.get("checkEditar", "")                 
    return jsonify({"sku": productoBusqueda})