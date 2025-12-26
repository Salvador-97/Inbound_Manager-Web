

export function tipoColumna(columna, columaPrincipal) {
    let td = null;
    if (columna == columaPrincipal) {
        td = document.createElement("th");
        return td;
    } else {
        td = document.createElement("td");
        return td;
    }
}

export function generarEncabezadosTabla(tipoConsulta) {
    const consultaArrivo = ['SKU', 'Descripción', 'Piezas', 'Cajas', 'Fecha', 'Contenedor', 'Ubicación']
    const consultaInfo = ['SKU', 'Descripción', 'Código Barras', 'Piezas', 'Cajas', 'Master Pack', 'Opciones']
    const encabezado = document.getElementById('encabezado')
    let tamañoEncabezado = 0

    encabezado.innerHTML = ""

    if (tipoConsulta == 'editar') {
        tamañoEncabezado = consultaInfo.length;
    } else {
        tamañoEncabezado = consultaArrivo.length;
    }

    for (let i = 0; i < tamañoEncabezado; i++) {
        const columna = document.createElement('th');

        if (tipoConsulta == 'editar') {
            if (consultaInfo[i] == 'Opciones') {
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

export function generarEncabezados(encabezados) {
    const titulos = document.getElementById('encabezado');

    titulos.innerHTML = "";

    for (let index = 0; index < encabezados.length; index++) {
        const columna = document.createElement('th');

        columna.textContent = encabezados[index]
        titulos.appendChild(columna);
    }
}

export function mensajesModal(modal, titulo, mensaje) {
    const miModal = new bootstrap.Modal(document.getElementById(modal));
    const tituloSelect = document.getElementById('miModalLabel');
    const mensajeSelect = document.getElementById('mensaje-Modal');


    tituloSelect.textContent = titulo;
    if (mensaje == 'input') {
        mensajeSelect.innerHTML = `<form action="" id="form-ubicacion">
                            <div class="form-group">
                            <input type="text" class="form-control input-ubicacion" id="ubicacion" name="ubicacion" form="form-ubicacion">
                            </div>
                            </form>`;
    } else {
        mensajeSelect.textContent = mensaje;
    }

    miModal.show();
}

export function navBuscar() {
    const botonNav = document.querySelector('[name="select-btn"]');
    const inputSelect = document.getElementById('select');
    const menuOpciones = document.querySelector(".nav-opciones");

    console.log("botonNav: ", botonNav)

    botonNav.addEventListener('click', e => {
        if (menuOpciones.classList.contains("mostrar")) {
            menuOpciones.classList.remove("mostrar");
        } else {
            menuOpciones.classList.add('mostrar')
            menuOpciones.addEventListener('click', e => {
                const boton = e.target.closest('button');
                const selectBoton = document.querySelector('[name="select-ctn"]');
                const textoSelect = document.querySelector('.texto-select');

                if (!boton) return;
                menuOpciones.classList.remove("mostrar");

                inputSelect.value = boton.value;
                textoSelect.textContent = boton.textContent;
            })
        }
    })
}