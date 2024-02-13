#!/usr/bin/python3
"""
Define class Rectangle
"""


class Rectangle:
    """
    Represents a rectangle with width and height attributes.

    Attributes:
        width (int): of rectangle.
        height (int): of rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with given width and height.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width attribute.

        Returns:
            int: width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.

        Args:
            value (int): The value to set as the width of the rectangle.

        Raises:
            TypeError: If the value provided is not an integer.
            ValueError: If the value provided is less than 0.

        Returns:
            int: The width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width:must be >=0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.

        Returns:
            int: Height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.

        Args:
            value (int): The value to set as the height of the rectangle.

        Raises:
            TypeError: If the value provided is not an integer.
            ValueError: If the value provided is less than 0.

        Returns:
            int: The height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
