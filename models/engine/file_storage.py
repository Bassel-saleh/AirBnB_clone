#!/usr/bin/python3
"""serializes instances to a JSON(file)
    deserializes JSON(file) to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Represent an abstracted storage engine

    Attributes:
        __file_path (str): The name of the file to save objects to
        __objects (dict): A dictionary of instantiated objects
    """
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
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        Args:
            obj(object) -> The object to add to __objects
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """ serializes objects to the JSON file """
        objects_dict = {}
        for key, value in self.__class__.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as storage:
            json.dump(objects_dict, storage)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = self.classes[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            return
