from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine, text 
from app.scripts.f_generales import consultaDescripcion

ubicaciones = Blueprint('ubicaciones', __name__, template_folder='app/templates')
baseDatos = create_engine(r'sqlite:///app/static\db\almacen.db')

@ubicaciones.route('/ubicaciones')
def ubicacionesMenu():
    return render_template('ubicaciones.html')

@ubicaciones.route('/ubicaciones/nuevo')
def nuevaUbicacion():
    return render_template('ubicaciones/nueva.html')

@ubicaciones.route('/ubicaciones/buscar')
def informacion():
    return render_template('ubicaciones/ubicaciones.html')

@ubicaciones.route('/api/ubicaciones/buscar', methods=['GET', 'POST'])
def informacionUbicacion():
    if request.method == 'GET':
        skuProducto = request.args.get('sku_producto', "")
        checkUbicacionSin = request.args.get("checkSin", "")
        checkUbicacionCon = request.args.get("checkCon", "")
        if skuProducto:
            with baseDatos.connect() as connection:
                if ((checkUbicacionSin == '0') and (checkUbicacionCon == "")):
                    consultaUbicacion = text("SELECT * FROM arrivo_productos WHERE sku_producto = :skuProducto AND ubicacion = 'S/U'")
                elif ((checkUbicacionCon == '1') and (checkUbicacionSin == "")):
                    consultaUbicacion = text("SELECT * FROM arrivo_productos WHERE sku_producto = :skuProducto AND ubicacion != 'S/U'")
                else:
                    consultaUbicacion = text("SELECT * FROM arrivo_productos WHERE sku_producto = :skuProducto")
                resultado = connection.execute(consultaUbicacion, {"skuProducto" :skuProducto})
                
                resultadoUbicaciones = [dict(row._mapping) for row in resultado.fetchall()]

                descripcion = consultaDescripcion(connection, skuProducto)
                contenidoDescripcion = dict(descripcion._mapping)
                            
                jsonConsulta = {
                    "ubicaciones": resultadoUbicaciones,
                    "descripcion": contenidoDescripcion.get('nombre')
                }
        return jsonify(jsonConsulta)
    if (request.method == 'POST'):
        ubicacion = request.form.get('ubicacion', "")
        skuProducto = request.form.get('skuProducto', "")
        cajas = request.form.get('cajas', "")
        idTarima = request.form.get('idTarima', "")
        if (ubicacion):
            with baseDatos.connect() as connection:
                consulta = text('SELECT * FROM ubicaciones WHERE ubicacion =:ubicacion')
                try:
                    resultado = connection.execute(consulta, {"ubicacion": ubicacion })
                except Exception as e:
                    jsonConsulta = {
                        "error": str(e),
                        "estado": 404
                    }
                else:
                    resultadoUbicacion = resultado.fetchone()
                    print("Resultado", resultadoUbicacion)
                    if (resultadoUbicacion != None):
                        if (resultadoUbicacion[2] == 0) :
                            # datos = {"skuProducto": skuProducto, "disponible": 1, "cajas": cajas, "ubicacion": ubicacion}
                            nuevaUbicacion = {"idTarima": idTarima, "disponible": 1, "cajas": cajas, "ubicacion": ubicacion}
                            insercionUbicacion = text('UPDATE ubicaciones SET id_tarima = :idTarima, disponible = :disponible, cajas = :cajas WHERE ubicacion = :ubicacion')
                            insercionArrivoUbicacion = text('UPDATE arrivo_productos SET ubicacion = :ubicacion WHERE id_tarima = :idTarima')        
                            try:
                                connection.execute(insercionUbicacion, nuevaUbicacion)
                                connection.execute(insercionArrivoUbicacion, {"ubicacion": ubicacion,"idTarima": idTarima})
                            except Exception as e:
                                print(e)
                                jsonConsulta = {
                                    "error": str(e),
                                    "estado": 400
                                }
                                connection.rollback()
                                connection.rollback()
                            else:
                                jsonConsulta = {
                                    "estado": 200
                                }
                                connection.commit()
                                connection.commit()       
                        else:
                            jsonConsulta = {
                                "estado": 400
                            }
                    else: 
                        jsonConsulta = {
                        "estado": 404
                    }
    return jsonify(jsonConsulta)
