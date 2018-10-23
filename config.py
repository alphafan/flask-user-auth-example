import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # APP MODE
    DEBUG = True

    # Top secret of website
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Bootstrap using local static files
    BOOTSTRAP_SERVE_LOCAL = True

    # Mail Configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'you-will-never-guess@gmail.com'
    MAIL_PASSWORD = 'you-will-never-guess'

    # ADMINS
    ADMINS = ['you-will-never-guess@gmail.com']


class TestConfig(Config):

    # Test Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
