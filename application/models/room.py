from app import mysqldb

class Room :
    room_id = mysqldb.Column(mysqldb.String(64), primary_key=True)
    min_coin = mysqldb.Column(mysqldb.Float)
    start_price = mysqldb.Column(mysqldb.Float)
    end_price = mysqldb.Column(mysqldb.Float)
    start_date = mysqldb.Column(mysqldb.DateTime)
    end_date = mysqldb.Column(db.DateTime)

    def __init__(self, room_id, min_coin, start_price, end_price,
                 start_date, end_date) :
        self.room_id = room_id
        self.min_coin = min_coin
        self.start_price = start_price
        self.end_price = end_price
        self.start_date = start_date
        sefl.end_date = end_date


