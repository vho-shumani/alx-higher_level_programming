#!/usr/bin/python3
"""define a empty class"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        define a square with given size

        attributes:
        size (int): size of the square
        position: position of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) < 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(n, int) and n > 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(0, self.__position[1]):
            print()
        if self.__size is not 0:
            for i in range(0, self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
        else:
            print()
