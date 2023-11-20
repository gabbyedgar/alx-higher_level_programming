#!/usr/bin/python3
"""Add `Louisiana` State object to database `hbtn_0e_6_usa`."""

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
    la = State(name='Louisiana')
    session.add(la)
    la = session.query(State.id).filter(State.name == 'Louisiana').one()
    print(la.id)
    session.commit()
