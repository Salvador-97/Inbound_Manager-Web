import { generarEncabezados, tipoColumna } from '../f_generales.js'

const busquedaCTN = document.getElementById("form_ctn_busqueda");
busquedaCTN.addEventListener('submit', function(e) {
    e.preventDefault();

    const infoFormulario = new FormData(busquedaCTN);
    const parametros = new URLSearchParams(infoFormulario);
    console.log("Parametros:" , parametros.toString())

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
        console.log("Datos: ", datos)

        const tablaContenedor = document.getElementById('tablaContenedor');
        tablaContenedor.innerHTML = "";

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

    })
    .catch(error => {
        console.log("Error: ", error)
    })
})
