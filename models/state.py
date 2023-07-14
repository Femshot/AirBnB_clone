#!/usr/bin/python3
"""Defines the state class"""
import models
BaseModel = models.base_model.BaseModel


class state(BaseModel):
    """Represents a user's state

    Attributes:
        name(str): The name of the user's state
    """

    name = ""
