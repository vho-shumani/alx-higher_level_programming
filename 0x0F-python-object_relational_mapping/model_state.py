#!/usr/bin/python3
"""
module defines a State and base class
"""
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    define a state
    """
    __tablename__ = 'states'
    id = Column(Integer(), unique=True, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
