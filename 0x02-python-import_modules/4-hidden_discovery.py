#!/usr/bin/python3
import hidden_4
for hidden in dir(hidden_4):
    if hidden[0:2] != "__":
        print("{}".format(hidden))

if __name__ == "__main__":
    hidden_4
