#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.

        Args:
            width (int): width of rectangle with value >= 0.
            height (int): height of rectangle with value >= 0.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Getter function for `height` attribute.

        Returns: value of `height` attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for `height` attribute.

        Args:
            value (int): value to use for `height`.

        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """Getter function for `width` attribute.

        Returns: value of `width` attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for `width` attribute.

        Args:
            value (int): value to use for `width`.

        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Method to compute area of Rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Method to compute perimeter length of Rectangle instance.

        Returns: 2 * (w + h) if both `width` and `height` > 0, else 0.
        """
        return 2*(self.width + self.height) * bool(self.width and self.height)

    def __str__(self):
        """Format Rectangle instance for printing as a grid of `#`.

        Returns: string contain `width` columns and `height` rows of `#`.
        """
        rect = ""
        for i in range(self.height):
            rect += '#'*self.width + '\n'
        return rect[:-1]

    def __repr__(self):
        """Format Rectangle instance so that eval(self.__repr__())
        creates a new similar instance.

        Returns: string representation to recreate object.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
