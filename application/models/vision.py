from flask_mongoengine.wtf import model_form
from app import mongodb

class Vision(mongodb.Document) :
    room_id = mongodb.StringField(required=True)
    invest_list = mongodb.ListField(
                    mongodb.EmbeddedDocumentField(Invest))

class Invest(mongodb.EmbeddedDocument) :
    invest_range = mongodb.IntField(required=True)
    invest_info = mongodb.ListField(
                        mongodb.EmbeddedDocumentField(Info))

class Info(mongodb.EmbeddedDocument) :
    email = mongodb.StringField(required=True)
    coin = mongodb.FloatField(required=True)
