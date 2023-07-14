#!/usr/bin/python3
"""Defines the Amenity class"""
import models
BaseModel = models.base_model.BaseModel


class Amenity(BaseModel):
    """Represents an Amenity

    Attributes:
        name(str): The name of the Amenity
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of Amenity class Object

        Args:
            args: positional arguments
            kwargs: keyword argument
        """
        super().__init__(*args, **kwargs)
