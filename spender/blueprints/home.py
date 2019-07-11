# encoding: utf-8

import logging
from flask import Blueprint, render_template

log = logging.getLogger(__name__)
home = Blueprint('home', __name__, url_prefix='/')


def index():
    return render_template('home/index.html')


home.add_url_rule('/', '/home', view_func=index)
