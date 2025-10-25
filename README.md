# 📦️ Inbound Manager Web

Gestor de arrivo de contenedores, con generación de tarimas y manejo de 
ubicaciones.

![Badge en Desarollo](https://img.shields.io/badge/estado-desarrollo-green)
![Badge de Versión](https://img.shields.io/badge/version-1.0.0-blue)

## Funcionalidades
- Ingreso de contenedores por su ID (Ej. VHRT5679125)
  - Asignación de productos que contiene
  - Creación de tarimas de acuerdo a la información del usuario
  - Creación de id para cada tarima
- Manejo de los productos del almacen.
  - Agregar nuevo producto
  - Editar su información
- Control de las ubicaciones de las tarimas de cada contenedor
  - Asignación de ubicaciones por id de tarima

### Proximas funcionalidades
- Creación de roles de usuario
- Importar/Exportar en archivo Excel
- Filtros de busqueda
- Vista de todas las ubicaciones y lo que contienen

## Requisitos
- Python 3.11.1
- Flask
- SQLAlchemy

## Instalación

```bash 
$ git clone https://github.com/Salvador-97/Inbound_Manager-Web.git`
$ cd Inbound_Manager-Web
$ pip install -r requirements.txt
$ python app.py
```
Ingresa a la url `http://127.0.0.1:5000/`

## Secciones del proyecto
### Contenedores
Páginas donde se muestra la parte de agregar un nuevo contenedor y la información requerida para darlo de alta.

![Nuevo contenedor](/app/static/img/Nuevo_Contenedor.PNG)

Información mostrada del contenedor que se ha buscado.

![Buscar contenedor](/app/static/img/Buscar_Contenedor.PNG)

### Productos
Página para dar de alta un nuevo producto y los datos necesarios.

![Nuevo producto](/app/static/img/Nuevo_Producto.PNG)

![Buscar producto](/app/static/img/Buscar_Producto.PNG)

### Ubicaciones
Página donde se busca un producto y se despliegan todos sin importar de que contenedor sean, mostrando si tiene una ubicación asignada y su identificador.

![Ver ubicaciones](/app/static/img/Ubicaciones.PNG)

Se pueden poner los filtros de mostrar todos aquellos que ya tiene o no una ubicación.

![Productos con ubicaciones](/app/static/img/Mostrar_Ubicacion.PNG)

Al presionar el botón de editar se despliega un modal para agregar la nueva ubicación que tendra esa tarima.

![Nueva ubicacion](/app/static/img/Nuevo_Ubicacion.PNG)

## Autores
[<img src="https://avatars.githubusercontent.com/Salvador-97" width=115><br><sub>Salvador Gutiérrez Olvera</sub>](https://github.com/Salvador-97)