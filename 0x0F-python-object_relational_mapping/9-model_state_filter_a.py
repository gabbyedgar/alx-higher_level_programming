#!/usr/bin/python3
"""Script to list all `State` objects that contain the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

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

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://'
                           '{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%')).\
            order_by(State.id):
        print("{}: {}".format(state.id, state.name))
