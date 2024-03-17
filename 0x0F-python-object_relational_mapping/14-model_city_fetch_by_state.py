#!/usr/bin/python3

"""
File: 14

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query_info = session.query(City, State).join(State)
    for city, state in query_info:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
