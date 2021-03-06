# encoding: utf-8

import inspect
import logging
import os
import pkgutil

from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from config import config

log = logging.getLogger(__name__)

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=config.get('development')):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    # migrate.init_app(app, db)
    _register_core_blueprints(app)

    init_db(app, db)

    return app


def url_for_static(filename):
    root = app.config.get('STATIC_ROOT', '')
    return join(root, filename)


def _register_core_blueprints(app):
    '''Register all blueprints defined in the `blueprints` folder
    '''
    def is_blueprint(mm):
        return isinstance(mm, Blueprint)

    path = os.path.join(os.path.dirname(__file__), 'blueprints')

    for loader, name, _ in pkgutil.iter_modules([path], 'blueprints.'):
        module = loader.find_module(name).load_module(name)
        for blueprint in inspect.getmembers(module, is_blueprint):
            app.register_blueprint(blueprint[1])
            log.info('Registered blueprint: {0!r}'.format(blueprint[0]))


def init_db(app, db):
    from spender.models import user
    from spender.models import budget
    with app.app_context():
        db.create_all()
        db.session.commit()
