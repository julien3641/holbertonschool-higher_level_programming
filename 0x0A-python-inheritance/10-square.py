#!/usr/bin/python3

"""Write a class BaseGeometry with a public instance"""


class BaseGeometry:
    """ def area that raise an exception message"""

    def area(self):
        raise Exception("area() is not implemented")

    """ public instance method that validate the type of value"""

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ write a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """ calculate the area of the Rectangle"""

    def area(self):
        return self.__width * self.__height

    """ def str to return the description of the Rectangle"""

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


""" create a class square of inheritance from Rectangle"""


class Square(Rectangle):
    """ defined a square of size "size by size" """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    """ function that compute the area of the square"""

    def area(self):
        return self.__size * self.__size
