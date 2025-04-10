from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,EmailField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo

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

class registerForm(FlaskForm):
    fullname = StringField("fullname", validators=[
        DataRequired(),
        Length(min=4)
    ])
    email = EmailField("email", validators=[
        DataRequired(),
        Length(max=25),
        Email()
    ])
    password = PasswordField("password", validators=[
        DataRequired(),
        Length(min=6,max=12),
        EqualTo("confirme",message="Repite la contrasela")
    ])
    confirme = PasswordField("confirme", validators=[
        DataRequired(),
        Length(min=6, max=12)
    ])
    enviar = SubmitField("Register")

class contactsForm(FlaskForm):
    img = StringField("img", validators=[
        DataRequired()
    ])
    descripcion = StringField("descripcion", validators=[
        DataRequired()
    ])
    enviar = SubmitField("agregar")