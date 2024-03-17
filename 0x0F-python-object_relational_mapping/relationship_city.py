#!/usr/bin/python3
"""
Module defines a State and base class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    define cities
    """
    __tablename__ = 'cities'
    id = Column(Integer(), unique=True, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), unique=True, nullable=False)
