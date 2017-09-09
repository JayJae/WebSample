from app import mysqldb

class User(mysqldb.Model) :
    email = mysqldb.Column(mysqldb.String(120), primary_key=True)
    nickname = mysqldb.Column(mysqldb.String(120), unique=True)
    wallet = mysqldb.Column(mysqldb.String(120), unique=True)

    def __init__(self, email, nickname, wallet) :
        self.email = email
        self.nickname = nickname
        self.wallet = wallet
