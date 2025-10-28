# wsgi.py
from app import crearApp

app = crearApp()  # crea el objeto Flask

if __name__ == "__main__":
    app.run()