#!/usr/bin/python3
"""Script to rpint all City objects from database `hbtn_0e_14_usa`."""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import State

    engine = create_engine('mysql+mysqldb://'
                           '{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state_name in session.query(City, State.name)\
                                   .join(State, State.id == City.state_id):
        print("{}: ({}) {}".format(state_name, city.id, city.name))
