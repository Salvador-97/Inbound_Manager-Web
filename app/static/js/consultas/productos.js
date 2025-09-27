import { tipoColumna, generarEncabezadosTabla } from "../f_generales.js"
import { crearBoton } from "../botones.js/editar.js";

const formulario = document.getElementById("form-sku-busqueda");
formulario.addEventListener('submit', function(e) {
    e.preventDefault();

    const infoFormulario = new FormData(formulario);
    const parametros = new URLSearchParams(infoFormulario);
    console.log("Parametros:" , parametros.toString())

    fetch(`/api/productos/infoproducto?${parametros.toString()}`, {
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
        const tbody = document.getElementById("tabla"); 
        tbody.innerHTML = "";

        const fragmento = document.createDocumentFragment();

        if (datos.tipo == 'editar'){
            generarEncabezadosTabla(datos.tipo)

            const fila = document.createElement("tr");
            const ordenInformacion = ['sku_producto', 'nombre', 'codigoBarras', 'piezas', 'cajas', 'masterPack']
            let td = null

            ordenInformacion.forEach(columna => {
                td = tipoColumna(columna, 'sku_producto')
                td.textContent = datos.producto[columna]
                fila.appendChild(td);
            })

            const tdBoton = document.createElement('td')
            const boton = crearBoton('editar', 'btn-primary')
            const boton2 = crearBoton('eliminar', 'btn-danger');
            tdBoton.appendChild(boton)
            tdBoton.appendChild(boton2)
            fila.appendChild(tdBoton)

            tbody.appendChild(fila);
        } else {
            generarEncabezadosTabla(datos.tipo)

            datos.productos.forEach(informacion => {
                const fila = document.createElement("tr");
                const ordenInformacion = ['sku_producto', 'descripcion', 'piezas', 'cajas', 'fecha', 'contenedor', 'ubicacion']
                ordenInformacion.forEach(columna => {
                    const td = tipoColumna(columna)
                    if (columna == 'descripcion'){
                        td.textContent = datos.descripcion.nombre;
                    } else {
                        td.textContent = informacion[columna];
                    }
                    fila.appendChild(td);
                })
                fragmento.appendChild(fila);
            })
        tbody.appendChild(fragmento);
        }
    })
    .catch(error => {
        console.log("Error: ", error)
    })
})
