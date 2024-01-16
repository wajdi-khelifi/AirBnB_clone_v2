#!/usr/bin/python3
from models import storage_type
from models.base_model import BaseModel
from model.base_model import Base
from model.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state"""
    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)

    if storage_type != "db":
        @property
        def cities(self):
            """List of city instance related th the state"""
            from models import storage
            list_city = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
