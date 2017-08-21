
class DatabaseConfig(object) :
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/websample'
    SQLALCHEMY_TRACH_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


