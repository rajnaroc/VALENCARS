import datetime
import pytz
from jwt import decode, encode
from decouple import config

class Security():

    secret = config("JWT_KEY")
    tz = pytz.timezone('Europe/Spain/Madrid')

    @classmethod
    def generate_token(cls, authenticated_user):
        payload = {
            'iat':datetime.datetime.now(tz=cls.tz),
            'exp':datetime.datetime.now(tz=cls.tz)+datetime.timedelta(minutes=10),
            'username':authenticated_user.username,
            'fullname':authenticated_user.fullname,
        }

        return encode(payload,cls.secret, algorithm='HS256')
