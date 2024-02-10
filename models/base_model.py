#!/usr/bin/python3
'''this module is base class for other classes to inherit from'''
import uuid
from datetime import datetime
import models


class BaseModel():
    '''this is base class which all other subclasses inherit from

    Attributes:
        id: basemodel id
        created_at: the datetime of creation
        updated_at: the datetime of updating

    Methods:
        __ini__(self, *args, **kwargs)
        __str__(self)
        to_dict(self)
        __repr__(self)
    '''

    def __init__(self, *args, **kwargs):
        '''initiates class instances'''

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''return representation of an object'''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def __repr__(self):
        ''' returns string representation '''
        return (self.__str__())

    def save(self):
        '''save the current state of an object'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''convert an instance into dictionary representation'''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
