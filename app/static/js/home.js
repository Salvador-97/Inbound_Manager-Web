const datosTarjetas = [
    {
        titulo: "Maneja tu almacen",
        imagen: "deposito.gif",
        texto: "Esta plataforma está diseñada para facilitar el control de entradas de mercancía en la empresa. Desde aquí se centraliza la información relacionada con contenedores, productos y su distribución dentro del almacén, asegurando un registro ordenado y accesible.",
        linkBoton: "/contenedores"
    },
    {
        titulo: "Contenedores",
        imagen: "container.gif",
        texto: "La sección de contenedores permite registrar cada arribo, identificando su número, fecha y la información detallada de la carga que transporta. De esta forma se lleva un control puntual sobre lo que ingresa, evitando errores y garantizando trazabilidad en todo momento.",
        linkBoton: "/contenedores"
    },
    {
        titulo: "Productos y almacén",
        imagen: "existencias.gif",
        texto: "Cada producto descargado de los contenedores recibe su registro de entrada en el sistema. Posteriormente, se asigna su ubicación en el almacén, lo que facilita la organización, la búsqueda y la correcta administración del inventario.",
        linkBoton: "/producto"
    }
]

const contenedor = document.getElementById("contenedor-tarjetas");
const tarjeta = document.getElementById("tarjeta-inicio");

datosTarjetas.forEach(datos => {
    const cloneTarjeta = tarjeta.content.cloneNode(true)
    cloneTarjeta.querySelector(".titulo").textContent = datos.titulo;
    cloneTarjeta.querySelector(".texto").textContent = datos.texto;
    cloneTarjeta.querySelector(".imagen").src = `/static/img/${datos.imagen}`;
    cloneTarjeta.querySelector(".link").href = datos.linkBoton;
    contenedor.appendChild(cloneTarjeta)
})