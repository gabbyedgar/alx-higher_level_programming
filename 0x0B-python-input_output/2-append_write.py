#!/usr/bin/python3

"""
module for append_write.
"""


def append_write(filename="", text=""):
    """string at the end of a text file"""
    with open(filename, 'a') as f:
        c = f.write(text)
    return c
