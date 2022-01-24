#!/usr/bin/python3

"""write a function that add to integer
The result will be a integer
The objectif of this exercices is to learn about testing a function
So we create a function to add two numbers
and create at least 9 tests to check the function"""


def add_integer(a, b=98):

    """write a function that add to integer
    if the number is not a float change it into an integer
    if the number is nor an integer or a float display the error message"""

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return int(a) + int(b)
