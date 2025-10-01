import { mensajesModal } from "../f_generales.js";

const formularioNuevoProd = document.getElementById('form-nuevo-producto');

formularioNuevoProd.addEventListener('submit', function(e){
    e.preventDefault();

    const datosFormulario = new FormData(formularioNuevoProd);
    const datos = Object.fromEntries(datosFormulario.entries())

    console.log("Datos: ", datos)

    // Agregar funcion que valide cada uno de los datos ingresados

    if (datos.skuProducto){
        const estado = document.getElementById('barra-estado');
        // estado.style.borderColor = "#F54927"
    }


    fetch('/api/productos/nuevo', {
        method: "POST",
        body: datosFormulario
    })
    .then(response => response.json())
    .then(consulta => {

        if (consulta.estado == 400){
            mensajesModal('miModal', 'Error', '¡El SKU del producto ya existe!')
        } else if (consulta.estado == 200) {
            mensajesModal('miModal', 'Exito', 'Producto agregado exitosamente');
        }
    })
    .catch(error => {
        console.error(error)
    })
})