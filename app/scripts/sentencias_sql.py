from sqlalchemy import text

#Sentencias productos
consultaProducto = 'SELECT * FROM productos WHERE sku_producto = :sku_producto'
consultaSku = text('SELECT sku_producto FROM productos WHERE sku_producto = :skuProducto')
insertProducto = text('INSERT INTO productos VALUES(:skuProducto, :descripcion, :codigo_barras, :producto_tarima, :cajas_tarima, :master_pack)')

#Sentencias contenedores
insertContenedor = text('INSERT INTO contenedores VALUES (:id_contenedor, :fecha_descarga , :id_proveedor, :sku_producto, :no_tarimas, :resto)')
insertArribo = text('INSERT INTO arribos VALUES (:id_tarima, :sku_producto, :fecha_descarga, :id_contenedor, :ubicacion, :cajas_por_tarima, :piezas_por_caja)')

#Sentencias ubicaciones
consultaSU = text("SELECT * FROM arribo_productos WHERE sku_producto = :skuProducto AND ubicacion = 'S/U'")
consultaCU = text("SELECT * FROM arribo_productos WHERE sku_producto = :skuProducto AND ubicacion != 'S/U'")
consultaUbicaciones = text("SELECT * FROM arribo_productos WHERE sku_producto = :skuProducto")
insertUbicacion = text('UPDATE ubicaciones SET id_tarima = :idTarima, disponible = :disponible, cajas = :cajas WHERE ubicacion = :ubicacion')
insertArriboUbicacion = text('UPDATE arribo_productos SET ubicacion = :ubicacion WHERE id_tarima = :idTarima') 

def idTarima(sku, contenedor, indice):
    return f"{sku}-{contenedor[0:2]}{contenedor[4:6]}-{indice:02}"