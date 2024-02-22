#!/usr/bin/python3
""" Class Square"""


class Square:
    """
    Square class.
        Attributes:
            __size (int): Priviate instance attribute sixe of square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Intialize a Square instance with optional size.
        Parameters:
            size (int, optional): of square. Defualto 0.
        Raises:
            TypeError if: size is not an integer.
            ValueError: if size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value: to set it.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area square"""
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout of square with character #"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
