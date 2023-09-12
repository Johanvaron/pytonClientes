from flask import Blueprint

clientes = Blueprint('clientes',
                     __name__,
                     url_prefix='/clientes',
                     template_folder='templates',
                     static_folder='imagenes')

# Vincula el archivo de rutas de clientes
from . import routes
