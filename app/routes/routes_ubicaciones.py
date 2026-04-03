from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import text 
from app.scripts.f_generales import consultaDescripcion
from app.scripts.sentencias_sql import consultaCU, consultaSU, consultaUbicaciones, insertUbicacion, insertArriboUbicacion
from app.routes.routes import basePostgreSQL

ubicaciones = Blueprint('ubicaciones', __name__, template_folder='app/templates')
apiUbicaciones = Blueprint('api_ubicaciones', __name__)

@ubicaciones.route('/ubicaciones')
def ubicacionesMenu():
    return render_template('ubicaciones.html')

@ubicaciones.route('/ubicaciones/nueva')
def nuevaUbicacion():
    return render_template('ubicaciones/nueva.html')

@ubicaciones.route('/ubicaciones/buscar')
def informacion():
    return render_template('ubicaciones/ubicaciones.html')

@apiUbicaciones.route('/buscar', methods=['GET', 'POST'])
def informacionUbicacion():
    """
    Realiza la busqueda de todos los productos a partir de su sku, y permite mostrar cuales 
    tienen o no tienen ubicación, tambien permite asignarles una ubicación o eliminarla.
    
    GET:
        -Recupera la información de las ubicaciones de un cierto producto.
    POST:
        -Permite asignarle una ubicación a un tarima.
    Returns:
        JSON de los estados de las operaciones en la base de datos.
    """
    if request.method == 'GET':
        skuProducto = request.args.get('sku_producto', "")
        checkUbicacionSin = request.args.get("checkSin", "")
        checkUbicacionCon = request.args.get("checkCon", "")
        
        if not skuProducto:
            return jsonify({
                "mensaje": "Error en la entrada",
            }), 400
        try:
            #Meter una opcion donde mencione si hay informacion o no del producto
            with basePostgreSQL.connect() as connection:
                if ((checkUbicacionSin == '0') and (checkUbicacionCon == "")):
                    consultaUbicacion = consultaSU
                elif ((checkUbicacionCon == '1') and (checkUbicacionSin == "")):
                    consultaUbicacion = consultaCU
                else:
                    consultaUbicacion = consultaUbicaciones
                resultado = connection.execute(consultaUbicacion, {"skuProducto" :skuProducto})
                    
                resultadoUbicaciones = [dict(row._mapping) for row in resultado.fetchall()]
                
                if not resultadoUbicaciones:
                    return jsonify({
                        "mensaje": "No hay información de este producto."
                }), 404

                descripcion = consultaDescripcion(connection, skuProducto)
                contenidoDescripcion = dict(descripcion._mapping)
                            
            return jsonify({
                "ubicaciones": resultadoUbicaciones,
                "descripcion": contenidoDescripcion.get('nombre'),
            }), 200
        except Exception as e:
            return jsonify({
                "mensaje": "Producto no encontrado.",
            }), 404
    if (request.method == 'POST'):
        formulario = ['ubicacion', 'skuProducto', 'cajas', 'idTarima']
        datos = {items: request.form.get(items) for items in formulario}
        
        if not datos:
            return jsonify({
                "mensaje": "Error en la entrada.",
            }), 400
        try:    
            with basePostgreSQL.connect() as connection:
                consulta = text('SELECT * FROM ubicaciones WHERE ubicacion =:ubicacion')
                resultado = connection.execute(consulta, datos)
                resultadoUbicacion = resultado.fetchone()
                
                if (resultadoUbicacion[2] == 0) :
                    datos['disponible'] = 1
                    insercionUbicacion = insertUbicacion
                    insercionArriboUbicacion = insertArriboUbicacion       

                    connection.execute(insercionUbicacion, datos)
                    connection.execute(insercionArriboUbicacion, datos)
                    
                connection.commit()
                return jsonify({
                    "mensaje": "Ubicación actualizada.",
                }), 200
        except Exception as e:
            connection.rollback()
            return jsonify({
                "mensaje": "Error en al agregar ubicación.",
            }), 400
    return jsonify({
        "mensaje": "Método no permitido",
    }), 405