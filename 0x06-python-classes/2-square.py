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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0") 
