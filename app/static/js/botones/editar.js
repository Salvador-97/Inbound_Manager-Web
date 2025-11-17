export function crearBoton(texto, tipoBoton){
    const boton = document.createElement('button');
    boton.classList.add('btn');
    boton.classList.add(tipoBoton);
    boton.setAttribute('type', 'submit')
    boton.setAttribute('name', texto)
    let fontawesome = '';

    switch (texto) {
        case 'editar':
            fontawesome = '<i class="fa-solid fa-pen" aria-hidden="true"></i>'
            break;
        case 'eliminar':
            fontawesome = '<i class="fa-solid fa-trash-can"></i>';
            boton.classList.add('mt-1')
            boton.classList.add('mt-lg-0')
            boton.classList.add('mx-lg-1')
            break;
        case 'actualizar': 
        fontawesome = '<i class="fa-solid fa-rotate"></i>'
        default:
            break;
    }

    boton.innerHTML = fontawesome;
    
    return boton;
}

