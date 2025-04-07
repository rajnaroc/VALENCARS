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

@app.route("/coche", methods=["GET"])
def coche():
    return render_template("coche.html")


if __name__ == '__main__':
    app.run(debug=True)
