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

    """ write a class Rectangle tha inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Arguments:
        @width: width size
        @height: height size
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
