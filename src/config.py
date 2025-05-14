import os
class Config:
    SECRET_KEY=os.getenv("SECRET_KEY")


class ProductionConfig(Config):
    DEBUG=False
    MYSQL_HOST=os.getenv("MYSQL_HOST")
    MYSQL_USER=os.getenv("MYSQL_USER")
    MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD")
    MYSQL_DB=os.getenv("MYSQL_DB")
    UPlOAD_FOLDER='static/img'

class DevelopConfig(Config):
    DEBUG=True
    MYSQL_HOST=os.getenv("MYSQL_HOST")
    MYSQL_USER=os.getenv("MYSQL_USER")
    MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD")
    MYSQL_DB=os.getenv("MYSQL_DB")
    UPlOAD_FOLDER='static/img'

config = {
    "dev" : DevelopConfig,
    "produ" : ProductionConfig
}