#!/usr/bin/python3
"""creating a new class Reactangle"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """
        defines a rectangle with given values

        attributes:
        width: width of a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle with character #"""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(0, self.height):
            print(self.width * '#', end="")
            if i is not self.height - 1:
                print()
        return ""

    def __repr__(self):
        """return string representation of rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints message when instance of class is deleted"""
        print("Bye rectangle...")
