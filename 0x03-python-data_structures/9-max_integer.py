#!/usr/bin/python3
def max_integer(my_list=[]):

    if my_list == []:
        return
    largest = 0
    for i in range(0, len(my_list)):
        if (my_list[i] > largest):
            largest = my_list[i]
    return largest
