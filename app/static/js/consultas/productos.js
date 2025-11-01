import { tipoColumna, generarEncabezadosTabla, mensajesModal } from "../f_generales.js"
import { crearBoton } from "../botones/editar.js";
import { reglasRegex, validacionInputColor, validarCampo } from "../inserciones/validacionDatos.js";

const formulario = document.getElementById("form-sku-busqueda");
formulario.addEventListener('submit', function (e) {
    e.preventDefault();

    const infoFormulario = new FormData(formulario);
    const parametros = new URLSearchParams(infoFormulario);
    const datos = Object.fromEntries(infoFormulario.entries())

    if(!validarCampo(datos.sku_producto, reglasRegex.skuProducto)){
        validacionInputColor(false, document.querySelector('[name=sku_producto]'))
        mensajesModal('modalInput', 'Error entrada', 'Formato no valido')
        return
    } else {
        validacionInputColor(true, document.querySelector('[name=sku_producto]'))
    }

    fetch(`/api/producto/informacion?${parametros.toString()}`, {
        method: 'GET',
    })
        .then(response => {
            if (!response.ok) {
                return response.json().then(datos => {
                    mensajesModal('modalInput', `Error ${response.status}`, datos.mensaje)
                })
            }
            return response.json()
        })
        .then(datos => {
            const tbody = document.getElementById("tabla");
            tbody.innerHTML = "";

            if (datos) {
                generarEncabezadosTabla(datos.tipo)

                const fila = document.createElement("tr");
                const ordenInformacion = ['sku_producto', 'nombre', 'codigoBarras', 'piezas', 'cajas', 'masterPack']
                let td = null

                ordenInformacion.forEach(columna => {
                    td = tipoColumna(columna, 'sku_producto')
                    td.textContent = datos.producto[columna]
                    fila.appendChild(td);
                })

                //Simplificar la creacion de estos botones
                const tdBoton = document.createElement('td')
                const boton = crearBoton('editar', 'btn-primary')
                const boton2 = crearBoton('eliminar', 'btn-danger');
                tdBoton.appendChild(boton)
                tdBoton.appendChild(boton2)
                fila.appendChild(tdBoton)

                tbody.appendChild(fila);
            }
        })
        .catch(error => {
            console.log("Error: ", error)
        })
})
