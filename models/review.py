#!/usr/bin/python3
"""Defines the review class"""
import models
BaseModel = models.base_model.BaseModel


class Review(BaseModel):
    """Represents a a review

    Attributes:
        place_id (str): The Place.id
        usr_id (str): The User.id
        text (str): The text of the review
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of User class Object

        Args:
            args: positional arguments
            kwargs: keyword argument
        """
        super().__init__(*args, **kwargs)
