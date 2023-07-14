#!/usr/bin/python3
"""Defines the User class"""
import models
BaseModel = models.base_model.BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email(str): The email of the user.
        password(str): The password of the user
        firt_name(str): The firt name of the user
        last_name(str): The last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of User class Object

        Args:
            args: positional arguments
            kwargs: keyword argument
        """
        super().__init__(*args, **kwargs)
