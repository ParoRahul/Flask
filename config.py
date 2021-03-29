import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".config"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_ENV = os.environ.get("FLASK_ENV")

    # Database
    APPLICATON_DIR = os.path.dirname(os.path.abspath(__file__))
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(APPLICATON_DIR, "application", "static", "image")

    # Production and Development Specific Environment
    if os.environ.get("FLASK_ENV") == "production":
        TESTING = False
        DEBUG = False
        SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI")
    else:
        TESTING = True
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")
