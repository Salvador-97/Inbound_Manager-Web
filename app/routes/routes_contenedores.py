from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import text
from app.scripts.f_generales import consultaDescripcion
from app.scripts.sentencias_sql import consultaProducto, insertContenedor, insertArrivo, idTarima
from app.routes.routes import baseDatos

contenedores = Blueprint('contenedores', __name__, template_folder='app/templates')
apiContenedores = Blueprint('api_contenedores', __name__)
# baseDatos = create_engine(r'sqlite:///app/static\db\almacen.db')

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
    if (request.method == 'GET'):
        skuProducto = request.args.get('sku_producto', "")
        
        if not skuProducto:
            return jsonify({
                "mensaje": "Falta el SKU del producto.",
            }), 400
            
        try:
            with baseDatos.connect() as connection:
                consulta = text(consultaProducto)
                resultado = connection.execute(consulta, {"sku_producto": skuProducto})
                producto = resultado.fetchone()
                
            if not producto:
                return jsonify({
                    "mensaje": "Producto no encontrado.",
            }), 404
            
            return jsonify({
                "producto": dict(producto._mapping),
            }), 200 
        except Exception as e:
            return jsonify({
                "error": str(e),
                "mensaje": "Error al consultar en la base de datos.",
            }), 500           
    elif (request.method == 'POST'):
        datosContenedor = request.get_json()

        if not datosContenedor:
            return jsonify({
                "mensaje": "Datos incorrectos en algun campo.",
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
                
                    connection.execute(insertArrivo, datosContenedor)
                connection.commit()
                return jsonify({
                    "mensaje": "Contenedor agregado exitosamente."
                }), 200
        except Exception as e:
            connection.rollback()
            return jsonify({
                "error": str(e),
                "mensaje": "Ocurrio un error al agregar el contenedor.",
                "estado": 400
            }), 400
    return jsonify({
        "mensaje": "Método no permitido.",
        "estado": 405
    }), 405
    
@contenedores.route('/contenedores/busqueda', methods=['GET', 'POST'])
def contenedoresBusqueda():
    return render_template('/contenedores/busqueda.html')

@apiContenedores.route('/busqueda', methods=['GET'])
def busqueda():
    """
    Realiza la consulta en la tabla de "contenedores" para ver si existe o no información
    del id del contenedor ingresado.
    
    Detalles:
        - Puede buscar un contenedor por su id, fecha o sku del producto
    
    Returns:
        dict: Estados de las operaciones en la base de datos.
    """
    if request.method == 'GET':
        opcionUsuario = request.args.get('select-ctn', "")
        valorBusqueda = request.args.get('id_ctn', "")
        if not (opcionUsuario or valorBusqueda):
            return jsonify({
                "mensaje": "Error en la entrada de busqueda",
            }), 400
            
        try:    
            with baseDatos.connect() as connection:
                consulta = text(f"SELECT * FROM contenedores WHERE {opcionUsuario} = :id_ctn")
                resultado = connection.execute(consulta, {"id_ctn": valorBusqueda})
                resultadosTabla = resultado.fetchall()
                    
                dicResultados = [dict(row._mapping) for row in resultadosTabla]
                descripcion = consultaDescripcion(connection, dicResultados[0].get('sku_producto'))
                contenidoDescripcion = dict(descripcion._mapping)
                return jsonify({
                    "contenedores": dicResultados,
                    "descripcion": contenidoDescripcion.get('nombre'),
                    "mensaje": ''
                }), 200  
        except Exception as e:
            return jsonify({
                "error": str(e),
                "mensaje": "Información no encontrada."
            }), 404
    return jsonify({
        "mensaje": "Método no permitido.",
        "estado": 405
    }), 405            
