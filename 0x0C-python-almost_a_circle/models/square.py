#!/usr/bin/python3
"""Module containing Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class to represent a square deriving from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new square with width and height equal to `size`.

        Args:
            size (int): side lengths of square
            x (int): width offset for drawing square
            y (int): height offset for drawing square
            id: identifier for instance. If None, then object count.

        Raises:
            TypeError: If args are not int (or None for id)
            ValueError: If size is <= 0 or x, y and < 0 or id < 0
        """
        super().__init__(size, size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """Getter/setter for size propetry.
        Uses width attribute from Rectangle parent to store `size`.

        Raises:
            TypeError: If `size` is not an int.
            ValueError: If `size` is <= 0.

        Returns: value associated with `size`.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for `size`."""
        setattr(self, "width", value)

    def __str__(self):
        """Returns string representation of Square instance.

        Example:
            >>> s = Square(3, 4, 8, 9) # --> (size, x, y, id)
            >>> print(s)
            [Square] (9) 4/8 - 3
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__,
            self.id,
            self.x, self.y,
            self.size
        )

    def update(self, *args, **kwargs):
        """Update Square instances with *args and **kwargs.
        Order of *args is 'id', 'size', 'x', 'y'. **kwargs can be in
        any order.

        Example:
            >>> s = Square(1)
            >>> args = [6]; kwargs = {"size": 4, "y": 3}
            >>> s.update(*args, **kwargs)
            >>> print(s)
            [Square] (6) 0/3 - 4
        """
        attrs = ["id", "size", "x", "y"]
        for attr, arg in zip(attrs, args):
            setattr(self, attr, arg)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """Return dictionary representation of writable attributes.

        Example:
            >>> s = Square(1, 2, 3, 4)
            >>> s.to_dictionary()
            {"id": 4, "size": 1, "x": 2, "y": 3}
        """
        attrs = ["id", "size", "x", "y"]
        return {k: getattr(self, k) for k in attrs}
