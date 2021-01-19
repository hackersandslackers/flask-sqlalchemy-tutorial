"""Initialize Flask app."""
import uptrace
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

upclient = uptrace.Client(dsn="")


db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    FlaskInstrumentor().instrument_app(app)

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Create database tables for our data models

        SQLAlchemyInstrumentor().instrument(
            engine=db.engine,
            service="database",
        )

        return app
