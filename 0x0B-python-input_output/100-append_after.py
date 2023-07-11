#!/usr/bin/python3
"""Module containing function that modifies file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts `new_string` into `filename` after lines containing
         `search_string`.

    Args:
        filename (str): file to modify
        search_string (str): string to look for in `filename`
        new_string (str): string to insert after `search_string`
    """
    with open(filename, 'r+') as f:
        lines = [line for line in f]
        f.seek(0)
        for idx, line in enumerate(lines):
            if search_string in line:
                lines.insert(idx + 1, new_string)
        f.writelines(lines)
