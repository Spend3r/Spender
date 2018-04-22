# encoding: utf-8

import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    EXPLAIN_TEMPLATE_LOADING = True


class DevelopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'spender.db')
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True


config = {
    "development": DevelopmentConfig,
    "default": Config
}
