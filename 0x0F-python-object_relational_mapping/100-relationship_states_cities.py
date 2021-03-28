#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py, and save
them as relationship_city.py and relationship_state.py
"""
import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    s1 = State(name='California')
    c1 = City(name='San Francisco')
    s1.cities.append(c1)
    session.add_all([c1, s1])
    session.commit()
    session.close()
