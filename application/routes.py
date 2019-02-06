from flask import request, render_template
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User


@app.route('/', methods=['GET'])
def entry():
    """Endpoint to create a user."""
    new_user = User(username='myuser2',
                    email='myuser2@example.com',
                    created=dt.now(),
                    bio="Because he's the hero Gotham deserves, but not the one it needs right now.",
                    admin=False
                    )
    db.session.add(new_user)
    db.session.commit()
    users = User.query.all()
    return render_template('users.html', users=users, title="Show Users")
