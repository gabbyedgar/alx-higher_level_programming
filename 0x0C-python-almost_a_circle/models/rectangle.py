#!/usr/bin/python3
"""Module containing Square class"""
from models.base import Base


class Rectangle(Base):
    """Class to represent a rectangle deriving from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new square with width, height, and offsets.

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): width offset for drawing rectangle
            y (int): height offset for drawing rectangle
            id: identifier for instance. If None, then object count

        Raise:
            TypeError: If `width`, `height`, `x`, or `y` are not ints.
            ValueError: If `width` or `height` are <= 0, or `x` or `y`
                are < 0.
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter/setter for width property.

        Raises:
            TypeError: If `width` is not an int.
            ValueError: If `width` is <= 0.

        Returns: value associated with `width`
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for `width`."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter for height property.

        Raises:
            TypeError: If `height` is not an int.
            ValueError: If `height` is <= 0.

        Returns: value associated with `height`
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for `height`."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter/setter for x (offset) property.

        Raises:
            TypeError: If `x` is not an int.
            ValueError: If `x` is < 0.

        Returns: value associated with `x`
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for `x` (offset)."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter/setter for y (offset) property.

        Raises:
            TypeError: If `y` is not an int.
            ValueError: If `y` is < 0.

        Returns: value associated with `y`
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for `y` (offset)."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method to compute the area of a rectangle.

        Returns: width * height
        """
        return self.__width * self.__height

    def display(self):
        """Method to print a representation of a Rectangle to stdout.

        Example:
            >>> r1 = Rectangle(2, 2)
            >>> r1.display()
            ##
            ##

            >>> r2 = Rectangle(3, 2, 1, 1)
            >>> r2.display()
            <BLANKLINE>
             ###
             ###

        """
        print('\n' * self.__y +
              '\n'.join([' ' * self.__x +
                         '#' * self.__width
                         for i in range(self.__height)]))

    def __str__(self):
        """Returns string representation of Rectangle instance.

        Example:
            >>> r = Rectangle(2, 3, 4, 8, 9) # --> (width, height, x, y, id)
            >>> print(r)
            [Rectangle] (9) 4/8 - 2/3
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__,
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    def update(self, *args, **kwargs):
        """Update Rectangle instances with *args and **kwargs.
        Order of *args is 'id', 'size', 'x', 'y'. **kwargs can be in
        any order.

        Example:
            >>> r = Rectangle(2, 2)
            >>> args = [6]; kwargs = {"height": 4, "y": 3}
            >>> r.update(*args, **kwargs)
            >>> print(r)
            [Rectangle] (6) 0/3 - 6/4
        """
        attrs = ["id", "width", "height", "x", "y"]
        for attr, arg in zip(attrs, args):
            setattr(self, attr, arg)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """Return dictionary representation of writable attributes.

        Example:
            >>> r = Rectangle(1, 1, 2, 3, 4)
            >>> r.to_dictionary()
            {"id": 4, "width": 1, "height": 1, "x": 2, "y": 3}
        """
        attrs = ["id", "width", "height", "x", "y"]
        return {k: getattr(self, k) for k in attrs}
