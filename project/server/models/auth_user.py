import datetime

from flask_security import UserMixin
from sqlalchemy import ForeignKeyConstraint

from project.server.helpers.encrypter import encrypt_password
from project.server.managers.database import db
from project.server.models.auth_role import Role

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('auth_users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('auth_roles.id')),

)


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "auth_users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime(), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    company = db.Column(db.String(255))
    title = db.Column(db.String(255))
    language = db.Column(db.String(255), nullable=False)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'), post_update=True)

    def __init__(self, username, password, email, first_name, last_name, language='en', company=None,
                 title=None, admin=False, confirmed=False, confirmed_on=None):
        self.username = username
        self.password = encrypt_password(password)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.title = title
        self.language = language
        self.registered_on = datetime.datetime.now()
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on

        if admin:
            role = Role.query.filter_by(name='ADMIN').one()
            self.roles.append(role)
        else:
            role = Role.query.filter_by(name='CUSTOMER').one()
            self.roles.append(role)

    def from_partial_json(self, dictionary):
        super(User, self).from_partial_json(dictionary)
        if 'password' in dictionary:
            self.password = encrypt_password(dictionary.get('password'))
        self.registered_on = datetime.datetime.now()
        return self

    def from_json(self, json):
        self.id = json.get('user_id', None)
        self.email = json.get('email', None)
        self.password = json.get('password', None)
        self.first_name = json.get('first_name', None)
        self.last_name = json.get('last_name', None)
        return self

    def to_dictionary(self):
        obj = {
            'user_id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'registered_on': self.registered_on,
            'confirmed': self.confirmed,
            'confirmed_on': self.confirmed_on,
            'company': self.company,
            'title': self.title,
            'language': self.language,
            'roles': [role.name for role in self.roles],
        }
        return obj
