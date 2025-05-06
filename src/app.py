from flask import Flask, app, request, jsonify, render_template, redirect, url_for, session, flash
from forms import loginform, contactsForm, registerform
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from config import config
from flask_mysqldb import MySQL
from entities.ModelUser import ModelUser
from utils.security import Security

app = Flask(__name__)

db = MySQL(app)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)
    

@app.route("/", methods=["GET"])
def catalogo():
    return render_template("catalogo.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    registerForm = registerform()
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["email"]
        contraseña = request.form["password"]
        es_super_admin = request.form.get("es_super_admin", False)
        
        if ModelUser.register(db, nombre, correo, contraseña, es_super_admin):
            flash("Usuario registrado con éxito", "success")
            return redirect(url_for("login"))
        else:
            flash("Error al registrar el usuario", "danger")
    
    return render_template("register.html", form=registerForm)

@app.route("/contacto", methods=["GET"])
def contacto():
    contactForm = contactsForm()
    if request.method == "POST":
        if contactForm.validate_on_submit():
            nombre = contactForm.nombre
            email = contactForm.email
            telefono = contactForm.telefono
            motivo = contactForm.motivo
            descripcion = contactForm.descripcion
            # Aquí podrías agregar la lógica para enviar el formulario o guardarlo en una base de datos
            flash("Formulario enviado con éxito", "success")
    return render_template("contacto.html", form=contactForm)

@app.route("/somos", methods=["GET"])
def somos():
    return render_template("somos.html")

@app.route("/vender", methods=["GET"])
def vender():
    return render_template("vender.html")

@app.route("/coche")
def coche():
    # Datos del coche
    images = [
        'img/Coche_img.png',
        'img/contacto.png',
        'img/foto.jpg'
    ]
    labels = ["Año", "Combustible", "Kilómetros", "Motor", "Color", "Consumo", "Cambio", "Puertas/Plazas"]
    values = ["Junio 2020", "Gasolina-GLP", "90.278 km", "1000 / 101 C.V.", "Blanco", "5.3 l / 100", "Manual", "4 puertas / 5 plazas"]
    datos = zip(labels, values)
    return render_template("coche.html", datos=datos, images=images)


@app.route("/inicio", methods=["GET"])
def inicio():
    return render_template("inicio.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = loginform()

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        logged_user = ModelUser.login(db, email, password)
        if logged_user:
            login_user(logged_user)
            jwt_token = Security.generate_token(logged_user)
            return redirect(url_for("panel"))
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html", form=loginForm)


@app.route("/panel", methods=["GET", "POST"])
def panel():
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return redirect(url_for("login"))
        return render_template("panel.html")
    
    if request.method == "POST":
        marca = request.form["marca"].strip()
        modelo = request.form["modelo"].strip()
        año = request.form["año"].strip()
        precio = request.form["precio"].strip()
        estado = request.form["estado"].strip()
        descripcion = request.form["marca"]
        ModelUser.agregar_coche(db,marca,modelo,año,precio,estado,descripcion,None,current_user.id)
        return redirect(url_for("panel"))


@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template("404.html"), 404

@app.route("/cerrar_sesion", methods=["GET"])
def logout():
    logout_user()
    flash("Logged out successfully", "success")
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.config.from_object(config["dev"])
    app.run()
