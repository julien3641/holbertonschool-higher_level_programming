#!/usr/bin/python3
"""Write a function that adds a new attribute to an object
if it’s possible:
Raise a TypeError exception, with the message
can't add new attribute if the object can’t have new attribute
You are not allowed to use try/catch
You are not allowed to import any module
"""


def add_attribute(obj, name, value):
    """add a new attribute to an object """
    if isinstance(obj, (int, float, str, tuple, bool, dict, frozenset)):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
