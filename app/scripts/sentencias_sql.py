from sqlalchemy import text

#Sentencias productos
consultaProducto = 'SELECT * FROM productos WHERE sku_producto = :sku_producto'
consultaSku = text('SELECT sku_producto FROM productos WHERE sku_producto = :skuProducto')
insertProducto = text('INSERT INTO productos VALUES(:skuProducto, :descripcion, :codigo_barras, :producto_tarima, :cajas_tarima, :master_pack)')

#Sentencias contenedores
insertContenedor = text('INSERT INTO contenedores VALUES (:id_ctn, :skuProducto, :fecha_descarga, :id_proveedor, :no_tarimas, :resto)')
insertArrivo = text('INSERT INTO arrivo_productos VALUES (:id_tarima, :skuProducto, :piezas, :cajas, :fecha_descarga, :id_ctn, :ubicacion)')

#Sentencias ubicaciones
consultaSU = text("SELECT * FROM arrivo_productos WHERE sku_producto = :skuProducto AND ubicacion = 'S/U'")
consultaCU = text("SELECT * FROM arrivo_productos WHERE sku_producto = :skuProducto AND ubicacion != 'S/U'")
consultaUbicaciones = text("SELECT * FROM arrivo_productos WHERE sku_producto = :skuProducto")
insertUbicacion = text('UPDATE ubicaciones SET id_tarima = :idTarima, disponible = :disponible, cajas = :cajas WHERE ubicacion = :ubicacion')
insertArrivoUbicacion = text('UPDATE arrivo_productos SET ubicacion = :ubicacion WHERE id_tarima = :idTarima') 

def idTarima(sku, contenedor, indice):
    return f"{sku}-{contenedor[0:2]}{contenedor[4:6]}-{indice:02}"