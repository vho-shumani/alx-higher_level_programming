#!/usr/bin/python3

"""Module define class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """accepts with and validate width and height

    Attributes:
    Width: the with of rectangle.
    height: the height of a rectangle.
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator('width', self.__width)
        super().integer_validator('height', self.__height)
