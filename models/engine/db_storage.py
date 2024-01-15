#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
from models.base_model import Base


class DBStorage:
    """Represents a database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """A new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """The current database session"""
        if cls is None:
            rows = self.__session.query(State).all()
            rows.extend(self.__session.query(City).all())
            rows.extend(self.__session.query(User).all())
            rows.extend(self.__session.query(Place).all())
            rows.extend(self.__session.query(Review).all())
            rows.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            rows = self.__session.query(cls)
        return {"{}.{}".format(type(c).__name__, c.id): c for c in rows}

    def new(self, obj):
        """Add obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session"""
        self.__session.close()
