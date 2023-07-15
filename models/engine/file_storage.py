#!/usr/bin/python3
"""Defines a class FileStorage """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Defines a class Filestorage to store object instance

    Attributes:
        file_path: String path to JSON file
        objects: Dictionary to store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        Args:
            cl_name: Class name of obj object
            cl_id: id of obj object
            ky: 'class name.class id'
        """
        cl_name = obj.__class__.__name__
        cl_id = obj.id
        ky = cl_name + "." + cl_id
        FileStorage.__objects[ky] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as fl:
            new_dict = {}
            for obj_id in FileStorage.__objects:
                inst = FileStorage.__objects[obj_id]
                new_dict[obj_id] = inst.to_dict()
            json.dump(new_dict, fl)

    def reload(self):
        """Deserializes the JSON file to __objects

        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r') as fl:
                obj_dict = json.load(fl)
                for key, value in obj_dict.items():
                    if key.startswith("BaseModel"):
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif key.startswith("User"):
                        FileStorage.__objects[key] = User(**value)
                    elif key.startswith("State"):
                        FileStorage.__objects[key] = State(**value)
                    elif key.startswith("City"):
                        FileStorage.__objects[key] = City(**value)
                    elif key.startswith("Amenity"):
                        FileStorage.__objects[key] = Amenity(**value)
                    elif key.startswith("Place"):
                        FileStorage.__objects[key] = Place(**value)
                    elif key.startswith("Review"):
                        FileStorage.__objects[key] = Review(**value)
        except Exception:
            pass
