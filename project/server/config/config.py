import datetime
import os
from logging.config import fileConfig

basedir = os.path.abspath(os.path.dirname(__file__))
mysql_local_base = 'mysql://macula:macula@localhost/'
database_name = 'macula'


class BaseConfig:
    """Base configuration."""
    FIXTURES_DIRS = './project/server/fixtures/'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=0, minutes=60)
    JWT_SECRET_KEY = os.getenv('SECRET_KEY', '\xdf-vm"\xadv-\xa8\xff\xc7\xe1\xc3\x05E\xe3\x14\x8f;\x06\xbb\xbf\xae.')
    SECRET_KEY = os.getenv('SECRET_KEY', '\xdf-vm"\xadv-\xa8\xff\xc7\xe1\xc3\x05E\xe3\x14\x8f;\x06\xbb\xbf\xae.')
    SECURITY_PASSWORD_SALT = os.getenv('SECRET_KEY', '\xdf-vm"\xadv-\xa8\xff\xc7\xe1\xc3\x05E\xe3\x14\x8f;\x06\xbb\xbf\xae.')
    JWT_IDENTITY_CLAIM = 'sub'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # gmail authentication
    MAIL_USERNAME = os.getenv('APP_MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('APP_MAIL_PASSWORD')

    # LOGGER
    # fileConfig(basedir + '/logging.conf')


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = mysql_local_base + database_name
    MAIL_DEFAULT_SENDER = 'test@localhost.com'

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # mail accounts
    MAIL_DEFAULT_SENDER = 'test@localhost.com'

    # UI Route
    UI_URL = 'http://localhost:4200'


class TestingConfig(BaseConfig):
    """Testing configuration."""
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=0, seconds=5)
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = mysql_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql:///example'
