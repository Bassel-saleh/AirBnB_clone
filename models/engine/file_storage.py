#!/usr/bin/python3
"""serializes instances to a JSON(file)
    deserializes JSON(file) to instances
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def all(self):
        """ Returns the dictionary objects """
        return self.__class__.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        Args:
            obj(object) -> The object to add to __objects
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__class__.__objects[key] = obj

    def save(self):
        """ serializes objects to the JSON file """
        objects_dict = {}
        for key, value in self.__class__.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as storage:
            json.dump(objects_dict, storage)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    base = FileStorage.classes[value["__class__"]](**value)
                    FileStorage.__objects[key] = base
