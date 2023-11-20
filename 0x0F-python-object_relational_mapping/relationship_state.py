#!/usr/bin/python3
"""Create table `states` using SQLAlchemy"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the `states` table.

    Columns:
        id (int): /NOT NULL/AUTO_INCREMENT/PRIMARY_KEY/
        name (string): /VARCHAR(128)/NOT NULL/
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="cities")
