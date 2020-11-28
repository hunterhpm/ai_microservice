from flask_jwt_extended import jwt_required

from project.server.decorators.authentification import admin_required
from project.server.handlers.database.users import register_user, get_current_user, get_user_list


def register():
    return register_user()


@jwt_required
def get_current():
    return get_current_user()


@admin_required
def get_list():
    return get_user_list()
