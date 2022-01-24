#!/usr/bin/python3

"""write a function that prints the first name and the last name
The result have to be a string
The objectif of this exercices is to learn about testing a function
So we create function that prints a string
and create at least 5 tests to check the function"""


def say_my_name(first_name, last_name=""):

    """write a function that prints the first name and the last name
    if the first_name or last_name is not a string print an error message
    """


    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
