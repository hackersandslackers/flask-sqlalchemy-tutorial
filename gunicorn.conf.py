"""Gunicorn configuration file."""

from os import environ, path

from dotenv import load_dotenv

# Read environment variables from ".env" file.
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Fetch deployment environment from environment variables.
ENVIRONMENT = environ.get("ENVIRONMENT")

proc_name = "flasksqlalchemy"
wsgi_app = "wsgi:app"
bind = ["127.0.0.1:8009"]
threads = 2
workers = 2
access_log_format = "%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"

if ENVIRONMENT == "development" or ENVIRONMENT is None:
    reload = True
    workers = 1
    threads = 1
elif ENVIRONMENT == "production":
    accesslog = "/var/log/flasksqlalchemy/access.json"
    errorlog = "/var/log/flasksqlalchemy/error.json"
else:
    raise ValueError(f"Unknown environment provided: `{ENVIRONMENT}`. Must be `development` or `production`.")
