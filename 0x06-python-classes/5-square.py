#!/usr/bin/python3
"""define a empty class"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        define a square with given size

        attributes:
        size (int): size of the square
        position: 
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

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size is not 0:
            for i in range(0, self.__size):
                print("#" * self.__size)
        else:
            print()
            
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if len(value) < 2 or not all(elements > 0 for elements in value):
            raise TypeError("position must be a tuple of 2 positive integers")
