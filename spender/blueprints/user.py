# encoding: utf-8

import logging
from flask import Blueprint, render_template

log = logging.getLogger(__name__)
user = Blueprint('user', __name__,  url_prefix='/user')


@user.before_request
def before_request():
    print("hello")
