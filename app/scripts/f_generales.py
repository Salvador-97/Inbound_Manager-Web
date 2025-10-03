from flask import request
from sqlalchemy import text 


diccionarioREGEX = {"id_contenedor" : "[A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
                    "sku_producto" : "[A-Z][A-Z][1-9][0-9]*[0-9]*C[1-9][0-9]*"}

def tipoBusqueda():
    tipoB = request.form.get("id-select-ctn", "")
    print("Tipo Busqueda: ", tipoB)
    
#Cambiar todo esto por un for
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
    
def consultaDescripcion(connection, productoBusqueda):
    consulta = text('SELECT * FROM productos WHERE sku_producto = :productoBusqueda')
    try:    
        resultado = connection.execute(consulta, {"productoBusqueda": productoBusqueda})
    except Exception as e:
        return None
    else:
        producto = resultado.fetchone()
        return producto