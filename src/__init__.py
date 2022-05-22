import os

from flask import Flask
from flask_migrate import Migrate
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


app = Flask(__name__)
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

db.init_app(app)
Migrate(app, db)
from src.api import api

api.init_app(app)


class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}
