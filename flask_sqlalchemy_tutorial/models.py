"""Data models."""
from . import db


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'flasksqlalchemy-tutorial-users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    bio = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)
