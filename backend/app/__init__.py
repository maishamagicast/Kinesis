from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.api import register_routes

def create_app(config_class=Config):
    app=Flask(__name__,static_folder=Config.STATIC_FOLDER)
    app.config.from_object(config_class)
    CORS(app,resources={r"/api/*":{"origins":config_class.CORS_ORIGINS}}) #allows CORS to work with specific urls instead of all of them
    register_routes(app)
    return app