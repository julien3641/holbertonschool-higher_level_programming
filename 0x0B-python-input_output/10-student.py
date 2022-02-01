#!/usr/bin/python3
"""Write a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self):
that retrieves a dictionary representation
of a Student instance (same as 8-class_to_json.py)
If attrs is a list of strings, only attribute names
contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initialize a class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve a dictionary representation"""
        if attrs is None:
            return self.__dict__
        mydict = {}
        for i in attrs:
            if i in self.__dict__:
                mydict[i] = self.__dict__[i]
        return mydict
