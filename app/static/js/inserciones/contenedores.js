import { validarCampo, reglasRegex, validacionInputColor, validacionAdvertencia } from "./validacionDatos.js";
import { mensajesModal } from "../f_generales.js";

const busquedaSKU = document.getElementById('form-sku');

busquedaSKU.addEventListener('submit', function(e) {
    e.preventDefault()

    const datosForm = new FormData(busquedaSKU);
    const parametros = new URLSearchParams(datosForm);

    const checkSku = validarCampo(datosForm.get('sku_producto'), reglasRegex.skuProducto);
    const input = document.getElementById('sku_producto');
    
    validacionInputColor(checkSku, input);

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
        console.log("Consulta: ", consulta)

        if (consulta.estado == 200){
        const datosProducto = ['sku_producto', 'nombre', 'codigoBarras', 'cajas', 'piezas', 'masterPack'];

        datosProducto.forEach(informacion => {
            const input = document.querySelector(`input[name=${informacion}]`);
            if (input) {
                input.value = consulta.producto[informacion];
            }
        })
        
        const inputs = ['nombre', 'codigoBarras', 'piezas', 'cajas', 'masterPack'];
        inputs.forEach(validacion => {
            const input = document.querySelector(`input[name=${validacion}]`);
            validacionAdvertencia(input, 'advertencia');
        })
        } else if (consulta.estado == 404) {
            mensajesModal('modalInputError', '404', consulta.producto);

        } else if (consulta.estado == 400) {
            mensajesModal('modalInputError', 'Error', 'Error dentro de la base de datos');
        }
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
    let sinErrores = true

    datosForm.forEach((valor, clave) => {
        if (reglasRegex[clave]) {
            const input = document.querySelector(`input[name=${clave}]`);
            if (input) {
                const check = validarCampo(valor, reglasRegex[clave]);
                const validacion = validacionInputColor(check, input);

                if (validacion) {
                    sinErrores = false;
                }
            }
        }
    })

    if (!sinErrores) {
        mensajesModal('modalInputError', 'Error datos', 'Uno o más campos estan incorrectos.')
        return
    }

    fetch('/api/contenedores/arrivo', {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(estado => {
        if (estado.error){
            console.log("Error: ", estado.error)
            if((estado.error).includes('UNIQUE')) {
                const input = document.querySelector('input[name=id_ctn]');

                validacionInputColor(false, input);
                mensajesModal('modalInputError', 'Error contenedor', 'ID contenedor repetido')

            } else {
                mensajesModal('modalInputError', 'Error', 'Error al insertar en base de datos.')

            }
        } else if (estado.estado == 200) {
            mensajesModal('modalInputError', 'Exito', 'Contenedor agregado correctamente')
        }
    })
    .catch(error => {
        console.log(error)
    })
})