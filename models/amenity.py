#!/usr/bin/python3
"""Defines the Amenity class"""
from models.base_model import BaseModel


class amenity(BaseModel):
    """Represents a user's state

    Attributes:
        name(str): The name of the user's Amenity
    """

    name = ""
