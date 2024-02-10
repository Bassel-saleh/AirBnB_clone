#!/usr/bin/python3
""" 
user module:
    username
    passwords
"""
from models.base_model import BaseModel

class User(BaseModel):
    """ user module
    Attributes:
        email (str) -> User's email
        password (str) -> User's password
        first_name (str) -> User's first Name
        last_name (str) -> User's last Name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
