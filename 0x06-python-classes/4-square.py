#!/usr/bin/python3
""" Class Square"""


class Square:
    """
    Square class.
        Attributes:
            __size (int): Priviate instance attribute sixe of square.
    """
    def __init__(self, size=0):
        """
        Intialize a Square instance with optional size.
        Parameters:
            size (int, optional): of square. Defualto 0.
        Raises:
            TypeError if: size is not an integer.
            ValueError: if size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value: New size to set.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current area square"""
        return self.__size ** 2
