#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
import os
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


Table('place_amenity',
      Base.metadata,
      Column(
          'place_id', String(60), ForeignKey('places.id'),
          primary_key=True, nullable=False),
      Column(
          'amenity_id', String(60), ForeignKey('amenities.id'),
          primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', backref='place')
    amenities = relationship(
        "Amenity", secondary=place_amenity, viewonly=False,
        backref='places')

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship('Review',
                               cascade="all, delete, delete-orphan",
                               backref='place')
        amenities = relationship('Amenity',
                                 secondary="place_amenity",
                                 viewonly=False,
                                 backref="place_amenities"
                                 )
    else:
        @property
        def reviews(self):
            """getter for reviews"""
            from models import storage
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """getter for amenities"""
            from models import storage
            return [amenity for amenity in storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """adds an ammenity to object"""
            from models import storage
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
