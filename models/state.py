#!/usr/bin/python3
"""Defines the state class"""
from models.base_model import BaseModel


class state(BaseModel):
    """Represents a user's state

    Attributes:
        name(str): The name of the user's state
    """

    name = ""
