#!/usr/bin/python3
"""Module implementing function to determine subclass membership"""


def inherits_from(obj, a_class):
    """Returns True if obj inherits from a_class. False otherwise."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
