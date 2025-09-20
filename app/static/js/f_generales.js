

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