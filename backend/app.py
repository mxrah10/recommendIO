from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, send, emit
from dotenv import load_dotenv
import os
from db_creation import Anime, db

load_dotenv('pass.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    socketio.run(app, debug=True)

