const busquedaSKU = document.getElementById('form-sku');

busquedaSKU.addEventListener('submit', function(e) {
    e.preventDefault()

    const datosForm = new FormData(busquedaSKU);
    const parametros = new URLSearchParams(datosForm);

    fetch(`/api/contenedores/arrivo?${parametros.toString()}`, {
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
    .then(consulta => {       
        const datosProducto = ['sku_producto', 'nombre', 'codigoBarras', 'cajas', 'piezas', 'masterPack'];

        datosProducto.forEach(informacion => {
            const input = document.querySelector(`input[name=${informacion}]`);
            if (input) {
                input.value = consulta.producto[informacion];
            }
        })
         const inputs = ['sku_producto', 'descripcion', 'codigo_barras', 'producto_tarima', 'cajas_tarima', 'master_pack'];
    })
    .catch(error => {
        console.log(error)
    })
})

const formularioContenedor = document.getElementById('form-ctn');

formularioContenedor.addEventListener('submit', function(e) {
    e.preventDefault();

    const datosForm = new FormData(formularioContenedor);
    const sku = document.getElementById('sku_producto').value;
    datosForm.set('skuProducto', sku);
    datosForm.append('ubicacion', "S/U");

    const datos = Object.fromEntries(datosForm.entries());

    console.log("Datos: ", datos)
    fetch('/api/contenedores/arrivo', {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(estado => {

    })
    .catch(error => {
        console.log(error)
    })
})