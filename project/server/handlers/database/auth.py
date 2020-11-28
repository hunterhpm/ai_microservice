from datetime import datetime

import itsdangerous
from flask import request, jsonify
from flask_jwt_extended import create_access_token, verify_jwt_in_request
from itsdangerous import URLSafeTimedSerializer

from project.server import app
from project.server.controllers.v1 import errors
from project.server.helpers.auth import get_auth_token, send_confirmation_email
from project.server.managers.bcrypt import bcrypt
from project.server.managers.database import db
from project.server.models.auth_blacklist_token import BlacklistToken
from project.server.models.auth_user import User


def __confirm_token(token, expiration=None):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except itsdangerous.exc.SignatureExpired:
        return False
    return email


def confirm_user_email():
    post_data = request.get_json()

    try:
        email = __confirm_token(post_data['token'], expiration=3600)
    except Exception as e:
        return errors.forbidden('invalid_confirmation_token')

    if isinstance(email, str):
        user = User.query.filter_by(
            email=email
        ).first()

        user.confirmed = True
        user.confirmed_on = datetime.now()

        db.session.add(user)
        db.session.commit()

        return jsonify({
            'status': 'success',
        }), 200

    return errors.forbidden('expired_confirmation_token')


def resend_email_confirmation():
    post_data = request.get_json()

    try:
        email = __confirm_token(post_data['token'])

        send_confirmation_email(app, email)
    except Exception as e:
        return errors.forbidden('invalid_confirmation_token')
    return jsonify({
        'status': 'success',
    }), 200


def login_user():
    post_data = request.get_json()
    try:
        # fetch the user data
        user = User.query.filter_by(
            username=post_data.get('username')
        ).first()
        if user and bcrypt.check_password_hash(
                user.password, post_data.get('password')
        ):
            if user.confirmed:
                auth_token = create_access_token(identity=user)
                if auth_token:
                    return jsonify({
                        'status': 'success',
                        'data': {
                            'auth_token': auth_token
                        }
                    }), 200
            else:
                return errors.forbidden('email_not_confirmed')
        else:
            return errors.not_found('invalid_user')
    except Exception as e:
        print(e)
        return errors.server_error('Try again')


def logout_user():
    auth_token = get_auth_token(request)

    if auth_token:
        verify_jwt_in_request()

        # check if user already exists
        existing_blacklisted_token = BlacklistToken.query.filter_by(token=auth_token).first()

        if existing_blacklisted_token:
            # insert the token
            return jsonify({
                'status': 'success',
            }), 201

        try:
            # mark the token as blacklisted
            blacklist_token = BlacklistToken(token=auth_token)

            # insert the token
            db.session.add(blacklist_token)
            db.session.commit()

            return jsonify({
                'status': 'success',
            }), 200
        except Exception as e:
            return errors.server_error(e)
    else:
        return errors.forbidden('Provide a valid auth token.')
