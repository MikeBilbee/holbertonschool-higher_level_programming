#!/usr/bin/python3
""" Deletes all State objects with a name containing the letter a """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    item = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()

    for city, state in item:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
