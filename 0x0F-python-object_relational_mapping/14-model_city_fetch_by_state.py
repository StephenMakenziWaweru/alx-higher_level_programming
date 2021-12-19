#!/usr/bin/python3
"""Fetch city state"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    cities = session.query(City, State).filter(City.state_id == State.id).\
        all()
    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.commit()
    session.close()
