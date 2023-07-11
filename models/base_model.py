#!/usr/bin/python3
"""
Define the BaseModel class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    defines the BaseModel class.
    """

    def __init__(self):
        """ Iniitalise a new BaseModel class instance

            Attributes:
                id: a unique id for each BaseModel
                created_at: datetime at creation of class instance
                updated_at: datetime at last update of class update of instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Defines str output of BaseModel object

            Returns: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ update updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary Representation of the BaseModel"""
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict



if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
