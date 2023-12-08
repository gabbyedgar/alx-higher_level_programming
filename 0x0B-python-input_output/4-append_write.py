#!/usr/bin/python3
"""Module to append `text` to `filename`"""


def append_write(filename="", text=""):
    """Append `text` to `filename` if it exists, or create `filename`

    Args:
        filename (str): file to write to
        text (str): text to write in utf8 encoding

    Returns: number of characters written
    """
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
