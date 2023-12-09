#!/usr/bin/python3
"""This module creates a Review class"""

from models.base_model import baseModel


class Review(baseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
