from project.server import app
from project.server.managers.bcrypt import bcrypt


def encrypt_password(password):
    return bcrypt.generate_password_hash(
        password, app.config.get('BCRYPT_LOG_ROUNDS')
    ).decode()
