#!/usr/bin/python3
"""Module to convert json string to python object"""
import json


def from_json_string(my_str):
    """Convert `my_str` json string into python object

    Args:
        my_str (str): json string representatino of object

    Returns: object represented by `my_str`
    """
    return json.loads(my_str)
