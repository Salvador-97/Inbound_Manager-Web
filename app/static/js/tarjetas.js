const tarjeta = document.querySelectorAll('.tarjeta');

tarjeta.forEach(tarjetas => {
  tarjetas.addEventListener('mouseover', function() {
    const icono = tarjetas.querySelector('i');
    const titulo = tarjetas.querySelector('h4')

    if (icono) {icono.classList.add('colorTarjeta');}
    if (titulo) {titulo.classList.add('colorTarjeta');}

  })
  tarjetas.addEventListener('mouseout', function() {
    const icono = tarjetas.querySelector('i');
    const titulo = tarjetas.querySelector('h4');

    if (icono) {icono.classList.remove('colorTarjeta');}
    if (titulo) {titulo.classList.remove('colorTarjeta');}
  })
})