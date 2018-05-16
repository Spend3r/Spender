# encoding: utf-8
from app import db


class Budget(db.Model):
    """ This is the user's budget """

    __tablename__ = "budget"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # the data type of the budget should match the data type of the price
    budget = db.Column(db.Numeric(15, 2))
    budget_userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", backref=backref('budget'))

    def __repr__(self):
        """ Object Representation"""

        return "<Budget id=%s budget=%s budget_userid=%s\
                category=%s budget_start_date=%s budget_end_date=%s>" % (
                self.id, self.budget, self.budget_userid)
