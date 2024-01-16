#!/usr/bin/python3
"""Module defines Rectangle class that inherits from Base class"""
from base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base class
    
    Attributes:
        width: width of rectangle.
        height: height of rectangle.
        x: horizontal position of rectangle.
        y: vertical position of rectangle.
        
    Methods:
        init: initailizes attributes.
        get_width: return value of width.
        set_width: sets value of width.
        get_height: return value of height.
        set_height: sets value of height.
        get_x: return value of x.
        set_x: sets value of x
        get_y: return value of y.
        set_y: sets value of y.
        area: return area of rectangle
        str: prints out a formatted string.
        display: diplay rectangle with character #.
        update: updates the value of attribute.
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes  Rectangle objects

        Args:
            width: width of rectangle.
            height: height of the rectangle.
            x: optional with the default value of 0.
            y: optional value with the valuee of 0.
        """
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)
        super().__init__(id)

    def get_width(self):
        """Return value of width"""
        return self.__width

    def set_width(self, new_width):
        """set value of the width"""
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")
        elif new_width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = new_width

    width = property(get_width, set_width)

    def get_height(self):
        """Return value of height"""
        return self.__height

    def set_height(self, new_height):
        """set value of height"""
        if not isinstance(new_height, int):
            raise TypeError("height must be an integer")
        elif new_height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = new_height

    height = property(get_height, set_height)

    def get_x(self):
        """Return value of x"""
        return self.__x

    def set_x(self, new_x):
        """set value of x"""
        if not isinstance(new_x, int):
            raise TypeError("x must be an integer")
        elif new_x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = new_x

    x = property(get_x, set_x)

    def get_y(self):
        """Return value of y"""
        return self.__y

    def set_y(self, new_y):
        """set value of y"""
        if not isinstance(new_y, int):
            raise TypeError("y must be an integer")
        elif new_y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = new_y

    y = property(get_y, set_y)

    def area(self):
        """Return the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle with the character"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print((' ' * self.x) + ('#' * self.width))

    def __str__(self):
        """Return a string"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute:"""
        if args == None or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:    
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
            
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {key.replace('_Rectangle__', ''): value for key, value in self.__dict__.items()}

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]

Rectangle.save_to_file(list_rectangles_input)

list_rectangles_output = Rectangle.load_from_file()

for rect in list_rectangles_input:
    print("[{}] {}".format(id(rect), rect))

print("---")

for rect in list_rectangles_output:
    print("[{}] {}".format(id(rect), rect))