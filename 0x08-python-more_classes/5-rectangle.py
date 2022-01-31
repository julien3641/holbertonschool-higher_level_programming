#!/usr/bin/python3

"""
This function is about to create a class named Rectangle
Where there will be a private instance attribute width
Return the area of the rectangle
and the perimeter of the rectangle

"""


class Rectangle:

    """Class that definies a rectangle
    The __init__ method is run as soon as the abject class is intantiated
    widht of the rectangle
    height ot the rectangle"""

    def __init__(self, width=0, height=0):

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    def __str__(self):
        """print a rectangle in #"""
        new_str = ""
        if self.__width == 0 and self.__height == 0:
            return new_str
        for i in range(self.__height):
            for j in range(self.__width):
                new_str += '#'
            if i < self.__height - 1:
                new_str += "\n"
        return new_str

    def __repr__(self):
        """Python __repr__() function change the returns
        the object representation in string format"""
        return "Rectangle({}, {})".format(
            eval(str(self.__width)), eval(str(self.__height)))

    def __del__(self):
        """Print the message when the instance of Rectangle is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Property Method return the width of the recaangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property method return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle Area"""
        return self.__width * self.__height

    def perimeter(self):
        """Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return
        return (self.__width * 2) + (self.__height * 2)
