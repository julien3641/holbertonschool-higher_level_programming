#!/usr/bin/python3
def max_integer(my_list=[]):

    if my_list == "":
        return None
    largest = 0
    for i in range(len(my_list)):
        if (my_list[i] > largest):
            largest = my_list[i]
    return largest
