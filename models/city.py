#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import baseModel


class City(baseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
