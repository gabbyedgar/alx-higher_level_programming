#!/usr/bin/python3


class Square:
    """Class to represent a square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        return False

    def __ne__(self, other):
        if self.area() != other.area():
            return True
        return False

    def __gt__(self, other):
        if self.area() > other.area():
            return True
        return False

    def __ge__(self, other):
        if self.area() >= other.area():
            return True
        return False

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        return False

    def __le__(self, other):
        if self.area() <= other.area():
            return True
        return False
