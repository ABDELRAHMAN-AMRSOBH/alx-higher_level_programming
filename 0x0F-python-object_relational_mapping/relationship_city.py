#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py, and save them as
relationship_city.py and relationship_state.py.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """
    inherits from Base (imported from model_state)
    links to the MySQL table cities
    class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a string of 128 characters
    and can’t be null
    class attribute state_id that represents a column of an integer, can’t be
    null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
