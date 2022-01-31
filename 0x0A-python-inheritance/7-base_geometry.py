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
