#!/usr/bin/python3

"""
module for save_to_json_file.
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
