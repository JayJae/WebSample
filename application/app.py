from flask import request, render_template, jsonify, url_for, redirect, g
from models.room import Room
from models.user import User
from models.vision import Vision
from models.result import Result
from index import app, mysqldb, mongodb

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')
