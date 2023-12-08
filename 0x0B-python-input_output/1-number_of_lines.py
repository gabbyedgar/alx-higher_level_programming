#!/usr/bin/python3
"""Module to get number of lines in a file"""


def number_of_lines(filename=""):
    """Count number of lines in `filename` if it exits

    Args:
        filename (str): path of file from which to count lines
    """
    nb_lines = 0
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            nb_lines += 1
    return nb_lines
