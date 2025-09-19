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
        const ordenInformacion = ['sku_producto', 'descripcion', 'piezas', 'cajas', 'fecha', 'contenedor', 'ubicacion']
        
        datos.productos.forEach(informacion => {
            const fila = document.createElement("tr");

            ordenInformacion.forEach(columna => {
                const td = document.createElement("td");

                if (columna == 'descripcion'){
                    td.textContent = datos.descripcion;
                } else {
                    td.textContent = informacion[columna];
                }
                fila.appendChild(td);
            })
            fragmento.appendChild(fila);
        })
        tbody.appendChild(fragmento);
    })
    .catch(error => {
        console.log("Error: ", error)
    })
})