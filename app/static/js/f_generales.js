

export function tipoColumna(columna, columaPrincipal){
    let td = null;
    if (columna == columaPrincipal){
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
            if (consultaInfo[i] == 'Opciones'){
                columna.textContent = consultaInfo[i];
                columna.id = 'editarBotones';
            } else {
                columna.textContent = consultaInfo[i];
            }
        } else {
            columna.textContent = consultaArrivo[i]
        }
        encabezado.appendChild(columna)
    }
}

export function generarEncabezados(encabezados){
    const titulos = document.getElementById('encabezado');

    titulos.innerHTML = "";

    for (let index = 0; index < encabezados.length; index++) {
        const columna = document.createElement('th');

        columna.textContent = encabezados[index]
        titulos.appendChild(columna);
    }
}