#!/usr/bin/python3
"""
city module
inherited from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """city model
    Attributes:
        state_id (str) -> State.id
        name (str) -> name of the city
    """
    name = ""
    state_id = ""
