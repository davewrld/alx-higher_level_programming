#!/usr/python3

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object with given width and height.
        Args:
            width (int): The width of the rectangle.
            height: The height of the rectangle.

            x = width
            y = height
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


@property
def width(self):
    """
    Getter method for width atrribute

    Returns:
        int: width of rectangle
    """
    return self.__width


@width.setter
def width(self, width):
    """
    setter for width 5
    """
    self.width = width


@property
def height(self):
    """
    Getter method for heighth
    """
    return self.__height


@height.setter
def height(self, height):
    """
    setter for height
    """
    self.__height = height


@property
def x(self):
    """
    getter for x
    """
    return self.__x


@x.setter
def x(self, x):
    """
    setter for x
    """
    self.__x = x


@property
def y(self):
    """
    getter for y
    """
    return self.__y


@y.setter
def y(self, height):
    """
    setter for y
    """
    self.__y = y
