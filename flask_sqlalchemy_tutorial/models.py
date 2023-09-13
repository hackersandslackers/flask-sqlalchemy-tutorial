"""Data models."""
from . import db


class User(db.Model):
    """User account data model."""

    __tablename__ = "flasksqlalchemy-tutorial-users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    bio = db.Column(db.Text, nullable=True)
    admin = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f"<User id={self.id}, username={self.username}, email={self.email}>"
