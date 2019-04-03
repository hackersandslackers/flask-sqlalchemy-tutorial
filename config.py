import os


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
