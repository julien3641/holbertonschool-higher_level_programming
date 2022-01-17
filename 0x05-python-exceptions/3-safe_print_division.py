#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if b != 0:
            result = a / b
            return result
        else:
            result = None
    except ZeroDivisionError:
        print("Inside result: {}".format(result))
    finally:
        print("Inside result: {}".format(result))
