#!/usr/bin/python3
"""
Review model
inherited from BaseModel
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review model

    Attributes:
        place_id: Place.id (place being reviewed)
        user_id: User.id ( Reviwer)
        text: The review text
    """
    place_id = ""
    user_id = ""
    text = ""
