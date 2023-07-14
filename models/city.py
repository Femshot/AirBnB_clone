#!/usr/bin/python3
"""Defines the City class"""
import models
BaseModel = models.base_model.BaseModel


class City(BaseModel):
    """Represents a user's state

    Attributes:
        state_id(str): The State.id
        name(str): The name of the city
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of City class Object

        Args:
            args: positional arguments
            kwargs: keyword argument
        """
        super().__init__(*args, **kwargs)
