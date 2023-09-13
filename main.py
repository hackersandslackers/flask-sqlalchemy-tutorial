"""App entry point."""
from flask_sqlalchemy_tutorial import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8089, debug=False, load_dotenv=True)
