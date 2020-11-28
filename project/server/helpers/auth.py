from flask import render_template
from itsdangerous import URLSafeTimedSerializer

from project.server.helpers.mail import send_email


def check_blacklist(auth_token):
    # check whether auth token has been blacklisted
    from project.server.models.auth_blacklist_token import BlacklistToken
    res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
    if res:
        return True
    else:
        return False


def get_auth_token(request):
    # get auth token
    auth_header = request.headers.get('Authorization')
    if auth_header:
        return auth_header.split(" ")[1]
    else:
        return ''


def generate_confirmation_token(app, email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


def send_confirmation_email(app, email):
    if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
        token = generate_confirmation_token(app, email)
        confirm_url = app.config['UI_URL'] + '/auth/confirm?token=' + token
        html = render_template('users/activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(email, subject, html)
