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
        console.log("DATOS: ", datos)

        const fila = document.createElement("tr");

        // 2. Crear celdas <td> para cada campo
        const tdSku = document.createElement("td");
        tdSku.textContent = datos.sku;

        fila.appendChild(tdSku)
        document.getElementById("tabla").appendChild(fila);

    })
    .catch(error => {
        console.log("Error: ", error)
    })
})