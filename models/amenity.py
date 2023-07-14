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

    pass
