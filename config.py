import os


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = os.environ["TESTING"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    FLASK_DEBUG = os.environ["FLASK_DEBUG"]

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    # SQLALCHEMY_ECHO = os.environ["SQLALCHEMY_ECHO"]
    # SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]
