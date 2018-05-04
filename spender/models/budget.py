# encoding: utf-8
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from database import Base
from sqlalchemy.orm import relationship, backref


class Budget(Base):
    """ This is the user's budget """

    __tablename__ = "budget"

    id = Column(Integer, autoincrement=True, primary_key=True)
    # the data type of the budget should match the data type of the price
    budget = Column(Numeric(15, 2))
    category_id = Column(Integer, ForeignKey('categories.id'))
    budget_userid = Column(Integer, ForeignKey('users.id'))
    budget_start_date = Column(DateTime)
    budget_end_date = Column(DateTime)

    user = relationship("User", backref=backref('budget'))

    category = relationship("Category", backref=backref('budget'))

    def __repr__(self):
        """ Provide useful info """

        return "<Budget id=%s budget=%s budget_userid=%s category=%s budget_start_date=%s budget_end_date=%s>" % (
            self.id, self.budget, self.budget_userid, self.category, self.budget_start_date, self.budget_end_date)
