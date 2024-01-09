#!/usr/bin/python3

"""Module defines load_from_json_file"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
        filename: file create object from.
    """
    with open(filename, 'r') as f:
        return json.load(f)
