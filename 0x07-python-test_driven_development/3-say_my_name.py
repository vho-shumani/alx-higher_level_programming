#!/usr/bin/python3
"""
module defines function that print message.

Function:
    - say_my_name(first_name, last_name=""): prints My name is <first name> <last name>,
    raises TypeError if arguments are not strings.
"""


def say_my_name(first_name, last_name=""):
    """My name is <first name> <last name>

Args:
    first_name (string): The first string.
    last_name (string): The second string.

Raises:
    TypeError: if argument is not string.
"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
