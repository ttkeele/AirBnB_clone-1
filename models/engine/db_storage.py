#!/usr/bin/python3
"""defines a class to manage database storage"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os


user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')


class DBStorage:
    """Class for database storage"""
    __classes = [State, City, User, Place, Amenity, Review]
    __engine = None
    __session = None

    def __init__(self):
        """initializes the storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
    if env == "test":
        Base.MetaData.drop_all()

    def all(self, cls=None):
        """Returns a dictionary of all objects in DB"""
        my_dict = {}
        if cls in self.__classes:
            result = DBStorage.__session.query(cls)
            for row in result:
            key = "{}.{}".format(row.__class__.__name__, row.id)
            my_dict[key] = row
        else:
            for cls in self.__classes:
                result = DBStorage.__session.query(cls)
                for row in result:
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    my_dict[key] = row
        return my_dict


    def new(self, obj):
        """adds an object to the session"""
        DBStorage.__session.add(obj)    


    def save(self):
        """commits the changes in  the current session"""
        DBStorage.__session.commit()


    def delete(self, obj=None):
        """deletes an object from the session"""
        DBStorage.__session.delete(obj)


    def reload(self):
        """reloads from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        DBStorage.__session = scoped_session(session_factory)
        DBStorage.__session = session()

    def close(self):
        """public method to call remove method"""
        DBStorage.__session.close()
