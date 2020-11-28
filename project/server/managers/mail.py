from flask_mail import Mail

mail = Mail()


def init_app(app):
    global mail
    mail = Mail(app)
