#!/usr/bin/python3
"""List all State objects and their corresponding City objects hbtn_0e_101_usa.
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

    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State)\
                              .join(State, State.id == City.state_id)\
                              .order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))
