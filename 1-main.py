#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print("--")
    something = FileStorage()
    something.new(my_model)
    something.reload()
