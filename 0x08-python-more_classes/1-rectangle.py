#!/usr/bin/python3
""" Empty class that defines rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Initialize a new rectangle:
        args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of the square"""
        return (self.__width)

    @property
    def height(self):
        """height of the square"""
        return (self.__height)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value