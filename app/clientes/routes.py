from flask import Flask, render_template, request
from . import clientes  # Asumiendo que "clientes" es tu Blueprint
from .forms import RegistrarClienteForm  # Importa el formulario adecuado
import os 

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('registro_cliente.html')

# Ruta para registrar un cliente
@app.route('/registrar_cliente', methods=['GET', 'POST'])
def registrar_cliente():
    form = RegistrarClienteForm()  # Crea una instancia del formulario
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        # Aquí puedes hacer lo que necesites con los datos del cliente
        # Por ejemplo, puedes guardarlos en la base de datos.

        return "Cliente registrado exitosamente"

    return render_template("nuwclientes.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
