#!/usr/bin/python3
"""state module
inherited from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class
    Attributes:
        name(str) -> Name of the state
    """
    name = ""
