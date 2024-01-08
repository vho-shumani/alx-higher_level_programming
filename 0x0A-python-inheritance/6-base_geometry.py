#!/usr/bin/python3

"""Module defines BaseGeometry class"""


class BaseGeometry:
    """ define a square with given size

        method:
        area: raises exception.
    """
    def area(self):
        """Raises exception with message

        arg:
        self: BaseGeometry itself.
        """
        raise Exception("area() is not implemented")
