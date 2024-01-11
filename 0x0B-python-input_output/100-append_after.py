#!/usr/bin/python3

"""Module defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after
    each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for within the file.
        new_string (str): The line of text to insert after matching lines.
    """
    with open(filename, 'r+') as f:
        lines = ''
        for line in f:
            lines += line
            if search_string in line:
                lines += new_string
        f.seek(0)
        f.write(lines)
