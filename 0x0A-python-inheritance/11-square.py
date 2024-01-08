#!/usr/bin/python3

"""Module defines Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square

    Attribute:
    size: size of a square
    """
    def __init__(self, size):
        self.__size = size
        super().integer_validator('size', self.__size)
        super().__init__(size, size)

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
