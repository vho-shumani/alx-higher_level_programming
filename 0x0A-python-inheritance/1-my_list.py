#!/usr/bin/python3

"""Module defines a class that inherits list"""


class MyList(list):
    """A list class that inherits from the built-in list class and provides a method to print the list in sorted order.

    Methods:
        print_sorted(self):
            Prints the elements of the list in ascending sorted order.
    """

    def print_sorted(self):
        """Prints the elements of the list in ascending sorted order.
        
        Args:
            self: The MyList instance itself.
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
