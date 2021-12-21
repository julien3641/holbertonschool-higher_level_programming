#!/usr/bin/python3
for number in range(0, 10):
    for number1 in range(0, 10):
        if (number < number1):
            print("{:d}".format(number), end="")
            if (number == 8 and number1 == 9):
                print("{:d}".format(number1))
            else:
                print("{:d}".format(number1), end=", ")
