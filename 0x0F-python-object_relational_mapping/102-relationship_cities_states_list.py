#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
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
    states = session.query(State).order_by(State.id)
    for state in states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> ", end='')
            print(f"{state.name}")
