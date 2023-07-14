#!/usr/bin/python3
"""Defines the review class"""
import models
BaseModel = models.base_model.BaseModel


class review(BaseModel):
    """Represents a a review

    Attributes:
        place_id (str): The place id
        usr_id (str): The user id
        text (str): The text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
