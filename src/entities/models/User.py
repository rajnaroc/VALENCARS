from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash

class User(UserMixin):
    
    def __init__(self,fullname,email,password):
        self.fullname = fullname
        self.email = email
        self.password = password


    @classmethod
    def check_password(cls,hashed_password,password):
        check_password_hash(hashed_password,password)
    
    @classmethod
    def hash_password(cls,password):
        generate_password_hash(password)

    
