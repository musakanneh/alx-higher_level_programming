#!/usr/bin/python3
"""script that lists all State objects that contain
 the letter a from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    q = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state in q:
        print("{}: {}".format(state.id, state.name))
    session.close()
