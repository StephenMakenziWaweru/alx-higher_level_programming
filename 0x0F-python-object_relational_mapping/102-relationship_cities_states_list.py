#!/usr/bin/python3
"""
lists all City objects from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                       argv[2],
                                                                       argv[3]
                                                                       ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    rows = session.query(State).order_by(State.id).all()
    for row in rows:
        for city in row.cities:
            print('{}: {} -> {}'.format(city.id, city.name, row.name))

    session.close()
