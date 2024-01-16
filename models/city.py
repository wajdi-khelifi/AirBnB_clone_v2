#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv
import models
import sqlalchemy


class City(BaseModel):
    """ The city class, contains state ID and name """
    if model.storage_t == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = relationship("Place", backref='cities', cascade"delete")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes city"""
        super().__init__(*args, **kwargs)
