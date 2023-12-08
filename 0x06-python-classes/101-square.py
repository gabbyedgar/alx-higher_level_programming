#!/usr/bin/python3


class Square:
    """Class to represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or \
           len(value) is not 2 or \
           any(map(lambda x: type(x) is not int or x < 0, value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        ret = ""
        if self.__size is 0:
            return ret
        else:
            ret = "\n" * self.__position[1]
            for i in range(self.__size):
                ret += " " * self.__position[0]
                ret += "#" * self.__size
                ret += "\n" if i < self.__size - 1 else ""
        return ret
