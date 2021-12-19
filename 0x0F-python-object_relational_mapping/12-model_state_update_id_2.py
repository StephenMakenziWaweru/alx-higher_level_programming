#!/usr/bin/python3
"""Fetch state from database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    state = session.query(State).filter(State.id == 2).all()
    if state:
        state[0].name = 'Nex Mexico'
    session.commit()
    session.close()
