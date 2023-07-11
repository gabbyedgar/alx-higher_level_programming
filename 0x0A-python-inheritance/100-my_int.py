#!/usr/bin/python3
"""Module implementing MyInt"""


class MyInt(int):
    """Class to represent rebel integer that swaps `==` and `!=`"""
    def __eq__(self, other):
        """Swaps meaning of `==` with `!=`

        Args:
            other: object to compare with `self`

        Returns: True if `self` and `other` *are not* equal,
            False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Swaps meaning of `==` with `!=`

        Args:
            other: object to compare with `self`

        Returns: False if `self` and `other` *are not* equal,
            True otherwise.
        """
        return super().__eq__(other)
