from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine, text 
from app.scripts.f_generales import consultaDescripcion
from app.scripts.sentencias_sql import consultaSku, insertProducto

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
    """
    Realiza la inserción de un nuevo producto en la base de datos "productos".
    
    POST:
        Verifica que no este el producto ya registrado, en caso de que no lo este,
        lo agrega a la base de datos.
    Returns
        JSON del estado de la operación
    """
    if (request.method == 'POST'):
        formularios = ['skuProducto', 'descripcion', 'codigo_barras', 'cajas_tarima', 'producto_tarima', 'master_pack']
        datos = {formulario: request.form.get(formulario) for formulario in formularios}
        
        if not datos:
            return jsonify({
                "mensaje": "Error en los datos ingresados.",
            }), 400
        try:
            with baseDatos.connect() as connection:
                
                if (connection.execute(consultaSku, {'skuProducto': datos.get('skuProducto')})):
                    return jsonify({
                        "mensaje": "El producto ya existe."
                    }), 404
                    
                connection.execute(insertProducto, datos)
                connection.commit()
                return jsonify({
                    "mensaje": "Producto agregado exitosamente."
                }), 200
                
        except Exception as e:
            return jsonify({
                "mensaje": "Ocurrio un error al consultar la base de datos.",
            }), 400
            
    return jsonify({
        "mensaje": "Ocurrio un problema al mandar la información, intente de nuevo.",
    }), 405

@productos.route('/productos/infoproducto', methods=['GET'])
def productosInfo():              
    return render_template('/productos/infoproducto.html')
    
@productos.route('/api/productos/infoproducto', methods=['GET'])
def productosInformacionFetch():
    """
    Realiza la busqueda de un producto para mostrar su información, en caso de no encontrarse
    se notifica al usuario.
    
    GET
        Solicita el sku del producto para buscar y regresar la información
    Returns
        JSON con es estado de la consulta
    """
    if request.method == 'GET':
        productoBusqueda = request.args.get("sku_producto", "")
        
        if not productoBusqueda:
            return jsonify({
                "mensaje": "Formato de SKU incorrecto.",
            }), 400
        
        try:
            with baseDatos.connect() as connection:
                
                resultado = consultaDescripcion(connection, productoBusqueda)
                dictResultado = dict(resultado._mapping)
                return jsonify({
                    "sku": productoBusqueda, 
                    "producto": dictResultado,
                }), 200
                
        except Exception as e:
            return jsonify({
                "mensaje": "Producto no encontrado.",
            }), 404
            
    return jsonify({
        "mensaje": "Ocurrio un problema al mandar la información, intente de nuevo.",
        "estado": 405
    }), 405