from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(app)
    app.config.from_object('config.Config')

    with app.app_context():
        # Imports
        from . import routes

        # Create tables for our models
        db.create_all()

        return app
