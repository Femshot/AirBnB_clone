#!/usr/bin/python3
"""Defines the Amenity class"""
import models
BaseModel = models.base_model.BaseModel


class amenity(BaseModel):
    """Represents a user's state

    Attributes:
        name(str): The name of the user's Amenity
    """

    name = ""
