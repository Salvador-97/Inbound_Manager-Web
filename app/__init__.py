from flask import Flask
from sqlalchemy import create_engine, text

def crearApp():
    app = Flask(__name__)
    from .routes import main
    
    app.register_blueprint(main)
    
    return app