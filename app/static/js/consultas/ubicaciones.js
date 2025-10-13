import { generarEncabezados, tipoColumna } from "../f_generales.js"
import { crearBoton } from "../botones/editar.js"

const formularioUbicaciones = document.getElementById("form-sku-ubicaciones")

formularioUbicaciones.addEventListener('submit', function(e) {
    e.preventDefault()

    const datosForm = new FormData(formularioUbicaciones)
    const parametros = new URLSearchParams(datosForm)

    fetch(`/api/productos/ubicaciones?${parametros.toString()}`, {
        method: 'GET'
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
        const tabla = document.getElementById('contenido-tabla');
        const fragmento = document.createDocumentFragment();

        tabla.innerHTML = "";

        const ordenInformacion = ['sku_producto', 'descripcion', 'piezas', 'cajas', 'fecha', 'ubicacion']
        const encabezados = ['SKU', 'Descripción', 'Producto/Tarima', 'Cajas', 'Fecha', 'Ubicación', 'Opciones'];
        generarEncabezados(encabezados)

        datos.ubicaciones.forEach(informacion => {
            const fila = document.createElement('tr');
            ordenInformacion.forEach(columnas => {
                const celda = tipoColumna(columnas, 'sku_producto')
                if (columnas == 'descripcion'){
                    celda.textContent = datos.descripcion;
                } else {
                    if (columnas == 'cajas'){
                        celda.setAttribute('name', 'cajas')
                    }
                    celda.textContent = informacion[columnas]
                }
                fila.appendChild(celda);
            })

            const celdaOpciones = document.createElement('td');
            const boton = crearBoton('editar', 'btn-primary')
            const boton2 = crearBoton('eliminar', 'btn-danger');

            celdaOpciones.appendChild(boton);
            celdaOpciones.appendChild(boton2);

            fila.appendChild(celdaOpciones);

            fragmento.appendChild(fila);
        })
        tabla.appendChild(fragmento);
    })
    .catch(error => {
        console.log("Error: ", error)
    });
})