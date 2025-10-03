import { generarEncabezados, mensajesModal, tipoColumna } from '../f_generales.js'
import { reglasRegex, validacionInputColor, validarCampo } from '../inserciones/validacionDatos.js';

const busquedaCTN = document.getElementById("form_ctn_busqueda");
busquedaCTN.addEventListener('submit', function(e) {
    e.preventDefault();

    const infoFormulario = new FormData(busquedaCTN);
    const parametros = new URLSearchParams(infoFormulario);

    //Validacion en donde la opcion seleccionada coincida con el regex de esa opcion
    const tipoSelect = {'id_contenedor': reglasRegex.id_ctn, 'sku_producto': reglasRegex.skuProducto, 'fecha_descarga': reglasRegex.fecha_descarga}

    const select = Object.entries(tipoSelect);
    let validacion = false

    select.forEach(([key, valor]) => {
        if (infoFormulario.get('select-ctn') == key) {
            const checkInput = validarCampo(infoFormulario.get('id_ctn'), valor);
            validacion = validacionInputColor(checkInput, document.querySelector('input[name=id_ctn]'))
        }
    })

    if (validacion) {
        mensajesModal('modalInput', "Error", "Error en la entrada de busqueda")
        return;
    }
    
    fetch(`/api/contenedores/busqueda?${parametros.toString()}`, {
        method: 'GET',
    })
    .then(response => {
        const contentType = response.headers.get('content-type');

        if (contentType && contentType.includes('application/json')) {
            return response.json();
        } else {
            return response.text();
        }
    })
    .then(datos => {
        const tablaContenedor = document.getElementById('tablaContenedor');
        tablaContenedor.innerHTML = "";
        console.log("Datos: ", datos)
        if (datos.estado == 200) {
            const fragmento = document.createDocumentFragment();

            const encabezados = ['ID', 'SKU', 'Proveedor', 'Fecha descarga', 'Descripción', 
            'No. Tarimas', 'Resto'];
            const ordenInformacion = ['id_contenedor', 'sku_producto', 'proveedor', 'fecha_descarga', 'descripcion', 'no_tarimas', 'resto_cajas'];
            let td = null;

            generarEncabezados(encabezados);
            datos.contenedores.forEach(informacion => {
                const fila = document.createElement("tr");
                ordenInformacion.forEach(columna => {
                    td = tipoColumna(columna, 'id_contenedor');
                    if (columna == 'descripcion'){
                        td.textContent = datos.descripcion;
                    } else {
                        td.textContent = informacion[columna];
                    }
                    fila.appendChild(td);            })
                fragmento.appendChild(fila);
            })
        tablaContenedor.appendChild(fragmento)
        } else if (datos.estado == 400) {
            mensajesModal('modalInput', "Error", 'Error dentro de la base de datos')
        } else if (datos.estado == 404) {
            mensajesModal('modalInput', "Error", 'Información no encontrada')
        }
    })
    .catch(error => {
        console.log("Error: ", error)
    })
})
