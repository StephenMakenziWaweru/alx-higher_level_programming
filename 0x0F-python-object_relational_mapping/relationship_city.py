#!/usr/bin/python3
"""City class module"""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
