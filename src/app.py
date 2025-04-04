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

if __name__ == '__main__':
    app.run(debug=True)