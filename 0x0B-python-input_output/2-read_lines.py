#!/usr/bin/python3
"""Module to read lines from file"""


def read_lines(filename="", nb_lines=0):
    """Read `nb_lines` lines from `filename`
    If `nb_lines` <= 0 read all lines. Otherwise, read up to `nb_lines`
        or EOF, whichever comes first.

    Args:
        filename (str): name of file to read
        nb_lines (int): maximum number of lines to read, or if <= 0, all lines
    """
    with open(filename, 'r', encoding='utf8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line in f:
                if nb_lines == 0:
                    break
                print(line, end="")
                nb_lines -= 1
