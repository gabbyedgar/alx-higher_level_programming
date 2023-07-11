#!/usr/bin/python3
"""Module to implement Rectangle class, extending BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class to represent a rectangle"""
    def __init__(self, width, height):
        """Initialize a new rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
