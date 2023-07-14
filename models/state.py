#!/usr/bin/python3
"""Defines the State class"""
import models
BaseModel = models.base_model.BaseModel


class State(BaseModel):
    """Represents a State

    Attributes:
        name(str): The name of the user's state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of State class Object

        Args:
            args: positional arguments
            kwargs: Keyword arguments
        """
        super().__init__(*args, **kwargs)
