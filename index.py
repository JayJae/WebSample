from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DatabaseConfig

app = Flask(__name__, static_foler="./static/dist", template_folder="./static")
app.config.from_object(DatabaseConfig)
db = SQLAlchemy(app)
