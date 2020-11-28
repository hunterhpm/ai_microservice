from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def init_app(app):
    global db
    db = SQLAlchemy(app)
