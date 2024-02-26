#!/usr/bin/python3
"""Base Class"""


class Base:
    """
    This class will be the base of all other classes.
    Goal is to manage
        Attribute: id - To avoid duplication of same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
