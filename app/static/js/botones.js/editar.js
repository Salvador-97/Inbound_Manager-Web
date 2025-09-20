export function crearBoton(texto, tipoBoton){
    const boton = document.createElement('button');
    boton.classList.add('btn');
    boton.classList.add(tipoBoton);
    boton.setAttribute('type', 'button')

    if (texto == 'editar'){
        boton.innerHTML = '<i class="fa-solid fa-pen" aria-hidden="true"></i>'
    } else if (texto == 'eliminar'){
        boton.innerHTML = '<i class="fa-solid fa-trash-can"></i>'
        boton.style.marginLeft = '0.6em';
    }
    
    return boton;
}

