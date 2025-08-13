from flask import Flask
from sqlalchemy import create_engine, text

baseDatos = create_engine(r'sqlite:///C:\Users\salva\Documents\Inbound_Web\Inbound_Manager-Web\app\static\db\productos.db')

def crearApp():
    app = Flask(__name__)
    from .routes import main
    
    app.register_blueprint(main)
    
    with baseDatos.connect() as connection:
        listaInformacion = []
        resultado = connection.execute(text('SELECT * FROM productos WHERE SKU="BB25C22"'))
        for row in resultado:
            print(row)
            listaInformacion.append(row)
        print("Descripcion: ", listaInformacion[0])
    return app