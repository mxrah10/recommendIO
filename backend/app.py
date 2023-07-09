from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    socketio.run(app, debug=True)

