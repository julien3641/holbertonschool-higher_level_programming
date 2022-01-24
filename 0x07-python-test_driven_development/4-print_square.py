#!/usr/bin/python3

"""Write a function that print a square of #
Size of the square is the size variable
There must some exceptions messages
if the size is less than 0 print a value error
and the size must be an integer"""

def print_square(size):

    """
    Function that print a square of size 'size'
    if the size is 0 print enter
    if the size is not a int print size must be an integer
    if the size is a float and < 0 print size must be an integer
    if the size is < 0 print Value error size must be >= 0
    """

    if size == 0:
        print()
    if type(size) != int or type(size) == float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
