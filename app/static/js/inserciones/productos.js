import { mensajesModal } from "../f_generales.js";

const formularioNuevoProd = document.getElementById('form-nuevo-producto');

formularioNuevoProd.addEventListener('submit', function(e){
    e.preventDefault();

    const datosFormulario = new FormData(formularioNuevoProd);
    const datos = Object.fromEntries(datosFormulario.entries())

    console.log("Datos: ", datos)

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
        console.log("Datos: ", consulta)
        console.log("Estado: ", consulta.estado)
        const estadoForm = document.getElementById('barra-estado');
        const miModal = new bootstrap.Modal(document.getElementById("miModal"));
        const mensaje = document.getElementById('mensaje-Modal');
        const titulo = document.getElementById('miModalLabel');


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