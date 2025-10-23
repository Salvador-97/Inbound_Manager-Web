from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine, text
from app.scripts.f_generales import consultaDescripcion
from app.scripts.sentencias_sql import consultaProducto, insertContenedor, insertUbicaciones, idTarima

contenedores = Blueprint('contenedores', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\almacen.db')

@contenedores.route('/contenedores')
def inicioContenedores():
    return render_template('contenedores.html')

@contenedores.route('/contenedores/arrivo', methods=['GET', 'POST'])
def contenedoresSKU():
    return render_template('/contenedores/arrivo.html')

@contenedores.route('/api/contenedores/arrivo', methods = ['GET', 'POST'])
def arrivoFetch():
    """
    Realiza consultas e inserciones para los nuevos contenedores que llegan al almacén.

    GET:
        Consulta la información del producto a recibir mediante una solicitud GET.
    POST:
        Inserta en la base de datos la información del contenedor y los productos recibidos vía POST.

    Returns:
        dict: Estados de las operaciones en la base de datos.
    """
    print(f"Método recibido: {request.method}")
    if (request.method == 'GET'):
        skuProducto = request.args.get('sku_producto', "")
        
        if not skuProducto:
            return jsonify({
                "error": "Falta el SKU del producto.",
                "estado": "400"
            }), 400
            
        try:
            with baseDatos.connect() as connection:
                consulta = text(consultaProducto)
                resultado = connection.execute(consulta, {"sku_producto": skuProducto})
                producto = resultado.fetchone()
                
            if producto:
                return jsonify({
                    "producto": dict(producto._mapping),
                    "estado": 200
                }), 200
                
            return jsonify({
                "producto": "Producto no encontrado.",
                "estado": 404
            }), 404
                
        except Exception as e:
            return jsonify({
                "error": str(e),
                "mensaje": "Error al consultar en la base de datos.",
                "estado": 500
            }), 500           
    elif (request.method == 'POST'):
        datosContenedor = request.get_json()

        if not datosContenedor:
            return jsonify({
                "mensaje": "Datos incorrectos.",
                "estado": 400
            }), 400
        try:        
            with baseDatos.connect() as connection:
                connection.execute(insertContenedor, datosContenedor)

                noTarimas = int(datosContenedor.get('no_tarimas'))
                for i in range(0, noTarimas + 1):
                    
                    datosContenedor['id_tarima'] = idTarima(datosContenedor.get('skuProducto'),datosContenedor.get('id_ctn'), i + 1)

                    if (i == noTarimas):
                        if (datosContenedor.get('masterPack') != 'N/A'):
                            cajasTarima = int(datosContenedor.get('masterPack')) * int(datosContenedor.get('resto'))
                            datosContenedor['piezas'] = cajasTarima
                        else:
                            datosContenedor['piezas'] = datosContenedor['resto']
                        datosContenedor['cajas'] = datosContenedor['resto']
                
                    connection.execute(insertUbicaciones, datosContenedor)
                connection.commit()
                return jsonify({
                    "estado": 200
                }), 200
        except Exception as e:
            connection.rollback()
            return jsonify({
                "error": str(e),
                "estado": 400
            }), 400
    return jsonify({
        "mensaje": "Método no permitido.",
        "estado": 405
    }), 405
    
@contenedores.route('/contenedores/busqueda', methods=['GET', 'POST'])
def contenedoresBusqueda():
    return render_template('/contenedores/busqueda.html')

@contenedores.route('/api/contenedores/busqueda', methods=['GET'])
def busqueda():
    """
    Realiza la consulta en la tabla de "contenedores" para ver si existe o no información
    del id del contenedor ingresado.
    
    Detalles:
        - Puede buscar un contenedor por su id, fecha o sku del producto
    
    Returns:
        dict: Estados de las operaciones en la base de datos.
    """
    opcionUsuario = ""
    if request.method == 'GET':
        opcionUsuario = request.args.get('select-ctn', "")
        valorBusqueda = request.args.get('id_ctn', "")
    if opcionUsuario:
        with baseDatos.connect() as connection:
                consulta = text(f"SELECT * FROM contenedores WHERE {opcionUsuario} = :id_ctn")
                try:
                    resultado = connection.execute(consulta, {"id_ctn": valorBusqueda})
                except Exception as e:
                    jsonConsulta = {
                        "error": str(e),
                        "estado": 404
                    }
                else:
                    resultadosTabla = resultado.fetchall()
                    if (resultadosTabla):
                        dicResultados = [dict(row._mapping) for row in resultadosTabla]
                        
                        descripcion = consultaDescripcion(connection, dicResultados[0].get('sku_producto'))
                        if (descripcion != None):
                            contenidoDescripcion = dict(descripcion._mapping)
                        
                            jsonConsulta = {
                                "contenedores": dicResultados,
                                "descripcion": contenidoDescripcion.get('nombre'),
                                "estado": 200
                            }
                        else:
                            jsonConsulta = {
                                "estado": 400
                            }
                    else:
                        jsonConsulta = {
                                "estado": 404
                            }
    return jsonify(jsonConsulta)