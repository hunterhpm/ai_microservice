from flask_jwt_extended import jwt_required

from project.server.handlers.database.auth import login_user, logout_user, confirm_user_email, resend_email_confirmation


def login():
    return login_user()


@jwt_required
def logout():
    return logout_user()


def confirm_email():
    return confirm_user_email()


def resend_confirmation():
    return resend_email_confirmation()
