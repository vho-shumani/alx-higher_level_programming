#!/usr/bin/python3

"""Module defines MyInt class"""


class MyInt(int):
    """changes the == operator to != operator

    Methods:
    eq: Inverts the == operator.
    ne: Inverts the != operator.
    """
    def __eq__(self, other):
        """Inverts the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator"""
        return super().__eq__(other)
