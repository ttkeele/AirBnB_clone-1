#!/usr/bin/python3
""" Define new engine DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User

mapped_classes = (City, State, User, Place, Amenity, Review)


class DBStorage:
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the storage"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                user, pwd, host, db), pool_pre_ping=True)
    if getenv('HBNB_ENV') == "test":
        Base.MetaData.drop_all(self.__engine)

    def all(self, cls=None):
        """returns objects in the database"""
        object = {}
        if cls in mapped_classes:
            objs.update({"{}.{}".format(cls.__name__, item.id): item
                         for item in self.__session.query(cls)})
        elif cls is None:
            for c in mapped_classes:
                objs.update({"{}.{}".format(c.__name__, item.id): item
                             for item in self.__session.query(c)})
        return objs

    def new(self, obj):
        """adds an object to the session"""
        if type(obj) in mapped_classes:
            self.__session.add(obj)

    def save(self):
        """commits the changes in  the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from db if not None"""
        if obj in self.all(type(obj).values()):
            self.__session.delete(obj)

    def reload(self):
        """reloads from the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """closes the current session"""
        self.__session.remove()
