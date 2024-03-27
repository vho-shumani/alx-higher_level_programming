#!/usr/bin/python3
"""
lists all City object from the database hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = f"""mysql://{sys.argv[1]}:
               {sys.argv[2]}@localhost:3306/{sys.argv[3]}"""
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        for city in session.query(City).filter(City.state_id == state.id).order_by(City.id):
            print(f'{state.name}: ({city.id}) {city.name}')
