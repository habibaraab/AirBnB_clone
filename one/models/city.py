#!/usr/bin/python3
"""This module creates a User class"""

from models.Base_Model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
