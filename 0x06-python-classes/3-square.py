#!/usr/bin/python3
"""Task"""


class Square:
    """This is a class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square"""
        return self.__size ** 2
