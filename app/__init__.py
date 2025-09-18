from flask import Flask

def crearApp():
    app = Flask(__name__)
    from .routes.routes import main
    from .routes.routes_contenedores import contenedores
    from .routes.routes_productos import productos
    
    app.register_blueprint(main)
    app.register_blueprint(contenedores)
    app.register_blueprint(productos)
    
    return app