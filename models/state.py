#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from models.base_model import Base
import models
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from Sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref"state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all City objects related"""
            list_city = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
