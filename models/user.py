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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
