from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,EmailField,PasswordField
from wtforms.validators import DataRequired,Length,Email
from wtforms import SelectField

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

class contactsForm(FlaskForm):
    nombre = StringField("Nombre", validators=[
        DataRequired(),
        Length(max=25)
    ])
    email = EmailField("Email", validators=[
        DataRequired(),
        Length(min=11,max=25),
        Email()
    ])
    telefono = StringField("Telefono", validators=[
        DataRequired(),
        Length(min=9,max=9)
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