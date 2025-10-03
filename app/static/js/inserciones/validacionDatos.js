export const reglasRegex = {
    "skuProducto": /[A-Z][A-Z][1-9][0-9]*[0-9]*C[1-9][0-9]*/,
    "id_proveedor": /P0[0-9][0-9]/,
    "id_ctn": /[A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9][0-9][0-9]/,
    "codigoBarras": /^[0-9]{13}$/,
    "masterPack": /^([0-9]+|N\/A)$/,
    "piezas": /[1-9][0-9]*$/,
    "cajas": /[1-9][0-9]*$/,
    "resto": /[1-9][0-9]*$/,
    "ubicacion": /^([0-9]+|S\/U)$/,
    "nombre": /^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ.,*\- ]+$/,
    "no_tarimas": /[1-9][0-9]*$/,
    "fecha_descarga": /^\d{4}-\d{2}-\d{2}$/
}

export function validarCampo(input, reglaRegex) {
    return reglaRegex.test(input)
}

export function validacionAdvertencia(input, tipoError){
    if (input.value == ""){
        input.classList.add(tipoError);
    }
}

export function validacionInputColor(check, input){
    if (check) {
        if (input.classList.contains('error')){
            input.classList.remove('error');
        }
        input.classList.add('check');
    }
    else {
        if (input.classList.contains('check')){
            input.classList.remove('check');
        }
        input.classList.add('error');
        return true
    }
}