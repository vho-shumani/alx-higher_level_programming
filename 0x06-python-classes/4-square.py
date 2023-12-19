#!/usr/bin/python3
"""define a empty class"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """
        define a square with given size

        attributes:
        size (int): size of the square
        """
        self.__size = size

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

    def area(self):
        return self.__size ** 2
