from flask_testing import TestCase

from project.server import app
from project.server.config.config import TestingConfig
from project.server.managers.database import db
from project.server.models.auth_role import Role


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object(TestingConfig)
        return app

    def setUp(self):
        db.create_all()
        admin = Role(name='ADMIN')
        customer = Role(name='CUSTOMER')
        db.session.add(admin)
        db.session.add(customer)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.reflect()
        db.drop_all()
