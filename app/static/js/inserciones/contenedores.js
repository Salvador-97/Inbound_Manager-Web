import { validarCampo, reglasRegex, validacionInputColor, validacionAdvertencia } from "./validacionDatos.js";
import { mensajesModal } from "../f_generales.js";

const busquedaSKU = document.getElementById('form-sku');

busquedaSKU.addEventListener('submit', function (e) {
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
            if (!response.ok) {
                return response.json().then(datos => {
                    mensajesModal('modalInputError', `Error ${response.status}`, datos.mensaje);
                })
            }
            return response.json()
        })
        .then(consulta => {
            console.log("Datos: ", consulta)

            if (consulta) {
                const datosProducto = ['sku_producto', 'descripcion', 'codigo_barras', 'cajas_por_tarima', 'piezas', 'piezas_por_caja'];

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
            }
        })
        .catch(error => {
            console.log(error)
        })
})

const formularioContenedor = document.getElementById('form-ctn');

formularioContenedor.addEventListener('submit', function (e) {
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
        .then(response => {
            if (!response.ok) {
                return response.json().then(datos => {
                    mensajesModal('modalInputError', `Error ${response.status}`, datos.mensaje);
                })
            } else if (response.ok) {
                return response.json().then(datos => {
                    mensajesModal('modalInputError', '', datos.mensaje);
                })
            }
            return response.json()
        })
        .catch(error => {
            console.log(error)
        })
})