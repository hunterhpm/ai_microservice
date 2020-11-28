from flask_mail import Message


def send_email(to, subject, template):
    from project.server import app
    from project.server.managers.mail import mail

    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)