#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False, default="")

    def __init__(self, *args, **kwargs):
        '''
            Initializes values of our attributes to correct types
        '''
        self.name = ""
        super().__init__(kwargs)

#    place_amenities = relationship(
#            "Place", secondary="place_amenity", back_populates="amenities")
