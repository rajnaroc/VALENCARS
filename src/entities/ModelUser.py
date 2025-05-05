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
    def login(cls,db,email,password):
        try:
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM admin WHERE email = %s", (email,))
            data = cur.fetchone()

            if data:
                id = data[0]
                password = data[2]
                email = data[3]
                valor = User.check_password(password,user.password)
                if valor:
                    user = User(id,None,email)

                    return user
                return print("error password")
            
        except Exception as e:
            print(e)