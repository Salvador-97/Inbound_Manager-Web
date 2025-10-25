import { generarEncabezados, mensajesModal, tipoColumna } from "../f_generales.js"
import { crearBoton } from "../botones/editar.js"
import { validarCampo, validacionInputColor, reglasRegex } from "../inserciones/validacionDatos.js"

const formularioUbicaciones = document.getElementById("form-sku-ubicaciones")

formularioUbicaciones.addEventListener('submit', function (e) {
    e.preventDefault()

    const datosForm = new FormData(formularioUbicaciones)
    const parametros = new URLSearchParams(datosForm)
    const datos = Object.fromEntries(datosForm.entries())

    if (!validarCampo(datos.sku_producto, reglasRegex.skuProducto)) {
        validacionInputColor(false, document.querySelector('[name=sku_producto]'))
        mensajesModal('modalUbicacion', 'Error entrada', 'Formato no valido')
        return
    } else {
        validacionInputColor(true, document.querySelector('[name=sku_producto]'))
    }

    fetch(`/api/ubicaciones/buscar?${parametros.toString()}`, {
        method: 'GET'
    })
        .then(response => {
            if (!response.ok) {
                return response.json().then(datos => {
                    mensajesModal('modalUbicacion', `Error ${response.status}`, datos.mensaje)
                })
            }
            return response.json()
        })
        .then(datos => {
            if (datos) {
                const tabla = document.getElementById('contenido-tabla');
                const fragmento = document.createDocumentFragment();

                tabla.innerHTML = "";

                const ordenInformacion = ['sku_producto', 'descripcion', 'id_tarima', 'piezas', 'cajas', 'fecha', 'ubicacion']
                const encabezados = ['SKU', 'Descripción', 'Id Tarima', 'Producto/Tarima', 'Cajas', 'Fecha', 'Ubicación', 'Opciones'];
                generarEncabezados(encabezados)

                datos.ubicaciones.forEach(informacion => {
                    const fila = document.createElement('tr');
                    ordenInformacion.forEach(columnas => {
                        const celda = tipoColumna(columnas, 'sku_producto')
                        if (columnas == 'descripcion') {
                            celda.textContent = datos.descripcion;
                        } else {
                            if (columnas == 'cajas') {
                                celda.setAttribute('name', 'cajas')
                            }
                            celda.textContent = informacion[columnas]
                        }
                        fila.appendChild(celda);
                    })

                    const celdaOpciones = document.createElement('td');
                    celdaOpciones.setAttribute('id', informacion.id_tarima)

                    const boton = crearBoton('editar', 'btn-primary')
                    const boton2 = crearBoton('eliminar', 'btn-danger');

                    celdaOpciones.appendChild(boton);
                    celdaOpciones.appendChild(boton2);

                    fila.appendChild(celdaOpciones);

                    fragmento.appendChild(fila);
                })
                tabla.appendChild(fragmento);
            }
        })
        .catch(error => {
            console.log("Error: ", error)
        });
})