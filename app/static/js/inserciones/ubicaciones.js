import { mensajesModal } from "../f_generales.js";

document.addEventListener('click', e => {
    const boton = e.target.closest('[name="editar"]');
    if (boton){
        e.preventDefault();
        mensajesModal('modalUbicacion', 'Nueva ubicación', 'input')

        const botonAgregar = document.getElementById('form-ubicacion');

        botonAgregar.addEventListener('submit', e => {
            e.preventDefault();
            
            const sku = document.getElementById('sku_producto').value;
            const cajas = document.querySelector('[name="cajas"]');
            const datosForm = new FormData(botonAgregar);

            datosForm.append('skuProducto', sku);
            datosForm.append('cajas', cajas.textContent)

            fetch('/api/productos/ubicaciones', {
                method: 'POST',
                body: datosForm
            })
            .then(response => response.json())
            .then(estado => {
                console.log("Estado: ", estado.estado)
                if (estado.estado == 400) {
                    console.log("Error: ", estado.error)
                }
            })
            .catch(error => {
                console.log(error)
            })
        })
    }
})