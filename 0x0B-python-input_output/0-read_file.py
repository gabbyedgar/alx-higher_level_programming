#!/usr/bin/python3
"""Module to read a file"""


def read_file(filename=""):
    """Read a file in utf8 encoding and print to stdout

    Args:
        filename (str): file to open
    """
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end="")
