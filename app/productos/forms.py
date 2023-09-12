from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms.validators import InputRequired,NumberRange



class RegistrarProductoForm(FlaskForm):
    nombre = StringField("Nombre del producto:", validators =[InputRequired(message = "No sea tonto mk escriba un nombre:")])
    precio = IntegerField("Precio del producto:",validators =[InputRequired(message = "Precio Requerido") ,
                                                              NumberRange(message="Precio fuera del rango", 
                                                                          min = 10, 
                                                                          max =10000)])
    
    
    
    
    imagen = FileField("Selecione la imagen del producto:" ,
                       validators=[FileRequired(message="Debe selecionar una imagen"),
                                   FileAllowed(['jpg','png'],
                                               "Solo se permiten imagenes")])
    
    submit = SubmitField("Guardar")