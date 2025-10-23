from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine, text 
from app.scripts.f_generales import consultaDescripcion

productos = Blueprint('productos', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\almacen.db')

@productos.route('/producto')
def productosSKU():
    return render_template('producto.html')

@productos.route('/productos/nuevo', methods=['GET', 'POST'])
def productoNuevo():
    return render_template('productos/nuevo.html')

@productos.route('/api/productos/nuevo', methods=['GET', 'POST'])
def fetchNuevoProducto():
    if (request.method == 'POST'):
        formularios = ['skuProducto', 'descripcion', 'codigo_barras', 'cajas_tarima', 'producto_tarima', 'master_pack']
        datos = {formulario: request.form.get(formulario) for formulario in formularios}
    if datos:
        with baseDatos.connect() as connection:
            print("JSON: ", datos.get('skuProducto'))
            consultaSKU = text('SELECT sku_producto FROM productos WHERE sku_producto = :skuProducto')
            checkSKU = connection.execute(consultaSKU, {'skuProducto': datos.get('skuProducto')})
            if (checkSKU.fetchone() != None): 
                estadoConsulta = {
                    "estado": 400
                }
            else:
                insertSKU = text('INSERT INTO productos VALUES(:skuProducto, :descripcion, :codigo_barras, :producto_tarima, :cajas_tarima, :master_pack)')
                connection.execute(insertSKU, datos)
                connection.commit()
                estadoConsulta = {
                    "estado": 200
                }
    return jsonify(estadoConsulta)

@productos.route('/productos/infoproducto', methods=['GET', 'POST'])
def productosInfo():              
    return render_template('/productos/infoproducto.html')
    
@productos.route('/api/productos/infoproducto', methods=['GET', 'POST'])
def productosInformacionFetch():
    if request.method == 'GET':
        productoBusqueda = request.args.get("sku_producto", "")
        # checkEditar = request.args.get("checkEditar", "")
        checkEditar = 'editar'
        
        if productoBusqueda:
            jsonConsulta = {}
            with baseDatos.connect() as connection:
                if checkEditar == "editar":
                    resultado = consultaDescripcion(connection, productoBusqueda)
                    dictResultado = dict(resultado._mapping)
                    jsonConsulta = {
                        "sku": productoBusqueda, 
                        "producto": dictResultado,
                        "tipo": checkEditar
                        }
                """
                else:
                    consulta = text('SELECT * FROM arrivo_productos WHERE sku_producto = :productoBusqueda')
                    resultado = connection.execute(consulta, {"productoBusqueda": productoBusqueda})
                    resultadoProducto = resultado.fetchall()
                    listaProductos = [dict(row._mapping) for row in resultadoProducto]
                    
                    descripcion = consultaDescripcion(connection, productoBusqueda)
                    contenidoDescripcion = dict(descripcion._mapping)
                    
                    jsonConsulta = {
                        "sku": productoBusqueda, 
                        "productos": listaProductos, 
                        "descripcion": contenidoDescripcion, 
                        "producto": contenidoDescripcion,
                        "tipo": 0
                        }
                """
    return jsonify(jsonConsulta)