import json

def authDict(response):
    return dict(
        Authorization='Bearer ' + json.loads(
            response.data.decode()
        )['data']['auth_token']
    )

def login_user(self, username='joe', password='password'):
    return self.client.post(
        '/v1/auth/login',
        data=json.dumps(dict(
            username=username,
            password=password
        )),
        content_type='application/json',
    )


def logout_user(self, response):
    return self.client.post(
        '/v1/auth/logout',
        headers=authDict(response)
    )

def register_user(self, username='joe', email='joe@gmail.com', password='password', first_name='Joe', last_name='Test',
                  admin=False):
    return self.client.post(
        '/v1/users/register',
        data=json.dumps(dict(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            admin=admin
        )),
        content_type='application/json',
    )

def login_new_user(self, username='joe', email='joe@gmail.com', password='password', first_name='Joe', last_name='Test',
                  admin=False):
    register_user(self, username=username, email=email, password=password, first_name=first_name, last_name=last_name, admin=admin)
    return login_user(self, username, password)