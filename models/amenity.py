#!/usr/bin/python3
"""Defines the Amenity class."""
import sqlalchemy
from os import getenv
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models import storage_type


class Amenity(BaseModel, Base):
    """Representation of Amenity"""
    __tablename__ = 'amenities'
    if model.storage_t == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **Kwargs)
