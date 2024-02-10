#!/usr/bin/python3
"""
Amenity model
inherited from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity model
    Attributes:
        name: Name of the amenity
    """
    name = ""
