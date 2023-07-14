from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv('pass.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    tags = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    continuity = db.Column(db.String(255), nullable=False)
    image = db.Column(db.LargeBinary)

with app.app_context():
    db.create_all()
