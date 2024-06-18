"""Flask configuration variables."""

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")
    APP_NAME = "flask_sqlalchemy_tutorial"

    # Flask Config
    FLASK_APP = "wsgi.py"
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SECRET_KEY = environ.get("SECRET_KEY")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


settings = Config
