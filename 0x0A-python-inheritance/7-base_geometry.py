#!/usr/bin/python3

"""Module define BaseGeometry class"""


class BaseGeometry:
    """ define a square with given size

        method:
        area: raises exception.
        integer_validator: Validates value.
    """
    def area(self):
        """Raises exception with message

        arg:
        self: BaseGeometry itself.

        Raise:
        Exception: raises Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates given value

        args:
        name (str): used to determine if its a string.
        value (int): used to determine if its int
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
