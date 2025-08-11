from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/contenedores')
def contenedores():
    return render_template('contenedores.html')

@main.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')