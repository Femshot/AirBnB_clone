#!/usr/bin/python3
"""Defines the City class"""
import models
BaseModel = models.base_model.BaseModel


class city(BaseModel):
    """Represents a user's state

    Attributes:
        name(str): The name of the user's city
    """

    name = ""

