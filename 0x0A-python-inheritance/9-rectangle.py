#!/usr/bin/python3

"""Module defines rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """accepts with and validate width and height

    Attributes:
    Width: the with of rectangle.
    height: the height of a rectangle.

    Methods:
    area: return the area of rectangle
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator('width', self.__width)
        super().integer_validator('height', self.__height)

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'
