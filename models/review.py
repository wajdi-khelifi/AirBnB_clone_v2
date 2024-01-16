#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy
from os import getenv


class Review(BaseModel):
    """ Review classto store review information """
    if models.storage_t == "db":
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('place.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Initializes review"""
        super().__init__(*args, **kwargs)
