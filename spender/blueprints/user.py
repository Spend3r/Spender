# encoding: utf-8

import logging
from flask import Blueprint, render_template, flash, redirect
from spender.models.user import User
from spender.forms.user import UserAddForm

log = logging.getLogger(__name__)
user = Blueprint('user', __name__,  url_prefix='/user')


def add_user():
    form = UserAddForm()
    if form.validate_on_submit():
        flash('Name is requested for the user {}'.format(form.name))
        user = User(form.name, form.email)
        return redirect('/')
    return render_template('user/add_user.html', form=form)


user.add_url_rule('/add', methods=['GET', 'POST'], view_func=add_user)
