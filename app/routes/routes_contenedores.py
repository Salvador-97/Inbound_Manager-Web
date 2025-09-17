from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, text
from app.scripts.f_generales import obtencionDatos

contenedores = Blueprint('contenedores', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\almacen.db')

@contenedores.route('/contenedores')
def inicioContenedores():
    return render_template('contenedores.html')

@contenedores.route('/contenedores/arrivo', methods=['GET', 'POST'])
def contenedoresSKU():
    producto = None
    skuProducto = ""
    if request.method == 'GET':
        skuProducto = request.args.get('sku_producto', "")
    if skuProducto:
        with baseDatos.connect() as connection:
            consulta = text('SELECT * FROM productos WHERE sku_producto = :sku_producto')
            resultado = connection.execute(consulta, {"sku_producto": skuProducto})
            producto = resultado.fetchone()
    if request.method == 'POST':
        tuplaDatos = obtencionDatos()
        with baseDatos.connect() as connection:
            columInsert = text('INSERT INTO contenedores VALUES (:id_contenedor, :sku_producto, :fecha_descarga, :proveedor, :no_tarimas, :resto_cajas)')
            connection.execute(columInsert, {"id_contenedor": tuplaDatos[0], "sku_producto": tuplaDatos[1],
                                                          "fecha_descarga": tuplaDatos[3], "proveedor": tuplaDatos[5],
                                                          "no_tarimas": tuplaDatos[7], "resto_cajas": tuplaDatos[9]})
            connection.commit() 
            # Poner una validacion para que solo si se realizo la insercion del contenedor pase a 
            # hacer esta otra insercion
            insertArrivo = text('INSERT INTO arrivo_productos VALUES (:sku_producto, :piezas, :cajas, :fecha, :contenedor, :ubicacion)')
            for i in range (0, int(tuplaDatos[7]) + 1):
                if (i == (int(tuplaDatos[7]))):
                    if (tuplaDatos[6] != 'N/A'):
                        piezasResto = int(tuplaDatos[6]) * int(tuplaDatos[9])
                    else: 
                        piezasResto = int(tuplaDatos[9])
                    connection.execute(insertArrivo, {"sku_producto": tuplaDatos[1], "piezas": piezasResto,
                                                      "cajas": tuplaDatos[9], "fecha": tuplaDatos[3], "contenedor": tuplaDatos[0],
                                                      "ubicacion": "S/A"})
                    connection.commit()
                else:
                    connection.execute(insertArrivo, {"sku_producto": tuplaDatos[1], "piezas": tuplaDatos[2],
                                                      "cajas": tuplaDatos[4], "fecha": tuplaDatos[3], "contenedor": tuplaDatos[0],
                                                      "ubicacion": "S/A"})
                    connection.commit()
                
    return render_template('/contenedores/arrivo.html', producto=producto, skuProducto = skuProducto)

@contenedores.route('/contenedores/busqueda', methods=['GET', 'POST'])
def busquedaContenedor():
    resultadosTabla = []
    tipoB = request.form.get("select-ctn", "")
    if request.method == 'POST':
        tipoBusqueda = request.form.get('id_ctn', "")
        if tipoBusqueda:
            with baseDatos.connect() as connection:
                consulta = text(f"SELECT * FROM contenedores WHERE {tipoB} = :id_ctn")
                resultado = connection.execute(consulta, {"id_ctn": tipoBusqueda})
                resultadosTabla = resultado.fetchall()
    return render_template('contenedores/busqueda.html', resultadosTabla=resultadosTabla, tipo = tipoB)