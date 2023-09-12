from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length

class RegistrarClienteForm(FlaskForm):
    username = StringField("Username:", validators=[
        InputRequired(message="El campo de usuario es obligatorio")
    ])
    password = PasswordField("Password:", validators=[
        InputRequired(message="El campo de contraseña es obligatorio"),
        Length(min=6, message="La contraseña debe tener al menos 6 caracteres")
    ])
    email = StringField("Email:", validators=[
        InputRequired(message="El campo de correo electrónico es obligatorio"),
        Email(message="Ingrese una dirección de correo electrónico válida")
    ])
    submit = SubmitField("Registrar")
