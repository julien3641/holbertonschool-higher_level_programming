#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == None:
        return 0
    coeff = 0
    moy = 0
    for i in range(len(my_list)):
        coeff += my_list[i][1]
        moy += my_list[i][0] * my_list[i][1]
    moyenne = moy / coeff
    return moyenne
