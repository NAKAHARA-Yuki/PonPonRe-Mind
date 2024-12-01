from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# データベース設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.controllers import main_controller
