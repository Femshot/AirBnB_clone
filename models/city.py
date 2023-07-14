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

    pass
