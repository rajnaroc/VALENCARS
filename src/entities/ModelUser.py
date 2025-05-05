from .models.User import User

class ModelUser:

    @classmethod
    def get_by_id(cls,db,id):
        try: 

            cur = db.connection.cursor()
            cur.execute("SELECT * FROM users WHERE id = %s", (id,))
            data = cur.fetchone()

            if data:
                id = data[0]
                fullname = data[1]
                email = data[3]
                
                user = User(id,fullname,None,email)

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
    def register(cls, db, username, password, fullname):

        try:
            hushed_pass = User.hush_password(password)
            cursor = db.connection.cursor()
            cursor.execute('INSERT INTO user (username, password, fullname) VALUES (%s, %s, %s)', (username, str(hushed_pass) , fullname))
            db.connection.commit()
        
        except Exception as e:
            
            raise Exception(e)
        
    @classmethod
    def login(cls,db,email,password):
        try:
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM admin WHERE email = %s", (email,))
            data = cur.fetchone()

            if data:
                id = data[0]
                password = data[3]
                email = data[2]
                valor = User.check_password(password,user.password)
                if valor:
                    user = User(id,None,email)
                    return user
                return print("error password")
            
        except Exception as e:
            print(e)