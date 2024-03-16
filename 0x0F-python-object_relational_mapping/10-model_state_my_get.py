#!/usr/bin/python3
"""prints State object with name passed as argument
   from the database hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = f"""mysql://{sys.argv[1]}:
               {sys.argv[2]}@localhost:3306/{sys.argv[3]}"""
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter_by(name=sys.argv[4]).one_or_none()
    print(states.id)
