#!/usr/bin/python3
""" class with size validation """


class Square:
    """ square class initialization"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    @property
    def size(self):
        '''Properties for the length of a sise of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Area of the square.
        Returns: the size squared.
        '''
        return self.__size * self.__size
