from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,EmailField,PasswordField
from wtforms.validators import DataRequired,Length,Email
from wtforms import SelectField

class loginform(FlaskForm):
    email = EmailField("email", validators=[
        DataRequired(),
        Length(max=25),
        Email()
    ])
    password = PasswordField("password", validators=[
        DataRequired(),
        Length(min=6,max=12)
    ])
    enviar = SubmitField("Iniciar sesion")

class contactsForm(FlaskForm):
    nombre = StringField("nombre", validators=[
        DataRequired(),
        Length(max=25)
    ])
    email = EmailField("email", validators=[
        DataRequired(),
        Length(max=25),
        Email()
    ])
    telefono = StringField("telefono", validators=[
        DataRequired(),
        Length(max=12)
    ])
    motivo = SelectField("motivo", choices=[
        ('Comprar', 'Comprar'),
        ('Venta', 'Venta'),
    ], validators=[DataRequired()])
    
    descripcion = StringField("descripcion", validators=[
        DataRequired(),
        Length(max=100)
    ])
    enviar = SubmitField("enviar")