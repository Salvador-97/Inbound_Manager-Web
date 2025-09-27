export function crearBoton(texto, tipoBoton){
    const boton = document.createElement('button');
    boton.classList.add('btn');
    boton.classList.add(tipoBoton);
    boton.setAttribute('type', 'button')
    let fontawesome = '';
    let marginLeft = '0'

    switch (texto) {
        case 'editar':
            fontawesome = '<i class="fa-solid fa-pen" aria-hidden="true"></i>'
            break;
        case 'eliminar':
            fontawesome = '<i class="fa-solid fa-trash-can"></i>';
            marginLeft = '0.6em';
            break;
        case 'actualizar': 
        fontawesome = '<i class="fa-solid fa-rotate"></i>'
        default:
            break;
    }

    boton.innerHTML = fontawesome;
    boton.style.marginLeft = marginLeft;
    
    return boton;
}

