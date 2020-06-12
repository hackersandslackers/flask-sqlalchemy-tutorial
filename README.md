# Flask-SQLAlchemy Tutorial

![Python](https://img.shields.io/badge/Python-v^3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-2.4.1-red.svg?longCache=true&style=flat-square&logo=flask&logoColor=white&colorA=4c566a&colorB=5e81ac)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/flask-sqlalchemy-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/flask-sqlalchemy-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/flask-sqlalchemy-tutorial.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=Github)](https://github.com/hackersandslackers/flask-sqlalchemy-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/flask-sqlalchemy-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/flask-sqlalchemy-tutorial/network)

![Flask-SQLAlchemy Tutorial](https://raw.githubusercontent.com/hackersandslackers/flask-sqlalchemy-tutorial/master/application/static/img/flask-sqlachemy-github.jpg)

Connect your Flask app to a database using Flask-SQLAlchemy. This repository contains source code for the accompanying tutorial on [Hackers and Slackers](https://hackersandslackers.com/manage-database-models-with-flask-sqlalchemy/).

## Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/hackersandslackers/flask-sqlalchemy-tutorial.git
$ cd flask-sqlalchemy-tutorial
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ flask run
```

**Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)**:

```shell
$ git clone https://github.com/hackersandslackers/flask-sqlalchemy-tutorial.git
$ cd flask-sqlalchemy-tutorial
$ pipenv shell
$ pipenv update
$ flask run
```

## Usage

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
* `FLASK_ENV`: The environment to run your app in (either `development` or `production`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `SQLALCHEMY_DATABASE_URI`: SQLAlchemy connection URI to a SQL database.

*Remember never to commit secrets saved in .env files to Github.*

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
