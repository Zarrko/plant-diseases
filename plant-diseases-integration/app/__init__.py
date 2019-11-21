from flask import Flask, jsonify
from .config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy()
migrate = Migrate(app, db)

from app.api.images import webapp

