#!/usr/bin/python3
"""Module to convert objects to json"""
import json


def to_json_string(my_obj):
    """Convert serializable `obj` to json string

    Args:
        obj: serializable object

    Returns: string representation of `obj`
    """
    return json.dumps(my_obj)
