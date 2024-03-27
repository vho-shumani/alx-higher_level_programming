#!/usr/bin/python3
"""
Module defines a State and base class
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """
    define a state
    """
    __tablename__ = 'states'
    id = Column(Integer(), unique=True, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="states", cascade="all, delete")
