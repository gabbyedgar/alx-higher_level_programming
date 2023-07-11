#!/usr/bin/python3

"""
module for read_file.
"""


def read_file(filename=""):
    """Read a text file"""
    with open(filename, 'r') as f:
        read_data = f.read()
    print(read_data, end="")
