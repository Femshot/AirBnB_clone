#!/usr/bin/python3
"""Defines the Place class"""
import models
BaseModel = models.base_model.BaseModel


class Place(BaseModel):
    """Represents a Place

    Attributes:
        city_id (str): The City.id
        user_id (str): The User.id
        name (str): The name of the Place
        description (str): The description of the Palce
        number_rooms (int): The number of rooms of the Place
        number_bathrooms (int): The number of bathrooms in the Place
        max_guest (int): The maximum number of guests the Place can take
        price_by_nigth (int): The price by night of the Place
        latitude (float): The latitude of the Place
        longitude (float): The longitude of the Place
        amenity_id (list(str's)): A list of Amenities.id's
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Instantiation of Place class Object

        Args:
            args: positional arguments
            kwargs: keyword argument
        """
        super().__init__(*args, **kwargs)
