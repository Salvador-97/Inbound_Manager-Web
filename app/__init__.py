from flask import Flask

def crearApp():
    app = Flask(__name__)
    from .routes import main
    
    app.register_blueprint(main)
    
    return app