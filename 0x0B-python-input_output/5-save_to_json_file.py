#!/usr/bin/python3

"""Module defines save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to be added.
        filename: file to add object.
    """
    with open(filename, 'w') as f:
        json.dumps(my_obj, f)
