from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine, text
from app.scripts.f_generales import obtencionDatos, consultaDescripcion

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
    if (request.method == 'GET'):
        skuProducto = request.args.get('sku_producto', "")
        if skuProducto:
            with baseDatos.connect() as connection:
                consulta = text('SELECT * FROM productos WHERE sku_producto = :sku_producto')
                resultado = connection.execute(consulta, {"sku_producto": skuProducto})
                producto = resultado.fetchone()
                
                jsonConsulta = {
                    "producto": dict(producto._mapping)
                }
    if ((request.method == 'POST')):
        datosContenedor = request.get_json()
        with baseDatos.connect() as connection:
            insertContenedor = text('INSERT INTO contenedores VALUES (:id_ctn, :skuProducto, :fecha_descarga, :id_proveedor, :no_tarimas, :resto)')
            insertUbicaciones = text('INSERT INTO arrivo_productos VALUES (:skuProducto, :piezas, :cajas, :fecha_descarga, :id_ctn, :ubicacion)')
            
            connection.execute(insertContenedor, datosContenedor)
            connection.commit()
            
            noTarimas = int(datosContenedor.get('no_tarimas'))
            for i in range(1, noTarimas + 1):
                if (i == noTarimas):
                    cajasTarima = int(datosContenedor.get('masterPack')) * int(datosContenedor.get('resto'))
                    datosContenedor['piezas'] = cajasTarima
                    datosContenedor['cajas'] = datosContenedor['resto']
                    connection.execute(insertUbicaciones, datosContenedor)
                    connection.commit()
                else:
                    connection.execute(insertUbicaciones, datosContenedor)
                    connection.commit()
        jsonConsulta = {
            "estado": 200
        }
    return jsonify(jsonConsulta)


@contenedores.route('/contenedores/busqueda', methods=['GET', 'POST'])
def contenedoresBusqueda():
    return render_template('/contenedores/busqueda.html')

@contenedores.route('/api/contenedores/busqueda', methods=['GET', 'POST'])
def busqueda():
    opcionUsuario = ""
    if request.method == 'GET':
        opcionUsuario = request.args.get('select-ctn', "")
        valorBusqueda = request.args.get('id_ctn', "")
    if opcionUsuario:
        with baseDatos.connect() as connection:
                consulta = text(f"SELECT * FROM contenedores WHERE {opcionUsuario} = :id_ctn")
                resultado = connection.execute(consulta, {"id_ctn": valorBusqueda})
                resultadosTabla = resultado.fetchall()
                dicResultados = [dict(row._mapping) for row in resultadosTabla]
                                
                descripcion = consultaDescripcion(connection, dicResultados[0].get('sku_producto'))
                contenidoDescripcion = dict(descripcion._mapping)
                
                jsonConsulta = {
                    "contenedores": dicResultados,
                    "descripcion": contenidoDescripcion.get('nombre')
                }
    return jsonify(jsonConsulta)