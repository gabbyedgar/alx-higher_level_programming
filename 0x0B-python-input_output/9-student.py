#!/usr/bin/python3

"""
module for class Student.
"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary"""
        return self.__dict__
