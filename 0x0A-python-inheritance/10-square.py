#!/usr/bin/python3
"""Module to implement a Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class implementing a Square as a subclass of Rectangle"""
    def __init__(self, size):
        """Initialize new Square instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Compute area of Square instance"""
        return self.__size ** 2
