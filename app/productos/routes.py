from flask import render_template
from . import productos
import app
from .forms import RegistrarProductoForm
import os
#Rutas del Modulo productos
@productos.route("/listar")
def listar():
    #Listar los productos utilizando modelos
    productos = app.models.Producto.query.all()
    return render_template("index.html",
                           productos = productos)

@productos.route("/nuevo", 
                 methods = ["GET", "POST"])
def nuevo():
    #Definir el formulario
    form = RegistrarProductoForm()
    #Definir el objeto producto
    p = app.models.Producto()
    if form.validate_on_submit():
        form.populate_obj(p)
    #alterar nombre de imagen
        p.imagen = form.imagen.data.filename   
        app.db.session.add(p)
        app.db.session.commit()
        #return os.getcwd()
        #Extraer el objeto FileStorage
        file = form.imagen.data
        file.save (os.path.abspath(os.getcwd() 
                                  + "/app/productos/imagenes/" +
                                 form.imagen.data.filename))
        
        return "Producto Registrado"
    
    return render_template("new.html",
                           form = form)