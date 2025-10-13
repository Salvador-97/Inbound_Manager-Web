import { mensajesModal } from "../f_generales.js";
import { reglasRegex, validacionInputColor, validarCampo } from "./validacionDatos.js";

const formularioNuevoProd = document.getElementById('form-nuevo-producto');

formularioNuevoProd.addEventListener('submit', function(e){
    e.preventDefault();

    const datosFormulario = new FormData(formularioNuevoProd);
    const datos = Object.fromEntries(datosFormulario.entries())
    console.log("Datos: ", datos)

    const inputRegex = {"skuProducto": reglasRegex.skuProducto, "descripcion": reglasRegex.nombre, "codigo_barras": reglasRegex.codigoBarras, "producto_tarima": reglasRegex.cajas, "cajas_tarima": reglasRegex.cajas, "master_pack": reglasRegex.masterPack};

    const inputs = Object.entries(inputRegex);
    let validacion = false;


    inputs.forEach(([key, valor]) => {
        const checkInput = validarCampo(datos[key], valor);
        if (checkInput) {
            validacionInputColor(checkInput, document.querySelector(`input[name=${key}]`))
        } else {
            validacion = validacionInputColor(checkInput, document.querySelector(`input[name=${key}]`))
        }
    })

    if (validacion) {
        mensajesModal('modalInput', "Error", "Revise los datos introducidos")
        return;
    }
    fetch('/api/productos/nuevo', {
        method: "POST",
        body: datosFormulario
    })
    .then(response => response.json())
    .then(consulta => {

        if (consulta.estado == 400){
            // mensajesModal('miModal', 'Error', '¡El SKU del producto ya existe!')
        } else if (consulta.estado == 200) {
            // mensajesModal('miModal', 'Exito', 'Producto agregado exitosamente');
        }
    })
    .catch(error => {
        console.error(error)
    })
})