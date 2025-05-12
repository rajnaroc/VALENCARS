from flask import flash, request
from .models.User import User
from werkzeug.utils import secure_filename
import os
import shutil

class ModelUser:

    @classmethod
    def get_by_id(cls,db,id):
        try: 

            cur = db.connection.cursor()
            cur.execute("SELECT * FROM admin WHERE id = %s", (id,))
            data = cur.fetchone()

            if data:
                id = data[0]
                nombre = data[1]
                email = data[2]
                
                user = User(id, nombre, None, email)


                return user
            return None
        except Exception as e:
            print(e)


    @classmethod
    def register(cls, db, nombre, correo, contraseña, es_super_admin=False):
        try:
            cursor = db.connection.cursor()

            # Verificar si el correo ya existe
            cursor.execute("SELECT * FROM admin WHERE email = %s", (correo,))
            resultado = cursor.fetchone()

            if resultado is not None:
                print("Error: El correo ya está registrado en admin.")
                cursor.close()
                return False

            # Hashear la contraseña
            hashed_password = User.hash_password(contraseña)

            print(f"Contraseña hasheada: {hashed_password}")

            # Insertar el nuevo administrador
            cursor.execute(
                "INSERT INTO admin (nombre, email, contraseña, fecha_creacion, es_super_admin) "
                "VALUES (%s, %s, %s, NOW(), %s)",
                (nombre, correo, hashed_password, int(es_super_admin))
            )

            db.connection.commit()
            cursor.close()

            return True
        except Exception as e:
            print("Error al registrar administrador:", e)
            try:
                cursor.close()
            except:
                pass
            return False


    @classmethod
    def login(cls,db,email,password):
        try:
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM admin WHERE email = %s", (email,))
            data = cur.fetchone()

            if data:
                print(data)
                id = data[0]
                nombre = data[1]
                email = data[2]
                hashed_password = data[3]

                valor = User.check_password(hashed_password,password)
                if valor:
                    
                    user = User(id, None, None, email)
                    
                    return user
                return flash("error password")
            
        except Exception as e:
            print(e)

    # funcion para añadir el coche
    @classmethod
    def agregar_coche(cls,db,marca,modelo,año,precio,estado,descripcion,fecha_agregada,admin_id):
        try:
            cur = db.connection.cursor()
            cur.execute("INSERT INTO coches (marca,modelo,año,precio,estado,descripcion,fecha_agregado,admin_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(marca,modelo,año,precio,estado,descripcion,fecha_agregada,admin_id))
            db.connection.commit()

            
            coche_id = cur.lastrowid  # ← AQUÍ obtienes el ID del coche insertado
            cur.close()

            return coche_id

        except Exception as e:
            print(e)

    @classmethod
    def obtener_coches(cls,db):
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM coches WHERE EXISTS (SELECT 1 FROM fotos WHERE fotos.coche_id = coches.id)")
        coche = cur.fetchall()
        cur.close()
        
        return coche
    
    @classmethod
    def enviar_contacto(cls,db,nombre,email,telefono,motivo,descripcion):
        try:
            cur = db.connection.cursor()
            cur.execute("INSERT INTO mensajes (nombre,email,telefono,motivo,descripcion) VALUES (%s,%s,%s,%s,%s)",(nombre,email,telefono,motivo,descripcion))
            db.connection.commit()
            cur.close()

            return True

        except Exception as e:
            print(e)
    @classmethod
    def obtener_mensajes(cls,db):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM mensajes")
        mensajes = cursor.fetchall()
        cursor.close()
        return mensajes
    @classmethod
    def eliminar_mensaje(cls,db,id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("DELETE FROM mensajes WHERE id = %s", (id,))
            db.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    # @classmethod
    # def subir_foto(cls,db,ruta,):
    #     try:
    #         cur = db.connection.cursor()
    #         cur.execute("INSERT INTO fotos (nombre, ruta) VALUES (%s, %s)",(foto,id))
    #         db.connection.commit()
    #         cur.close()

    #         return True
    #     except Exception as e:
    #         print(e)
    #         return False