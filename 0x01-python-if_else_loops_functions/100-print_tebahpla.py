#!/usr/bin/python3
for idx in range(122, 96, -1):
    if idx % 2 != 0:
        alpha = idx - 32
    else:
        alpha = idx
    print("{}".format(chr(alpha)), end="")
