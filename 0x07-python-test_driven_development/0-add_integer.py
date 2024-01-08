#!/usr/bin/python3
"""
module provides addition function.

Function:
    - add(x, y): Adds two numbers together,
    raises TypeError if number is not interger or float.
"""


def add_integer(a, b=98):
    """Adds two numbers together.

Args:
    a (int or float): The first number to add.
    b (int or float): The second number to add.

Returns:
    int: The sum of a and b.

Raises:
    TypeError: if number is number is not int or float.
"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(a, float):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
