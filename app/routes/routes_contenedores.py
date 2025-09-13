from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, text, insert

contenedores = Blueprint('contenedores', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\almacen.db')

@contenedores.route('/contenedores')
def inicioContenedores():
    return render_template('contenedores.html')

@contenedores.route('/contenedores/arrivo', methods=['GET', 'POST'])
def contenedoresSKU():
    producto = None
    skuProducto = None
    if request.method == 'GET':
        skuProducto = request.args.get('sku_producto', "")
    if skuProducto:
        with baseDatos.connect() as connection:
            consulta = text('SELECT * FROM productos WHERE SKU = :sku_producto')
            resultado = connection.execute(consulta, {"sku_producto": skuProducto})
            producto = resultado.fetchone()
            print("Producto enviado: ", producto)
    if request.method == 'POST':
        tuplaDatos = obtencionDatos()
        with baseDatos.connect() as connection:
            columInsert = text('INSERT INTO contenedores VALUES (:id_contenedor, :sku_producto, :fecha_descarga, :proveedor, :no_tarimas, :resto_cajas)')
            connection.execute(columInsert, {"id_contenedor": tuplaDatos[0], "sku_producto": tuplaDatos[1],
                                                          "fecha_descarga": tuplaDatos[3], "proveedor": tuplaDatos[5],
                                                          "no_tarimas": tuplaDatos[7], "resto_cajas": tuplaDatos[9]})
            connection.commit()
    return render_template('/contenedores/arrivo.html', producto=producto, skuProducto = skuProducto)

def obtencionDatos():
    idContenedor = request.form.get('id_ctn', "")
    skuProducto = request.form.get('skuProducto', "")
    productoTarima = request.form.get('producto_tarima', "");
    fechaDescarga = request.form.get('fecha_descarga', "");
    cajasTarima = request.form.get('cajas_tarima', "");
    idProveedor = request.form.get('id_proveedor', "");
    masterPack = request.form.get('master_pack', "");
    noTarimas = request.form.get('no_tarimas', "");
    descripcion = request.form.get('descripcion', "");
    resto = request.form.get('resto', "");
    codigoBarras = request.form.get('codigo_barras', "");
    
    return [idContenedor, skuProducto, productoTarima, fechaDescarga, cajasTarima, idProveedor, 
            masterPack, noTarimas, descripcion, resto, codigoBarras]

@contenedores.route('/contenedores/busqueda', methods=['GET'])
def busquedaContenedor():
    contenedor = None
    if request.method == 'GET':
        idContenedor = request.args.get('id_ctn', "")
        if idContenedor:
            with baseDatos.connect() as connection:
                consulta = text('SELECT * FROM contenedores WHERE id_contenedor = :idContenedor')
                resultado = connection.execute(consulta, {"idContenedor": idContenedor})
                contenedor = resultado.fetchone()
    return render_template('contenedores/busqueda.html', contenedor=contenedor, contenedorID = idContenedor)