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

    pass
