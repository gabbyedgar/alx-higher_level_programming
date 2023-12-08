#!/usr/bin/python3
"""Module implementing class with method to serialize itself"""


class Student:
    """Class to represent student"""
    def __init__(self, first_name, last_name, age):
        """Initialize new student instance with name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Create copy of attributes for use in json string

        If `attrs` is not None, use `attrs` list to select desired attributes.
        """
        if attrs is None or not isinstance(attrs, (list, tuple)):
            return self.__dict__.copy()
        else:
            ret = {k: v for k, v in filter(lambda x: x[0] in attrs,
                                           self.__dict__.items())}
            return ret

    def reload_from_json(self, json):
        """Use serialized version of `Student` instance to update `self`

        Recreate instance from previously serialized `Student` instance.
        """
        self.__dict__.update(json)
