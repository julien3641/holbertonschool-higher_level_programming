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
