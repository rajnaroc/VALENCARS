from flask import Flask, app, request, jsonify, render_template, redirect, url_for, session, flash, make_response
from forms import loginform, contactsForm, registerform
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from config import config
from flask_mysqldb import MySQL
from entities.ModelUser import ModelUser
from utils.security import Security
from werkzeug.utils import secure_filename
import os
import shutil
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

db = MySQL(app)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)
    

    
@app.route("/", methods=["GET"])
def catalogo():
    # Aquí puedes obtener los coches de la base de datos y pasarlos al template
    coches = ModelUser.obtener_coches(db)
    for i in coches:
        print(i)
    return render_template("catalogo.html",coches=coches)

@app.route("/solicitudes", methods=["GET"])
def solicitudes():
    if not current_user.is_authenticated:
        return redirect("/")
    
    solicitudes = ModelUser.obtener_mensajes(db)
    return render_template("mensajes_admin.html", solicitudes=solicitudes)

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

@app.route("/contacto", methods=["POST", "GET"])
def contacto():

    contactForm = contactsForm()
    
    if request.method == "POST":
            if contactForm.validate_on_submit():
                nombre = request.form["nombre"]
                email = request.form["email"]
                telefono = request.form["telefono"]
                motivo = request.form["motivo"]
                descripcion = request.form["descripcion"]
                
                ModelUser.enviar_contacto(db, nombre, email, telefono, motivo, descripcion)
                return redirect(url_for("contacto"))
            else:
                flash("Error al enviar el mensaje", "danger")
                return render_template("contacto.html", form=contactForm)
    if request.method == "GET":
        return render_template("contacto.html", form=contactForm)

@app.route("/mensaje/<int:id>", methods=["GET"])
def eleminar_mensaje(id):
    if not current_user.is_authenticated:
        return redirect("/")
    
    ModelUser.eliminar_mensaje(db, id)
    flash("Mensaje eliminado con éxito", "success")
    return redirect(url_for("ver_mensajes"))

@app.route("/mensaje", methods=["GET"])
def ver_mensajes():
    if not current_user.is_authenticated:
        return redirect("/")
    
    mensajes = ModelUser.obtener_mensajes(db)
    
    return render_template("mensajes_admin.html", mensajes=mensajes)


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
            jwt_token = Security.generate_token(logged_user)
            login_user(logged_user)
            response = make_response(redirect(url_for("panel")))
            response.set_cookie("jwt_token", jwt_token, httponly=True, secure=True, samesite="Lax")
            return response
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html", form=loginForm)


@app.route("/panel", methods=["GET", "POST"])
def panel():
    token = request.cookies.get("jwt_token")
    has_access = Security.verify_token(token)

    if not has_access:
        flash("Sesion no válida. Inicia sesion nuevamente", "warning")
        return redirect(url_for("login"))
    if request.method == 'GET':
        print(current_user.is_authenticated)
        if not current_user.is_authenticated:
            return redirect(url_for("login"))
        return render_template("panel.html")
        
    if request.method == "POST":
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        precio_contado = request.form.get('precio_contado')
        precio_financiado = request.form.get('precio_financiado')
        ano = request.form.get('ano')
        consumo = request.form.get('consumo')
        combustible = request.form.get('combustible')
        cambio = request.form.get('cambio')
        kilometros = request.form.get('kilometros')
        puertas = request.form.get('puertas')
        plazas = request.form.get('plazas')
        motor = request.form.get('motor')
        comentario = request.form.get('comentario')
        color = request.form.get('color')
        
        id_coche = ModelUser.agregar_coche(db, marca, modelo, precio_contado, precio_financiado, ano,
                                            consumo, combustible, cambio, kilometros, puertas,
                                            plazas, motor, comentario, color, current_user.id)
        
        
        carpeta_temp = os.path.join("static/temp", str(current_user.id))
        carpeta_final = os.path.join("static/uploads", str(id_coche))
        os.makedirs(carpeta_final, exist_ok=True)

        for foto_nombre in os.listdir(carpeta_temp):
            origen = os.path.join(carpeta_temp, foto_nombre)
            destino = os.path.join(carpeta_final, foto_nombre)
            os.rename(origen, destino)

            ruta_relativa = os.path.relpath(destino)  # o solo el nombre del archivo
            cursor = db.connection.cursor()
            cursor.execute("INSERT INTO fotos (id_coche, ruta_foto) VALUES (%s, %s)", (id_coche, ruta_relativa))
            db.connection.commit()
            cursor.close()

        # Eliminar carpeta temporal del usuario
        os.rmdir(carpeta_temp)

        return redirect(url_for("panel"))
    else:
        return jsonify({"error": "Unauthorized"}), 401
    

@app.route("/subir_foto_temp", methods=["POST"])
def subir_foto_temp():
    foto = request.files.get("foto")
    if not foto:
        return jsonify({"error": "No se recibió ninguna foto"}), 400

    user_id = current_user.id
    carpeta_temp = os.path.join("static/temp", str(user_id))
    os.makedirs(carpeta_temp, exist_ok=True)
    
    filename = secure_filename(foto.filename)
    ruta_foto = os.path.join(carpeta_temp, filename)
    foto.save(ruta_foto)

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
