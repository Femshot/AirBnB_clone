#!/usr/bin/python3
"""Defines the place class"""
import models
BaseModel = models.base_model.BaseModel


class place(BaseModel):
    """Represents a user's state

    Attributes:
        city_id (str): The city id
        user_id (str): The user id
        name (str): The name of the place
        description (str): The description of the palce
        number_rooms (int): The number of rooms of the place
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The maximum number of guests the place can take
        price_by_nigth (int): The price by night of the place
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_id (list): A list of Amenities
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_nigth = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []
