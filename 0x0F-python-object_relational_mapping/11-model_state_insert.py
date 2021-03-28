#!/usr/bin/python3
"""
script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    st = State(name='Louisiana')
    session.add(st)
    our_user = session.query(State).filter_by(name='Louisiana').first()
    session.commit()
    print(our_user.id)
    session.close()
