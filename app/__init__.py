import os
from flask import Flask

def crearApp():
    app = Flask(__name__)
    from .routes.routes import main
    from .routes.routes_contenedores import contenedores
    from .routes.routes_contenedores import apiContenedores
    from .routes.routes_productos import productos
    from .routes.routes_ubicaciones import ubicaciones
    
    app.register_blueprint(main)
    app.register_blueprint(contenedores)
    app.register_blueprint(apiContenedores, url_prefix='/api/contenedores')
    app.register_blueprint(productos)
    app.register_blueprint(ubicaciones)
    
    ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "static", "db", "almacen.db"))
    print("Ruta absoluta de la DB:", ruta_db)

    if os.path.exists(ruta_db):
        print("✅ El archivo existe.")
        size = os.path.getsize(ruta_db)
        print(f"Tamaño del archivo: {size} bytes")
        if size < 1000:
            print("⚠️  El archivo parece estar vacío o recién creado.")
    else:
        print("❌ No se encontró la base de datos en esa ruta.")
    
    return app