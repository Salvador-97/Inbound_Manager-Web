from sqlalchemy import text


consultaProducto = 'SELECT * FROM productos WHERE sku_producto = :sku_producto'
insertContenedor = text('INSERT INTO contenedores VALUES (:id_ctn, :skuProducto, :fecha_descarga, :id_proveedor, :no_tarimas, :resto)')
insertUbicaciones = text('INSERT INTO arrivo_productos VALUES (:id_tarima, :skuProducto, :piezas, :cajas, :fecha_descarga, :id_ctn, :ubicacion)')

def idTarima(sku, contenedor, indice):
    return f"{sku}-{contenedor[0:2]}{contenedor[4:6]}-{indice:02}"