from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,EmailField,PasswordField,SelectField
from wtforms.validators import DataRequired,Length,Email,Regexp

class loginform(FlaskForm):
    email = EmailField("Email", validators=[
        DataRequired(message="El campo Email es obligatorio."),
        Length(max=25, message="El Email no puede tener más de 25 caracteres."),
        Email(message="Debes introducir un correo válido.")
    ])
    password = PasswordField("Password", validators=[
        DataRequired(message="La contraseña es obligatoria."),
        Length(min=6, max=12, message="La contraseña debe tener entre 6 y 12 caracteres.")
    ])
    enviar = SubmitField("Iniciar sesión")

class registerform(FlaskForm):
    nombre = StringField("Nombre", validators=[
        DataRequired(message="El nombre es obligatorio."),
        Length(max=25, message="El nombre no puede superar los 25 caracteres.")
    ])
    email = EmailField("Email", validators=[
        DataRequired(message="El correo electrónico es obligatorio."),
        Length(min=11, max=25, message="El correo debe tener entre 11 y 25 caracteres."),
        Email(message="Introduce un correo válido.")
    ])
    password = PasswordField("Password", validators=[
        DataRequired(message="La contraseña es obligatoria."),
        Length(min=6, max=12, message="La contraseña debe tener entre 6 y 12 caracteres.")
    ])
    es_super_admin = SelectField("¿Es super admin?", choices=[
        ('0', 'No'),
        ('1', 'Sí')
    ], validators=[DataRequired(message="Debes seleccionar una opción.")])
    
    enviar = SubmitField("Registrar")


class contactsForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message="El nombre es obligatorio."),
        Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres."),
        Regexp('^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$', message="El nombre solo puede contener letras y espacios.")
    ])
    email = StringField('Correo electrónico', validators=[
        DataRequired(message="El correo electrónico es obligatorio."),
        Email(message="Introduce un correo válido.")
    ])
    telefono = StringField('Teléfono', validators=[
        DataRequired(message="El teléfono es obligatorio."),
        Regexp('^[0-9]{9}$', message="El teléfono debe tener exactamente 9 dígitos.")
    ])
    motivo = SelectField("Motivo", choices=[
        ('Comprar', 'Comprar'),
        ('Venta', 'Venta'),
    ], validators=[DataRequired(message="Selecciona un motivo.")])
    
    descripcion = StringField("Descripción", validators=[
        DataRequired(message="La descripción es obligatoria."),
        Length(max=200, message="La descripción no puede superar los 200 caracteres.")
    ])
    enviar = SubmitField("Enviar")
