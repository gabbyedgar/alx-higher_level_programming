#!/usr/bin/python3
"""Module to serialize class to json"""


def class_to_json(obj):
    """Make serializable copy of `obj` attributes for json

    Args:
        obj: object to serialize

    Returns: copy of `obj`s attributes as dictionary
    """
    return obj.__dict__.copy()
