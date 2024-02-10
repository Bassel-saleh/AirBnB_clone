#!/usr/bin/python3
"""
Place model
inherited from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place model
    Attributes:
        city_id: City.id
        user_id: City.id
        name: name of place
        description: description of place
        number_rooms: Number of rooms: default is 0
        number_bathrooms: Number of bathrooms: default is 0
        max_guest: Maximum number of guests: default is 0
        price_by_night: charing rate by night: default is 0
        latitude: Geographical lattitude
        longitude: Geographical longitude
        amenity_ids: list of strings of ameninty ID's
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
