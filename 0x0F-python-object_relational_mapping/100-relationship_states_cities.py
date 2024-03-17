#!/usr/bin/python3
"""
creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa:
"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = f"""mysql://{sys.argv[1]}:
               {sys.argv[2]}@localhost:3306/{sys.argv[3]}"""
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()
