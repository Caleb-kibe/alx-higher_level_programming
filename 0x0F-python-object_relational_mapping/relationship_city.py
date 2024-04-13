#!/usr/bin/python3
"""
This file contains a class definition of State and an instance
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    State city that inherits from Base
    Attribute:
            id: Id city
            name: Name of the city
            state_id: State Id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('States.id'), nullable=False)
