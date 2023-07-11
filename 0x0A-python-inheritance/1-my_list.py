#!/usr/bin/python3
"""Module that implements MyList class"""


class MyList(list):
    """MyList class extends lists to include print_sorted method"""
    def print_sorted(self):
        """Prints list elements in sorted order"""
        print(sorted(self))
