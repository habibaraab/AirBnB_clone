#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import baseModel


class User(baseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
