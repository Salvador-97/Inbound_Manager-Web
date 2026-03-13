# 📦️ Inbound Manager Web

![Badge en Desarollo](https://img.shields.io/badge/estado-desarrollo-green)
![Badge de Versión](https://img.shields.io/badge/version-1.0.0-blue)

Gestor de arrivo de mercancia a traves de contenedores.
Este sistema permite la gestión y registro de los productos que llegan a un almacen a traves de la generación de información como lo es el número de tarimas que se general despues de la descarga de un contenedor, asignandoles un "ID" para poder identificar cada una y así poder despues asignarles una ubicación dentro del almacen. 

Con esto se permite tener un mejor control de la mercancia que ingresa facilitando su movimento dentro del almacen.

## Objetivo del proyecto
- Facilitar y tener un mejor control del ingreso de mercancia y su posterior ubicacion dentro del almacen, optimizando el tiempo de captura de información y de la integridad del inventario fisico y virtual.

## Alcance
- 
- 

## Tecnologias
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Fetch API](https://img.shields.io/badge/Fetch_API-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Sass](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)

## Arquitectura del sistema
- 

## Flujo de trabajo
### Flujo principal
1. Busqueda del producto que llega en el contenedor para recuperar su información.
2. Agregar datos como el id del contenedor, el proveedor, tarimas totales y resto, 
3. Se generan id's para cada una de las tarimas que se suben a la base de datos para esperar que se les asigne una ubicación.

### Flujo secundario
- Alta y edición de productos
- Búsqueda de tarimas y contenedores
- Reasignación de ubicaciones

## Modelo de datos
- 

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

![Nuevo contenedor](/app/static/img/Nuevo_Contenedor.png)

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

## Limitaciones conocidas
- 

## Motivación
- 


## Autores
[<img src="https://avatars.githubusercontent.com/Salvador-97" width=115><br><sub>Salvador Gutiérrez Olvera</sub>](https://github.com/Salvador-97)