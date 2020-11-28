# project/server/tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from project.server import app
from project.server.config import config


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object(config.DevelopmentConfig)
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object(config.TestingConfig)
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'])


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object(config.ProductionConfig)
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
