from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
from config import MySQLConfig, MongoConfig

app = Flask(__name__, static_folder="./static/dist", template_folder="./static")

app.config.from_object(MySQLConfig)
mysqldb = SQLAlchemy(app)

app.config.from_object(MongoConfig)
mongodb = MongoEngine(app)
