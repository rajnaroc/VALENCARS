from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,EmailField,PasswordField,SelectField
from wtforms.validators import DataRequired,Length,Email,Regexp

class loginform(FlaskForm):
    email = EmailField("Email", validators=[
        DataRequired(),
        Length(max=25),
        Email()
    ])
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=6,max=12)
    ])
    enviar = SubmitField("Iniciar sesion")

class registerform(FlaskForm):
    nombre = StringField("Nombre", validators=[
        DataRequired(),
        Length(max=25)
    ])
    email = EmailField("Email", validators=[
        DataRequired(),
        Length(min=11,max=25),
        Email()
    ])
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=6,max=12)
    ])
    es_super_admin = SelectField("Es super admin", choices=[
        ('0', 'No'),
        ('1', 'Si')
    ], validators=[DataRequired()])
    
    enviar = SubmitField("Registrar")

class contactsForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(),
        Length(min=2, max=50),
        Regexp('^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$', message="Solo letras y espacios.")
    ])
    email = StringField('Correo electrónico', validators=[
        DataRequired(),
        Email()
    ])
    telefono = StringField('Teléfono', validators=[
        DataRequired(),
        Regexp('^[0-9]{9}$', message="Debe tener 9 dígitos.")
    ])
    motivo = SelectField("Motivo", choices=[
        ('Comprar', 'Comprar'),
        ('Venta', 'Venta'),
    ], validators=[DataRequired()])
    
    descripcion = StringField("Descripcion", validators=[
        DataRequired(),
        Length(max=200)
    ])
    enviar = SubmitField("Enviar")