#!/usr/bin/python3
"""List City objects"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
    session.commit()
    session.close()
