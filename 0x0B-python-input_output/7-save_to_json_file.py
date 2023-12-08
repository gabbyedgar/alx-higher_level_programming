#!/usr/bin/python3
"""Module containing function to save python object in json format"""
import json


def save_to_json_file(my_obj, filename):
    """Convert `my_obj` to json string and save to `filename`

    Args:
        my_obj: serializable object to convert to json
        filename (str): file to save json string to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
