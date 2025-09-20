

export function tipoColumna(columna){
    let td = null;
    if (columna == 'sku_producto'){
        td = document.createElement("th");
        return td;
    } else {
        td = document.createElement("td");
        return td;
    }
}

export function generarEncabezadosTabla(tipoConsulta){
    const consultaArrivo = ['SKU', 'Descripción', 'Piezas', 'Cajas', 'Fecha', 'Contenedor', 'Ubicación']
    const consultaInfo = ['SKU', 'Descripción', 'Código Barras', 'Piezas', 'Cajas', 'Master Pack', 'Opciones']
    const encabezado = document.getElementById('encabezado')
    let tamañoEncabezado = 0

    encabezado.innerHTML = ""
    
    if (tipoConsulta == 'editar'){
        tamañoEncabezado = consultaInfo.length;
    } else {
        tamañoEncabezado = consultaArrivo.length;
    }

    for(let i = 0; i < tamañoEncabezado; i++){
        const columna = document.createElement('th');

        if (tipoConsulta == 'editar'){
            columna.textContent = consultaInfo[i]
        } else {
            columna.textContent = consultaArrivo[i]
        }
        encabezado.appendChild(columna)
    }
}