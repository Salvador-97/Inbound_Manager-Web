import os
from dotenv import load_dotenv
from flask import Blueprint, render_template
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

main = Blueprint('main', __name__, template_folder='app/templates')

# Conexion PostgreSQL
load_dotenv()

url = URL.create(
    "postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

basePostgreSQL = create_engine(url)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')