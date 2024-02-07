#!/usr/bin/python3
"""Square class defination"""


class Square:
    """A class to define a square.
    Attributes:
        __size (int): Private instance attribute to store size
    """
    def __init__(self, size):
        """Initializes a Square instance with a given size.
        Parameters:
             size (int): of the square.
        """
        self.__size = size
