from datetime import datetime

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from sqlalchemy import or_

from project.server import app
from project.server.controllers.v1 import errors
from project.server.helpers.auth import send_confirmation_email
from project.server.helpers.serialize import get_json_clean_response
from project.server.managers.database import db
from project.server.models.auth_user import User


def register_user():
    # get the post data
    post_data = request.get_json()

    # check if user already exists
    user = User.query.filter(
        or_(
            User.username == post_data.get('username'),
            User.email == post_data.get('email')
        )
    ).first()

    if not user:
        try:
            user = User(
                username=post_data.get('username'),
                password=post_data.get('password'),
                email=post_data.get('email'),
                first_name=post_data.get('first_name'),
                last_name=post_data.get('last_name'),
                admin=post_data.get('admin')
            )

            if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
                send_confirmation_email(app, user.email)
            else:
                user.confirmed = True
                user.confirmed_on = datetime.now()

            # insert the user
            db.session.add(user)
            db.session.commit()

            return jsonify({
                'status': 'success',
                'data': {
                    'user': user.to_dictionary(),
                }
            }), 201
        except Exception as e:
            errors.unauthorized(e)
    else:
        message = 'user_already_exists'
        if user.username == post_data.get('username'):
            message = 'username_already_used'
        elif user.email == post_data.get('email'):
            message = 'email_already_used'

        return errors.bad_request(message=message)


def get_current_user():
    username = get_jwt_identity()
    if isinstance(username, str):
        user = User.query.filter_by(username=username).first()
        return jsonify({
            'status': 'success',
            'data': {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'registered_on': user.registered_on
            }
        }), 200

    return errors.unauthorized(message='login_required')


def get_user_list():
    users = get_json_clean_response(User.query.all())
    return jsonify({
        'status': 'success',
        'data': {
            'users': users
        }
    }), 200
