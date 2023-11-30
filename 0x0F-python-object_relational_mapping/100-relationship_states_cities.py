#!/usr/bin/python3
"""Script to create State `California` with City `San Francisco` within
database hbtn_0e_100_usa.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import State, Base

    engine = create_engine('mysql+mysqldb://'
                           '{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    ca = State(name='California')
    sf = City(name='San Francisco')
    ca.cities = [sf]
    session.add(ca)
    session.commit()
