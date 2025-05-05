from math import log
from flask import Flask, app, request, jsonify, render_template, redirect, url_for, session, flash
from forms import loginform, contactsForm
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)


@app.route("/", methods=["GET"])
def catalogo():
    return render_template("catalogo.html")

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
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html", form=loginForm)

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.config.from_object(config["dev"])
    app.run()
