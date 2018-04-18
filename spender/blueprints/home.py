from flask import Blueprint


home = Blueprint('home', __name__)


def index():
    return 'Hello World'

home.add_url_rule('/home', view_func=index)
