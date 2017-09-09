class MySQLConfig :
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/bitvision'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class MongoConfig :
    MONGODB_DB = 'bitvision'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
