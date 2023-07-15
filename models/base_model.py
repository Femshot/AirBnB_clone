#!/usr/bin/python3
"""
Define the BaseModel class
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    defines the BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """ Iniitalise a new BaseModel class instance

            Attributes:
                id: a unique id for each BaseModel
                created_at: datetime at creation of class instance
                updated_at: datetime at last update of class update of instance

            Args:
                *args (any): Unused
                **kwargs (dict): Key or value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Defines str output of BaseModel object

            Returns: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ update updated_at with the current datetime"""
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary Representation of the BaseModel"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
