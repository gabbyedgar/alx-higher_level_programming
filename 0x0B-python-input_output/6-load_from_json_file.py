#!/usr/bin/python3
"""Module implementing function to retrieve objects from json file"""
import json


def load_from_json_file(filename):
    """Load json string representing python object from file `filename`

    Args:
        filename (str): name of file containing json string

    Returns: object saved by json file
    """
    with open(filename, 'r') as f:
        return json.load(f)
