# encoding: utf-8

import logging

from flask import Blueprint, flash, redirect, render_template

from spender import db
from spender.forms.user import UserAddForm
from spender.models.user import User

log = logging.getLogger(__name__)
user = Blueprint('user', __name__,  url_prefix='/user')


def add_user():
    form = UserAddForm()
    if form.validate_on_submit():
        user = User(form.name.data, form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/')

    return render_template('user/add_user.html', form=form)


user.add_url_rule('/add', methods=['GET', 'POST'], view_func=add_user)
