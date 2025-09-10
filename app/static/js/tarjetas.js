const tarjeta = document.querySelectorAll('.tarjeta');

  tarjeta.forEach(tarjeta => {
    tarjeta.addEventListener('mouseenter', () => {
      tarjeta.forEach(c => c.classList.add('hovered')); // aplica a todos
    });
    tarjeta.addEventListener('mouseleave', () => {
      tarjeta.forEach(c => c.classList.remove('hovered'));
    });
  });