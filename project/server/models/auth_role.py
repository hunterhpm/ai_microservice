from flask_security import RoleMixin

from project.server.managers.database import db


class Role(db.Model, RoleMixin):
    """ User Model for storing user related details """
    __tablename__ = "auth_roles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Enum(
         'ADMIN',
         'CUSTOMER',
         name='role_name_type'
     ), unique=True)

    def from_json(self, json):
        self.id = json.get('role_id', None)
        self.name = json.get('name', None)
        return self

    def to_dictionary(self):
        return {
            'role_id': self.id,
            'name': self.name,
        }