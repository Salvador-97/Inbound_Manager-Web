from flask import Flask
from flask_assets import Environment, Bundle

def crearApp():
    app = Flask(__name__)
    
    assets = Environment(app)
    scss = Bundle('styles/sass/home.scss', filters='libsass', output='styles/css/home.css')
    assets.register('scss_all', scss)
    
    from .routes.routes import main
    from .routes.routes_contenedores import contenedores
    from .routes.routes_contenedores import apiContenedores
    from .routes.routes_productos import productos
    from .routes.routes_productos import apiProductos
    from .routes.routes_ubicaciones import ubicaciones
    from .routes.routes_ubicaciones import apiUbicaciones
    
    app.register_blueprint(main)
    app.register_blueprint(contenedores)
    app.register_blueprint(apiContenedores, url_prefix='/api/contenedores')
    app.register_blueprint(productos)
    app.register_blueprint(apiProductos, url_prefix='/api/producto')
    app.register_blueprint(ubicaciones)
    app.register_blueprint(apiUbicaciones, url_prefix='/api/ubicaciones')
    
    return app