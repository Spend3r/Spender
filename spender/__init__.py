# encoding: utf-8

import inspect
import logging
import os
import pkgutil

from flask import Flask, Blueprint


log = logging.getLogger(__name__)


def create_app(config=None):
    app = Flask(__name__)
    _register_core_blueprints(app)
    print(app.url_map)
    return app


def _register_core_blueprints(app):
    u'''Register all blueprints defined in the `blueprints` folder
    '''
    def is_blueprint(mm):
        return isinstance(mm, Blueprint)

    path = os.path.join(os.path.dirname(__file__), 'blueprints')

    for loader, name, _ in pkgutil.iter_modules([path], 'blueprints.'):
        module = loader.find_module(name).load_module(name)
        for blueprint in inspect.getmembers(module, is_blueprint):
            app.register_blueprint(blueprint[1])
            log.debug(u'Registered core blueprint: {0!r}'.format(blueprint[0]))
