#!/usr/bin/python3
""" Class that defines rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
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

    def area(self):
        """area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """perimeter of the rectangle.
        returns 0 if either width or height is zero"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """returns a printable representation
         of a rectangle with '#' character"""
        if self.width == 0 or self.height == 0:
            return ""

        rect = []
        for i in range(self.height):
            [rect.append('#') for j in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
