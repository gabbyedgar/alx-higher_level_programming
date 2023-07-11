#!/usr/bin/python3
"""Module to write text to a file"""


def write_file(filename="", text=""):
    """Write `text` to `filename`

    Args:
        filename (str): file to write to
        text (str): text to write into `filename`

    Returns: number of characters written
    """
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
