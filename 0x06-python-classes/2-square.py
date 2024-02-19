#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """ Square class.
    Attributes:
        __size (int): Private instance attribute size of square.
    """
    def __init__(self, size=0):
        """
        Intialize a Square instance with optional size.

        Parameters:
            size (int, optional): of square. Defualt to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
