#!/usr/bin/python3
"""
This script lists all city objects from the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3], pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State).filter_by(id=city.state_id)\
                .first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()
