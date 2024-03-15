#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
    
db_url = f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"
engine = create_engine(db_url)
Base = declarative_base()
Base.metadata.create_all(engine)

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer(), primary_key = True, autoincrement = True)
    name = Column(String(128), nullable=False)
