#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = 0
    if len(argv) == 0:
        print("{}".format(count))
    for argument in range(1, len(argv)):
        count += int(argv[argument])
    print("{}".format(count))
