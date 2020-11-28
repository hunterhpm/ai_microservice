from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def init_app(app):
    global bcrypt
    bcrypt = Bcrypt(app)

