#!/usr/bin/python3
"""Module defines Square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """defines a square and inherits from rectangle
    
    Attributes:
        size (int): size of the square.
        X (int): optional default value of 0, horizontal position of square.
        y (int): optional default value of 0, vertical position of square.
        id (int): optional default value None, id of object.
        
    Methods:
    init: initializes the attributes.
    str: returns a formatted string.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initiatialize the attributes
        
        Args:
            size (int): size of the square.
            X (int): optional default value of 0, horizontal position of square.
            y (int): optional default value of 0, vertical position of square.
            id (int): optional default value None, id of object.
        """
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """Return formatted string"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    def get_size(self):
        """return the value of size"""
        return self.width
    
    def set_size(self, size):
        """sets the value of size"""
        super().set_width(size)
        super().set_height(size)
        
    size = property(get_size, set_size)
    
    def update(self, *args, **kwargs):
        """updates value of attributes"""
        if args == None or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

s1 = Square(5)
s2 = Square(7, 9, 1)
list_squares_input = [s1, s2]

Square.save_to_file(list_squares_input)

list_squares_output = Square.load_from_file()

for square in list_squares_input:
    print("[{}] {}".format(id(square), square))

print("---")

for square in list_squares_output:
    print("[{}] {}".format(id(square), square))