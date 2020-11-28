# project/tests/test_auth.py

import json
import time
import unittest

from project.server.managers.database import db
from project.server.models.auth_user import User
from project.server.models.auth_blacklist_token import BlacklistToken
from project.tests.helpers import login_user, register_user, logout_user, authDict, login_new_user
from project.tests.base import BaseTestCase


class TestAuthBlueprint(BaseTestCase):
    def test_registration(self):
        """ Test for user registration """
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_registered_with_already_registered_user(self):
        """ Test registration with already registered email"""
        user = User(
            username='joe',
            email='joe@gmail.com',
            password='test',
            first_name='Joe',
            last_name='Test',
        )
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'username_already_used')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_registered_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # registered user login
            response = login_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_non_registered_user_login(self):
        """ Test for login of non-registered user """
        with self.client:
            response = login_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'invalid_user')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

    def test_registered_user_invalid_password_login(self):
            """ Test for login of registered-user login """
            with self.client:
                # user registration
                register_user(self)
                # registered user login
                response = login_user(self, password='test')
                data = json.loads(response.data.decode())
                self.assertTrue(data['status'] == 'fail')
                self.assertTrue(data['message'] == 'invalid_user')
                self.assertTrue(response.content_type == 'application/json')
                self.assertEqual(response.status_code, 404)

    def test_get_user(self):
        """ Test for user status """
        with self.client:
            resp_login = login_new_user(self)

            response = self.client.get(
                '/v1/users/me',
                headers=authDict(resp_login)
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(data['data']['username'] == 'joe')
            self.assertTrue(data['data']['email'] == 'joe@gmail.com')
            self.assertTrue(data['data']['first_name'] == 'Joe')
            self.assertTrue(data['data']['last_name'] == 'Test')
            self.assertEqual(response.status_code, 200)

    def test_valid_logout(self):
        """ Test for logout before token expires """
        with self.client:
            # user login
            resp_login = login_new_user(self)
            # valid token logout
            response = logout_user(self, resp_login)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(response.status_code, 200)

    def test_invalid_logout(self):
        """ Testing logout after the token expires """
        with self.client:
            # user registration
            resp_login = login_new_user(self)
            # invalid token logout
            time.sleep(6)
            response = logout_user(self, resp_login)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'The token has expired')
            self.assertEqual(response.status_code, 401)

    def test_valid_blacklisted_token_logout(self):
        """ Test for logout after a valid token gets blacklisted """
        with self.client:
            # user registration
            resp_login = login_new_user(self)
            # blacklist a valid token
            blacklist_token = BlacklistToken(
                token=json.loads(resp_login.data.decode())['data']['auth_token'])
            db.session.add(blacklist_token)
            db.session.commit()
            # blacklisted valid token logout
            response = logout_user(self, resp_login)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(response.status_code, 201)

    def test_user_status_malformed_bearer_token(self):
        """ Test for user status with malformed bearer token"""
        with self.client:
            resp_login = login_new_user(self)
            response = self.client.get(
                '/v1/users/me',
                headers=dict(
                    Authorization='Bearer' + json.loads(
                        resp_login.data.decode()
                    )['data']['auth_token'] + 'a'
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Signature verification failed')
            self.assertTrue(data['error'] == 'invalid_token')
            self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
