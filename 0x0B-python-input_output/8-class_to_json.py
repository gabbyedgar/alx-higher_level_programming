#!/usr/bin/python3
"""
Python class-to-JSON
"""


def class_to_json(obj):
    """Return the dictionary"""
    return obj.__dict__
