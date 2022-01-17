#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (ZeroDivisionError, AttributeError, IndexError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(None)
