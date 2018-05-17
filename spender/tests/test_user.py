# encoding: utf-8

import pytest_flask


def test_create_user(session):
    '''Test create user '''
    name = 'Jon Snow'
    email = 'j.snow@wall.com'

    user = user.User(name, email)
    session.add(user)
    session.commit()

    assert user.id is not None
