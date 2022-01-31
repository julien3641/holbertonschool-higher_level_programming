#!/usr/bin/python3

"""Write a function that return True or False
    if the object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):

    """ function that return True if the object is an instance
     or if the object is an instance of a class"""

    return isinstance(obj, a_class)
