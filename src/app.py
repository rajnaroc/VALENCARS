from turtle import st
from flask import Flask, app, request, jsonify, render_template, redirect, url_for, session, flash


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("catalogo.html")

@app.route("/contacto", methods=["GET"])
def contacto():
    return render_template("contacto.html")

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




if __name__ == '__main__':
    app.run(debug=True)
